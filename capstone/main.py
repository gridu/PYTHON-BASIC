import logging

from capstone.arguments_cleaning import (
    gather_args_and_config_parser,
    get_clean_arguments,
)
from capstone.data_generation import (
    orchestrate_data_generation,
    prepare_output_directory,
)


def configure_logging() -> None:
    logging.basicConfig(level=logging.INFO)


def main():
    configure_logging()

    args_raw = gather_args_and_config_parser()
    args_clean = get_clean_arguments(args_raw)

    prepare_output_directory(
        args_clean.abs_path_to_save, args_clean.file_name, args_clean.clear_path
    )

    orchestrate_data_generation(clean_args=args_clean)


if __name__ == "__main__":
    main()
