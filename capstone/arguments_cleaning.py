import argparse
import configparser
import json
import sys
from pathlib import Path

from pydantic import ValidationError

import capstone.messages as messages
from capstone.model import CleanArgs


class CombinedFormatter(
    argparse.ArgumentDefaultsHelpFormatter, argparse.RawTextHelpFormatter
):
    """Combines default-value rendering with raw multi-line message support."""

    pass


def load_ini_defaults() -> dict:
    config = configparser.ConfigParser()
    ini_path = Path(__file__).parent / "default.ini"

    if not ini_path.exists():
        return {}

    config.read(ini_path)
    defaults = {}

    for key, value in config["DEFAULTS"].items():
        if value.lower() in ("true", "false"):
            defaults[key] = config["DEFAULTS"].getboolean(key)
        elif value.isdigit() or (value.startswith("-") and value[1:].isdigit()):
            defaults[key] = config["DEFAULTS"].getint(key)
        else:
            defaults[key] = value

    return defaults


def gather_args_and_config_parser():
    ini = load_ini_defaults()

    parser = argparse.ArgumentParser(
        prog="Console Data Generator",
        description="Generates mock data matching a provided custom data schema.",
        formatter_class=CombinedFormatter,
    )

    parser.add_argument(
        "--path_to_save_files",
        default=ini.get("path_to_save_files", "./output"),
        help=messages.PATH_SAVE_HELP,
    )

    parser.add_argument(
        "--files_count",
        default=ini.get("files_count", 1),
        help=messages.FILES_COUNT_HELP,
    )

    parser.add_argument(
        "--file_name",
        default=ini.get("file_name", "data"),
        help=messages.FILE_NAME_HELP,
    )

    parser.add_argument(
        "--file_prefix",
        default=ini.get("file_prefix", "count"),
        choices=["count", "random", "uuid"],
        help=messages.FILE_PREFIX_HELP,
    )

    fallback_schema = '{"date": "timestamp:", "name": "str:rand"}'
    parser.add_argument(
        "--data_schema",
        default=ini.get("data_schema", fallback_schema),
        help="The generation schema blueprint formatted as a JSON string.",
    )

    parser.add_argument(
        "--data_lines",
        default=ini.get("data_lines", 10),
        help=messages.DATA_LINES_HELP,
    )

    parser.add_argument(
        "--clear_path",
        action="store_true",
        default=ini.get("clear_path", False),
        help=messages.CLEAR_PATH_HELP,
    )

    parser.add_argument(
        "--multiprocessing",
        default=ini.get("multiprocessing", 1),
        help=messages.MULTIPROCESSING_HELP,
    )

    return parser.parse_args()


def get_clean_arguments(args: argparse.Namespace) -> CleanArgs:
    args_dict = vars(args)

    # Convert path to absolute
    raw_path = args_dict.pop("path_to_save_files", None)
    if raw_path:
        args_dict["abs_path_to_save"] = str(Path(raw_path).resolve())
    else:
        args_dict["abs_path_to_save"] = None

    schema_input = args_dict.get("data_schema")
    # Check if schema is path or string
    if isinstance(schema_input, str):
        schema_input = schema_input.strip()
        potential_file = Path(schema_input)

        # Path
        if potential_file.is_file():
            try:
                with open(potential_file, "r", encoding="utf-8") as file:
                    args_dict["data_schema"] = json.load(file)
            except json.JSONDecodeError:
                print(
                    f"Error: The schema file '{schema_input}' does not contain valid JSON.",
                    file=sys.stderr,
                )
                sys.exit(1)
            except Exception as e:
                print(
                    f"Error: Failed to read schema file '{schema_input}': {e}",
                    file=sys.stderr,
                )
                sys.exit(1)

        # String
        else:
            try:
                args_dict["data_schema"] = json.loads(schema_input)
            except json.JSONDecodeError:
                print(
                    "Error: The --data_schema provided is neither a valid file path nor a valid JSON string.",
                    file=sys.stderr,
                )
                sys.exit(1)

    try:
        return CleanArgs(**args_dict)

    except ValidationError as e:
        for error in e.errors():
            field_name = error["loc"][0]
            error_message = error["msg"]

            # Translation back to original name to not confuse user
            cli_flag = (
                "--path_to_save_files"
                if field_name == "abs_path_to_save"
                else f"--{field_name}"
            )

            print(
                f"Error: Invalid value for {cli_flag}. {error_message}.",
                file=sys.stderr,
            )

        sys.exit(1)
