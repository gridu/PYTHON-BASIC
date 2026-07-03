from capstone.argmunets_cleaning import (
    gather_args_and_config_parser,
    get_clean_arguments,
)
from capstone.data_generation import (
    orchestrate_data_generation,
    prepere_output_direcotry,
)


def main():
    args_raw = gather_args_and_config_parser()
    args_clean = get_clean_arguments(args_raw)

    prepere_output_direcotry(
        args_clean.abs_path_to_save, args_clean.file_name, args_clean.clear_path
    )

    orchestrate_data_generation(clean_args=args_clean)

    # TODO somehow make it work with provided dataschemas


if __name__ == "__main__":
    main()
