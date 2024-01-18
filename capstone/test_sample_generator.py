import logging
from typing import Callable

import pytest
# Types testing
from sample_generator import parsers, list_pattern, rand_pattern, \
    parsing_schema_err, parsing_schema_warning
# Generating testing
from sample_generator import parse_data_schema, generate_data
from sample_generator import main
from sample_generator import clear_existing_files
from sample_generator import save
import uuid
import random
import time
import json
import tempfile
import os


def check_uuid(uuid_to_test: str, t: str, tv: str, version=4) -> bool:
    try:
        uuid_obj = uuid.UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test


def check_one_of(val_to_test: str, t: str, tv: str):
    val = list(map(lambda x: int(x) if t == 'int' else str.strip(x) if t == 'str' else None,
                   list_pattern.findall(tv)[0].split(",")))
    return (val_to_test in val) and type(val_to_test).__name__ == t


check_str_const: Callable[[str, str, str], bool] = \
    lambda val_to_test, t, tv: val_to_test == tv and type(val_to_test).__name__ == t


def check_int_rand(val_to_test: str, t: str, tv: str):
    return val_to_test in range(0, 10000) and type(val_to_test).__name__ == t


def check_int_rand_range(val_to_test: str, t: str, tv: str):
    low = int(rand_pattern.findall(tv)[0][0])
    high = int(rand_pattern.findall(tv)[0][1])
    return val_to_test in range(low, high) and type(val_to_test).__name__ == t


def check_time(val_to_test: float, t: str, tv: str):
    current_time = time.time()
    tolerance = 100
    return (current_time - tolerance <= val_to_test <= current_time + tolerance) and \
        type(val_to_test).__name__ == 'float'


DATA_TYPE_EXPECTED = {
    "str": {"rand": check_uuid,
            "[' str1 subs1', 'subs2 str2 ', 'str3']": check_one_of,
            "rand(123, 234)": 'exit_status_and_log_message',
            "Any Str": check_str_const,
            "{}": check_str_const,
            "None": check_str_const,
            },
    "int": {"rand": check_int_rand,
            "[1, 2, 3]": check_one_of,
            "rand(123, 234)": check_int_rand_range,
            "Any Str": 'exit_status_and_log_message',
            "2123": lambda val_to_test, t, tv: val_to_test == int(tv) and type(val_to_test).__name__ == t,
            "": lambda val_to_test, t, tv: val_to_test is None and type(val_to_test).__name__ == "NoneType",
            '123.456': 'exit_status_and_log_message',
            },
    "timestamp": {
        "rand(123, 234)": 'exit_status_and_log_message',
        "": check_time,
        "asdas": 'check_time_warning',
        "{}": 'check_time_warning',
        "[1,2,3]": 'check_time_warning',
    }
}


def exit_status_and_log_message(f, t, tv, caplog):
    with pytest.raises(SystemExit) as ex_info:
        f(t, tv)

    err_msg = parsing_schema_err.format(t=t, tv=tv)
    # Check if method exits with status 1 and log message is present in the captured logs
    return ex_info.value.code == 1 and any(err_msg in record.message for record in caplog.records)


def check_time_warning(f, t, tv, caplog):
    time_val = eval(f(t, tv))

    err_msg = parsing_schema_warning.format(t=t, tv=tv)
    # Check if log message is present in the captured logs
    return check_time(time_val, t, tv) and any(err_msg in record.message for record in caplog.records)


def types_match(data_schema: dict, generated_data: dict) -> bool:
    for k, v in data_schema.items():
        g_type_name = type(generated_data.get(k)).__name__
        s_type_name = v.split(":")[0]
        tv = v.split(":")[1].strip()
        if s_type_name == 'timestamp':
            return g_type_name == 'float'
        elif s_type_name == 'int' and tv == '':
            return g_type_name == 'NoneType'
        else:
            return g_type_name == s_type_name


# Write a parameterized test for different data types.
class TestTypes:
    types_make_expected = [[t, f, r] for t, ex in DATA_TYPE_EXPECTED.items() for f, r in ex.items()]

    @pytest.mark.parametrize("test_type, test_input, expected", types_make_expected)
    @pytest.mark.usefixtures("caplog")
    def test_data_types(self, test_type, test_input, expected, caplog):
        if expected == 'exit_status_and_log_message':
            assert exit_status_and_log_message(f=parsers[test_type], t=test_type, tv=test_input, caplog=caplog)
        elif expected == 'check_time_warning':
            assert check_time_warning(f=parsers[test_type], t=test_type, tv=test_input, caplog=caplog)
        else:
            val = parsers[test_type](test_type, test_input)
            if type(val).__name__ == "str":
                val = eval(parsers[test_type](test_type, test_input))
            assert expected(val, test_type, test_input)


