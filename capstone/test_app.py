import json
import logging
import os
import sys
from pathlib import Path

import pytest

from capstone.arguments_cleaning import (
    gather_args_and_config_parser,
    get_clean_arguments,
)
from capstone.data_generation import (
    create_list_of_output_files_paths,
    orchestrate_data_generation,
    prepare_output_directory,
)
from capstone.model import CleanArgs


@pytest.fixture
def temp_schema_file(tmp_path):
    schema_data = {
        "id": "str:rand",
        "status": "str:['active', 'inactive']",
        "score": "int:rand(1, 100)",
    }
    file_path = tmp_path / "schema.json"
    file_path.write_text(json.dumps(schema_data))
    return file_path


@pytest.fixture
def temp_output_dir(tmp_path):
    for i in range(3):
        mock_data = {
            "date": "1534717897.967033",
            "name": "f82a44ac-daa7-4b8f-8569-83898fb9b312",
            "type": " partner",
            "age": 45,
        }
        file_path = tmp_path / f"mock_data_{i}.jsonl"
        file_path.write_text(json.dumps(mock_data))
    file_path = tmp_path / "random_file.txt"
    file_path.write_text("Lorem Ipsum")
    return tmp_path


# TEST SUCCESSES ARG PARSING


def test_absolute_defaults(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["main.py"])

    args_raw = gather_args_and_config_parser()
    args_clean = get_clean_arguments(args_raw)

    assert isinstance(args_clean, CleanArgs)
    assert args_clean.files_count >= 0


def test_inline_arguments(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "main.py",
            "--files_count",
            "3",
            "--clear_path",
            "--data_schema",
            '{"user":"str:rand"}',
        ],
    )

    args_raw = gather_args_and_config_parser()
    args_clean = get_clean_arguments(args_raw)

    assert args_clean.files_count == 3
    assert args_clean.clear_path is True
    assert args_clean.data_schema == {"user": "str:rand"}


def test_schema_from_file_path(monkeypatch, temp_schema_file):
    monkeypatch.setattr(
        sys, "argv", ["main.py", "--data_schema", str(temp_schema_file)]
    )

    args_raw = gather_args_and_config_parser()
    args_clean = get_clean_arguments(args_raw)

    assert "status" in args_clean.data_schema
    assert args_clean.data_schema["score"] == "int:rand(1, 100)"


def test_multiprocessing_cpu_capping(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["main.py", "--multiprocessing", "999"])

    args_raw = gather_args_and_config_parser()
    args_clean = get_clean_arguments(args_raw)

    assert args_clean.multiprocessing == (os.cpu_count() or 1)


@pytest.mark.parametrize(
    "correct_schema",
    [
        '{"age": "int:13"}',
        '{"name": "str:rand"}',
        r'{"name": "str:[\"an\",\"baa\"]"}',
        r"""{"date": "timestamp:","name": "str:rand","type": "str:['client', 'partner', 'government']","age": "int:rand(1, 90)"}""",
        '{"num": "int:[2,3]"}',
    ],
)
def test_various_correct_schemas(monkeypatch, correct_schema):
    monkeypatch.setattr(sys, "argv", ["main.py", "--data_schema", correct_schema])

    args_raw = gather_args_and_config_parser()
    args_clean = get_clean_arguments(args_raw)

    assert isinstance(args_clean, CleanArgs)


# TEST FAILURES ARG PARSING


def test_negative_files_count_raises_cli_error(monkeypatch, caplog):
    monkeypatch.setattr(sys, "argv", ["main.py", "--files_count", "-5"])

    args_raw = gather_args_and_config_parser()

    with caplog.at_level(logging.ERROR):
        with pytest.raises(SystemExit) as sample_exit:
            get_clean_arguments(args_raw)

    assert sample_exit.value.code == 1
    assert "Error: Invalid value for --files_count" in caplog.text


def test_negative_multiprocessing_raises_cli_error(monkeypatch, caplog):
    monkeypatch.setattr(sys, "argv", ["main.py", "--multiprocessing", "-5"])

    args_raw = gather_args_and_config_parser()

    with caplog.at_level(logging.ERROR):
        with pytest.raises(SystemExit) as sample_exit:
            get_clean_arguments(args_raw)

    assert sample_exit.value.code == 1
    assert "Error: Invalid value for --multiprocessing" in caplog.text


def test_negative_data_lines_raises_cli_error(monkeypatch, caplog):
    monkeypatch.setattr(sys, "argv", ["main.py", "--data_lines", "-5"])

    args_raw = gather_args_and_config_parser()

    with caplog.at_level(logging.ERROR):
        with pytest.raises(SystemExit) as sample_exit:
            get_clean_arguments(args_raw)

    assert sample_exit.value.code == 1
    assert "Error: Invalid value for --data_lines" in caplog.text


@pytest.mark.parametrize(
    "bad_schema",
    ['{"age": "int:head"}', '{"name": "str:rand(1,10)"}', '{"num": "int:[abc,3]"}'],
)
def test_corrupt_schema_syntax_errors(monkeypatch, caplog, bad_schema):
    monkeypatch.setattr(sys, "argv", ["main.py", "--data_schema", bad_schema])

    args_raw = gather_args_and_config_parser()

    with caplog.at_level(logging.ERROR):
        with pytest.raises(SystemExit) as sample_exit:
            get_clean_arguments(args_raw)

    assert sample_exit.value.code == 1
    assert "Error:" in caplog.text


