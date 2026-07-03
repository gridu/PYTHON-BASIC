import ast
import logging
import os
import sys
from typing import Dict, Literal

from pydantic import BaseModel, Field, field_validator


class CleanArgs(BaseModel):
    abs_path_to_save: str
    files_count: int = Field(ge=0)
    file_name: str
    file_prefix: Literal["count", "random", "uuid"]
    data_schema: Dict[str, str]
    data_lines: int = Field(ge=0)
    clear_path: bool = False
    multiprocessing: int = Field(g=0)

    @field_validator("data_schema")
    @classmethod
    def validate_schema_structure(cls, schema: Dict[str, str]) -> Dict[str, str]:
        for key, value in schema.items():
            if ":" not in value:
                print(
                    f"Error: Invalid schema for key '{key}'. Value '{value}' is missing the ':' separator.",
                    file=sys.stderr,
                )
                sys.exit(1)
            data_type, instruction = value.split(":", 1)
            data_type = data_type.strip()
            instruction = instruction.strip()

            if not instruction:
                # empty value is always allowed
                continue

            match data_type:
                case "str":
                    if instruction == "rand":
                        # str:rand allowed
                        pass

                    elif instruction.startswith("rand("):
                        # str:rand(from,to) not allowed, that bracket rand is reserved for ints
                        print(
                            f"Error: 'rand(from, to)' notation is only compatible with 'int' type. "
                            f"Key '{key}' cannot use it with 'str'.",
                            file=sys.stderr,
                        )
                        sys.exit(1)

                    elif instruction.startswith("[") and instruction.endswith("]"):
                        # str:list is allowed but must be valid list
                        try:
                            parsed_list = ast.literal_eval(instruction)
                            if not isinstance(parsed_list, list):
                                raise ValueError
                        except (ValueError, SyntaxError):
                            print(
                                f"Error: Invalid list format for key '{key}': '{instruction}'",
                                file=sys.stderr,
                            )
                            sys.exit(1)
                    else:
                        # standalone value is always allowed for strings
                        pass

                case "int":
                    if instruction == "rand":
                        # int:rand is allowed.
                        pass

                    elif instruction.startswith("rand(") and instruction.endswith(")"):
                        # int:rand(from,to) is allowed but must be correct
                        try:
                            bounds = instruction[5:-1].split(",")
                            num_from = int(bounds[0].strip())
                            num_to = int(bounds[1].strip())
                            if num_from > num_to:
                                raise ValueError()
                        except (ValueError, IndexError):
                            print(
                                f"Error: Invalid range boundaries in '{instruction}' for key '{key}'. "
                                f"Values must be integers and second number must be greater than or equal to the first ",
                                file=sys.stderr,
                            )
                            sys.exit(1)

                    elif instruction.startswith("[") and instruction.endswith("]"):
                        # int:list is allowed but must be valid list
                        try:
                            parsed_list = ast.literal_eval(instruction)
                            if not isinstance(parsed_list, list):
                                raise ValueError
                        except (ValueError, SyntaxError):
                            print(
                                f"Error: Invalid list format for key '{key}': '{instruction}'",
                                file=sys.stderr,
                            )
                            sys.exit(1)

                    else:
                        # standalone value must be convertible to int
                        try:
                            int(instruction)
                        except ValueError:
                            print(
                                f"Error: Standalone value '{instruction}' for key '{key}' "
                                f"cannot be converted to 'int' type.",
                                file=sys.stderr,
                            )
                            sys.exit(1)

                case "timestamp":
                    # timestamp should ignore anything that comes after ':'
                    logging.warning(
                        f"Note: 'timestamp' type for key '{key}' does not support extra expressions. "
                        f"The instruction '{instruction}' will be ignored and current UNIX timestamp will be used."
                    )

                case _:
                    # Unknown type
                    print(
                        f"Error: Unsupported type '{data_type}' for key '{key}'. "
                        f"Allowed types are 'str', 'int', or 'timestamp'.",
                        file=sys.stderr,
                    )
                    sys.exit(1)

        return schema

    @field_validator("multiprocessing")
    @classmethod
    def cap_to_cpu_count(cls, value: int) -> int:
        if value <= 0:
            print(
                "Error: Invalid value for --multiprocessing",
                "Value must be >=1 ",
                file=sys.stderr,
            )
            sys.exit(1)
        cpu_count = os.cpu_count() or 1
        if value > cpu_count:
            logging.warning(
                f"Note: Requested multiprocessing count ({value}) exceeds maximum available CPU cores ({cpu_count}). "
                f"Overriding and capping process count to {cpu_count}."
            )
            return cpu_count
        return value