DATA_SCHEMA_EXPECTED = {
    "happy_path": [
        # Happy paths
        {"key1": "str:rand", "key2": "int:[1, 2, 3]", "key3": "timestamp:{}"},
        {"date":"timestamp:", "name": "str:rand", "type": "str:['client', 'partner', 'government']", "age": "int:rand(1, 90)"},
        # Test cases for 'str' type
        {"key1": "str:rand", "key2": "str:['apple', 'banana', 'cherry']", "key3": "str:{}"},
        # Test cases for 'int' type
        {"key4": "int:rand(10, 20)", "key5": "int:[1, 2, 3]", "key6": "int:100"},
        # Test cases for 'timestamp' type
        {"key7": "timestamp:{}", "key8": "timestamp:"},
        # Edge cases
        {"key12": "str:", "key13": "int:"}
    ],
    "bad_scenario": [
        # Bad scenario: Exit(1)
        # Empty values
        {"key15": "", "key16": "", "key17": ""},
        # timestamp should not have rand range
        {"key1": "int:rand(10, 20)", "key2": "str:['apple', 'banana', 'cherry']", "key3": "timestamp:rand(100, 200)"},
        # str should not have rand range
        {"key1": "int:rand(10, 20)", "key2": "str:rand(123, 234)"}
    ],
}


# Write a parameterized test for different data schemas.
class TestDataSchema:
    data_schema_make_expected = [(s, tc) for s, test_cases in DATA_SCHEMA_EXPECTED.items() for tc in test_cases]

    @pytest.mark.parametrize("scenario, data_schema", data_schema_make_expected)
    @pytest.mark.usefixtures("caplog")
    def test_data_schema(self, scenario, data_schema, caplog):
        if scenario == 'happy_path':
            # Parse the data schema
            parsed_schema = parse_data_schema(data_schema)
            # Generate data based on the parsed schema
            generated_data = generate_data(parsed_schema)

            # Check is all keys are present
            assert set(data_schema.keys()) == set(generated_data.keys())
            # Check if generated types match
            assert types_match(data_schema, generated_data)

        # Bad scenario
        else:
            # Try to Parse the data schema
            with pytest.raises(SystemExit) as ex_info:
                parse_data_schema(data_schema)
                # Check if method exits with status 1
                assert ex_info.value.code == 1


# This is a class with fixture which could be reused in number of other Test classes
class TestSimpleData:

    @pytest.fixture
    def temp_dir(self, tmp_path):
        d = tmp_path / "dr"
        d.mkdir()
        yield d
        d.rmdir()

    data_schema = {
        "field1": "str:rand",
        "field2": "int:rand(1, 100)",
        "field3": "timestamp:"
    }
    args = [
        "--files_count", "1",
        "--file_name", "output_file",
        "--file_prefix", "count",
        "--data_lines", "5",
        "--multiprocessing", "1"
    ]


# Write a test that uses temporary files to test your program when the data schema is loaded with a json file.
# You have to use fixtures here.
class TestSchemaLoad(TestSimpleData):
    @pytest.fixture
    def temp_data_schema_file(self):
        # Create a temporary JSON file with a predefined data schema

        with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
            json.dump(self.data_schema, temp_file)
            temp_file_path = temp_file.name

        yield temp_file_path

        # Clean up: Remove the temporary file
        os.remove(temp_file_path)

    def test_main_with_temp_data_schema(self, temp_data_schema_file, monkeypatch, temp_dir):
        args = TestSimpleData.args + [
            "--data_schema", temp_data_schema_file,
            "--path_to_save_files", str(temp_dir),
        ]

        monkeypatch.setattr("sys.argv", ["sample_generator.py"] + args)
        main()

        # Check if file exists
        result_file_path = os.path.join(temp_dir, "output_file_0.json")
        assert os.path.exists(result_file_path)

        # Read and Validate the results file
        with open(result_file_path, "r") as result_file:
            result_data = json.load(result_file)

        # Test if 5 record were generated
        assert len(result_data) == 5
        # Check if all keys are present and types match
        for r in result_data:
            assert set(self.data_schema.keys()) == set(r.keys())
            assert types_match(self.data_schema, r)

        # Clean up: Remove the result file
        os.remove(result_file_path)