# TEST COMPONENTS
@pytest.fixture
def clean_args_factory():
    def _create_args(**overrides):
        blueprint = {
            "abs_path_to_save": str(Path("./test_output").resolve()),
            "file_name": "mock_data",
            "file_prefix": "count",
            "files_count": 1,
            "data_lines": 5,
            "clear_path": False,
            "multiprocessing": 1,
            "data_schema": {"id": "str:rand"},
        }
        blueprint.update(overrides)
        return CleanArgs(**blueprint)

    return _create_args


def test_clear_path(monkeypatch, temp_output_dir):
    ###XXX: it should be changed to clean_args factory
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "main.py",
            "--clear_path",
            "--file_name",
            "mock_data",
            "--path_to_save_files",
            str(temp_output_dir),
        ],
    )

    args_raw = gather_args_and_config_parser()
    args_clean = get_clean_arguments(args_raw)

    prepare_output_directory(
        args_clean.abs_path_to_save, args_clean.file_name, args_clean.clear_path
    )

    # names from fixture probably it could be automated
    jsonl_file_path = temp_output_dir / "mock_data_2.jsonl"
    random_file_path = temp_output_dir / "random_file.txt"

    assert temp_output_dir.exists()
    assert temp_output_dir.is_dir()

    assert not jsonl_file_path.exists()
    assert random_file_path.exists()

    files_in_dir = len([item for item in temp_output_dir.iterdir() if item.is_file()])
    assert files_in_dir == 1


def test_create_list_of_output_files_paths(temp_output_dir, clean_args_factory):
    args_clean = clean_args_factory(
        abs_path_to_save=str(temp_output_dir), files_count=3
    )

    prepare_output_directory(
        args_clean.abs_path_to_save, args_clean.file_name, args_clean.clear_path
    )

    output_files_paths = create_list_of_output_files_paths(
        args_clean.abs_path_to_save,
        args_clean.file_name,
        args_clean.file_prefix,
        args_clean.files_count,
    )

    assert len(output_files_paths) == 3
    assert output_files_paths == [
        temp_output_dir / f"mock_data_{i + 1}.jsonl" for i in range(3)
    ]


def test_perform_file_generation(temp_output_dir, clean_args_factory):
    args_clean = clean_args_factory(
        abs_path_to_save=str(temp_output_dir),
        files_count=3,
        clear_path=True,
        file_name="mock_data",
        data_lines=15,
    )

    prepare_output_directory(
        args_clean.abs_path_to_save, args_clean.file_name, args_clean.clear_path
    )

    files_in_dir_before = len(
        [item for item in temp_output_dir.iterdir() if item.is_file()]
    )

    orchestrate_data_generation(clean_args=args_clean)

    jsonl_file_path = temp_output_dir / "mock_data_2.jsonl"

    assert temp_output_dir.exists()
    assert temp_output_dir.is_dir()

    assert jsonl_file_path.exists()

    files_in_dir_after = len(
        [item for item in temp_output_dir.iterdir() if item.is_file()]
    )
    assert files_in_dir_after == files_in_dir_before + 3

    with open(jsonl_file_path, "r", encoding="utf-8") as f:
        actual_lines = sum(1 for line in f)

    assert actual_lines == 15


def test_perform_file_generation_with_multiprocessing(
    temp_output_dir, clean_args_factory
):
    args_clean = clean_args_factory(
        abs_path_to_save=str(temp_output_dir),
        files_count=3,
        clear_path=True,
        file_name="mock_data",
        multiprocessing=2,
        data_lines=15,
    )

    prepare_output_directory(
        args_clean.abs_path_to_save, args_clean.file_name, args_clean.clear_path
    )

    files_in_dir_before = len(
        [item for item in temp_output_dir.iterdir() if item.is_file()]
    )

    orchestrate_data_generation(clean_args=args_clean)

    jsonl_file_path = temp_output_dir / "mock_data_2.jsonl"

    assert temp_output_dir.exists()
    assert temp_output_dir.is_dir()

    assert jsonl_file_path.exists()

    files_in_dir_after = len(
        [item for item in temp_output_dir.iterdir() if item.is_file()]
    )
    assert files_in_dir_after == files_in_dir_before + 3

    with open(jsonl_file_path, "r", encoding="utf-8") as f:
        actual_lines = sum(1 for line in f)

    assert actual_lines == 15


def test_files_count_equal_0(temp_output_dir, clean_args_factory, capsys, caplog):
    args_clean = clean_args_factory(
        abs_path_to_save=str(temp_output_dir),
        files_count=0,
        data_lines=3,
    )

    prepare_output_directory(
        args_clean.abs_path_to_save, args_clean.file_name, args_clean.clear_path
    )

    files_in_dir_before = len(
        [item for item in temp_output_dir.iterdir() if item.is_file()]
    )

    with caplog.at_level(logging.INFO):
        orchestrate_data_generation(clean_args=args_clean)

    files_in_dir_after = len(
        [item for item in temp_output_dir.iterdir() if item.is_file()]
    )

    assert files_in_dir_before == files_in_dir_after

    out, _ = capsys.readouterr()
    assert "id" in out
    assert "Successfully streamed data chunk to console." in caplog.text
