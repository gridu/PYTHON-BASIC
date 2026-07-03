import ast
import json
import random
import sys
import time
import uuid
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Callable, Dict, List, Literal, Tuple

from capstone.model import CleanArgs


class OutputDirectoryNotPrepared(Exception):
    pass


def prepare_output_directory(
    output_dir_path_str: str, file_name: str, clean_required: bool
):
    output_dir_path = Path(output_dir_path_str)
    if output_dir_path.exists() and output_dir_path.is_dir():
        if clean_required:
            del_count = 0
            for item in output_dir_path.iterdir():
                if item.is_file() and item.name.startswith(file_name):
                    item.unlink()
                    del_count += 1
            print(f"INFO: Deleted {del_count} files from {output_dir_path}")
    else:
        output_dir_path.mkdir(parents=True, exist_ok=True)
        print("INFO: Output directory didn't exist, so it was created.")


def create_list_of_output_files_paths(
    output_dir_path_str: str,
    file_name: str,
    file_prefix: Literal["count", "random", "uuid"],
    files_to_create: int,
) -> list[Path]:
    output_dir_path = Path(output_dir_path_str)
    prefixes = []
    match file_prefix:
        case "count":
            prefixes = [i for i in range(1, files_to_create + 1)]
        case "random":
            # there is no definition in docs what random means so i will do this:
            prefixes = random.sample(range(1, 500), k=files_to_create)
        case "uuid":
            prefixes = [str(uuid.uuid4()) for _ in range(files_to_create)]
    output_files = [
        output_dir_path / f"{output_dir_path}" / f"{file_name}_{prefixes[i]}.json"
        for i in range(files_to_create)
    ]
    return output_files


# Workers helper function. Shared between File Workers and Console workers
def _compile_generators(
    data_schema: Dict[str, str],
) -> List[Tuple[str, Callable[[], Any]]]:
    generators = []
    for key, value in data_schema.items():
        data_type, instruction = value.split(":", 1)
        data_type, instruction = data_type.strip(), instruction.strip()

        if data_type == "timestamp":
            generators.append((key, lambda: time.time()))
            continue
        if not instruction:
            generators.append((key, lambda dt=data_type: None if dt == "int" else ""))
            continue
        if instruction == "rand":
            if data_type == "str":
                generators.append((key, lambda: str(uuid.uuid4())))
            elif data_type == "int":
                generators.append((key, lambda: random.randint(0, 10000)))
            continue
        if instruction.startswith("rand(") and instruction.endswith(")"):
            bounds = instruction[5:-1].split(",")
            low, high = int(bounds[0].strip()), int(bounds[1].strip())
            generators.append((key, lambda lo=low, hi=high: random.randint(lo, hi)))
            continue
        if instruction.startswith("[") and instruction.endswith("]"):
            parsed_list = ast.literal_eval(instruction)
            generators.append((key, lambda choices=parsed_list: random.choice(choices)))
            continue

        generators.append(
            (key, lambda v=int(instruction) if data_type == "int" else instruction: v)
        )

    return generators


# File Worker
def create_file(
    output_path: Path, data_schema: Dict[str, str], num_of_lines: int
) -> str:
    if not output_path.parent.exists():
        raise OutputDirectoryNotPrepared(
            "You probably forgot to run prepare_output_directory function before creating files"
        )
    generators = _compile_generators(data_schema)

    with open(output_path, "w", encoding="utf-8") as file:
        for _ in range(num_of_lines):
            row_data = {key: gen() for key, gen in generators}
            file.write(json.dumps(row_data) + "\n")

    return f"INFO: Successfully created file: {output_path}"


# Console Worker (not worker anymore but lets keep it that way)
def print_schema_to_console(data_schema: Dict[str, str], num_of_lines: int) -> str:
    generators = _compile_generators(data_schema)

    for _ in range(num_of_lines):
        row_data = {key: gen() for key, gen in generators}
        line_str = json.dumps(row_data) + "\n"

        sys.stdout.write(line_str)

    print("INFO: Successfully streamed data chunk to console.")


def perform_file_generation(clean_args: CleanArgs):
    output_files_paths = create_list_of_output_files_paths(
        clean_args.abs_path_to_save,
        clean_args.file_name,
        clean_args.file_prefix,
        clean_args.files_count,
    )

    with ProcessPoolExecutor(max_workers=clean_args.multiprocessing) as executor:
        futures = [
            executor.submit(
                create_file, path, clean_args.data_schema, clean_args.data_lines
            )
            for path in output_files_paths
        ]
        for future in as_completed(futures):
            try:
                result = future.result()
                print(result)
            except Exception as e:
                print(f"ERROR: Worker crashed with error: {e}", file=sys.stderr)


def orchestrate_data_generation(clean_args: CleanArgs):
    only_console = clean_args.files_count == 0

    if only_console:
        print_schema_to_console(clean_args.data_schema, clean_args.data_lines)
    else:
        perform_file_generation(clean_args)