# Test for the “clear_path” action.
class TestClearPath(TestSimpleData):
    args = TestSimpleData.args + [
        "--data_schema", f'{TestSimpleData.data_schema}'.replace("'", "\""),
    ]

    # The --clear_path is False. clear_existing_files should not be called
    def test_clear_path_not_called(self, monkeypatch, mocker, temp_dir):
        monkeypatch.setattr("sys.argv", ["sample_generator.py"] + self.args + ["--path_to_save_files", str(temp_dir)])
        mocked_clear_existing_files = mocker.patch('sample_generator.clear_existing_files')
        main()
        mocked_clear_existing_files.assert_not_called()

        # Clean up: Remove the result file
        result_file_path = os.path.join(temp_dir, "output_file_0.json")
        os.remove(result_file_path)

    # The --clear_path is Set. clear_existing_files should be called
    def test_clear_path_called(self, monkeypatch, mocker, temp_dir):
        monkeypatch.setattr("sys.argv", ["sample_generator.py"] + self.args +
                            ["--clear_path",
                             "--path_to_save_files", str(temp_dir)])
        mocked_clear_existing_files = mocker.patch('sample_generator.clear_existing_files')
        main()
        mocked_clear_existing_files.assert_called_once_with(str(temp_dir))

        # Clean up: Remove the result file
        result_file_path = os.path.join(temp_dir, "output_file_0.json")
        os.remove(result_file_path)

    # Test if it prints out logging message
    @pytest.mark.usefixtures("caplog")
    def test_clear_path_prints_logging_msg(self, monkeypatch, caplog, temp_dir):
        monkeypatch.setattr("sys.argv", ["sample_generator.py"] + self.args +
                            ["--clear_path",
                             "--path_to_save_files", str(temp_dir)])
        with caplog.at_level(logging.INFO):
            main()
        assert any(f'`{str(temp_dir)}` folder is cleaned up' in record.message for record in caplog.records)

        # Clean up: Remove the result file
        result_file_path = os.path.join(temp_dir, "output_file_0.json")
        os.remove(result_file_path)

    # Test if it deletes files
    def test_clear_path_deletes_files(self, temp_dir):
        # Create temporary files in the temporary folder
        for i in range(10):
            temp_file_path = os.path.join(temp_dir, f"temp_file{i}.txt")
            with open(temp_file_path, 'w') as temp_file:
                temp_file.write("I'm temporary file!")

        # Check if files exist
        for i in range(10):
            temp_file_path = os.path.join(temp_dir, f"temp_file{i}.txt")
            assert os.path.exists(temp_file_path)

        # It will delete all files and recreate base directory
        clear_existing_files(temp_dir)
        for i in range(10):
            temp_file_path = os.path.join(temp_dir, f"temp_file{i}.txt")
            assert not os.path.exists(temp_file_path)


# Test to check saving file to disk
class TestSave(TestSimpleData):
    # Should be called with given parameters
    def test_save(self, monkeypatch, temp_dir):
        result_file_path = os.path.join(temp_dir, "output_file_0.json")
        data = {"key": "value"}

        # Remove file if exists
        if os.path.exists(result_file_path):
            os.remove(result_file_path)
        assert not os.path.exists(result_file_path)

        save(data, temp_dir, "output_file.json", "0")
        assert os.path.exists(result_file_path)

        # Test if saved data match to original data
        with open(result_file_path, 'r') as file:
            saved_data = json.load(file)
        assert saved_data == data

        # Clean up: Remove the result file
        os.remove(result_file_path)


# Write a test to check a number of created files if “multiprocessing” > 1.
class TestNumberOfFiles(TestSimpleData):
    args = [
        "--file_name", "output_file",
        "--file_prefix", "count",
        "--data_lines", "5",
        "--data_schema", f'{TestSimpleData.data_schema}'.replace("'", "\""),
    ]

    files_mp = [(["--files_count", str(f), "--multiprocessing", str(m)], f) for m in [1,3,10] for f in [2,5]]

    @pytest.mark.parametrize("args_files_mp, expected", files_mp)
    def test_number_of_files_mp1(self, monkeypatch, temp_dir, args_files_mp, expected):
        monkeypatch.setattr("sys.argv",
                            ["sample_generator.py"] +
                            self.args +
                            ["--path_to_save_files", str(temp_dir)] +
                            args_files_mp)
        main()

        # Number of files should be as expected
        assert len(os.listdir(temp_dir)) == expected

        for f in os.listdir(temp_dir):
            result_file_path = os.path.join(temp_dir, f)

            # Test if saved data valid
            with open(result_file_path, 'r') as file:
                saved_data = json.load(file)
                # each file should contain 5 data lines
                assert len(saved_data) == 5
                for elem in saved_data:
                    assert set(TestSimpleData.data_schema.keys()) == set(elem.keys())
                    # Check if generated types match
                    assert types_match(TestSimpleData.data_schema, elem)

                # Clean up: Remove the result file
                os.remove(result_file_path)
