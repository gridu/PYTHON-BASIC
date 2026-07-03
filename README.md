# Python-Basics Course Tasks

This repository contains exercises for the [GridU Python Basic course](https://gridu.litmos.com/course/6897870).

- **`practice/`** — weekly module tasks (m1–m7)
- **`capstone/`** — final Console Data Generator project

Both parts share the same dependencies and the same virtual environment. Set up the environment once at the repository root, then run practice scripts, capstone commands, and tests from there.

## Prerequisites

- **Python 3.11+** (see `pyproject.toml`)
- `git`

## Project structure

```
PYTHON-BASIC/
├── practice/          # Course exercises by module
│   ├── m1_python_part_1/
│   ├── m2_python_part_2/
│   ├── m3_python_testing/
│   ├── m4_python_part_3/
│   ├── m5_additional_topics/
│   ├── m6_web_scraping/
│   └── m7_concurrency/
├── capstone/          # Capstone project (data generator CLI)
├── requirements.txt   # Shared dependencies for practice and capstone
├── pyproject.toml     # Ruff configuration
└── pytest.ini         # Pytest configuration
```

Some modules include their own `README.md` with task-specific instructions (for example `practice/m6_web_scraping/` or `practice/m5_additional_topics/parsing_serialization_task/`).

---

## Virtual environment setup

Use **one** virtual environment at the repository root for both `practice/` and `capstone/`.

### 1. Clone and enter the repository

```bash
git clone <repository-url>
cd PYTHON-BASIC
```

### 2. Create a virtual environment

**macOS / Linux:**

```bash
python3 -m venv .venv
```

**Windows (Command Prompt):**

```cmd
python -m venv .venv
```

**Windows (PowerShell):**

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows (Command Prompt):**

```cmd
.venv\Scripts\activate.bat
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

Your shell prompt should show `(.venv)` when the environment is active.

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. (Optional) Install pre-commit hooks

```bash
pre-commit install
```

This runs Ruff and basic file checks automatically before each commit.

### Deactivate the virtual environment

```bash
deactivate
```

---

## Running commands

**Always run commands from the repository root** with the virtual environment activated.

### Practice tasks

Most early tasks are standalone scripts:

```bash
python practice/m1_python_part_1/task1.py
python practice/m2_python_part_2/task_classes.py
```

Tasks that import other project modules must be run as packages:

```bash
python -m practice.m6_web_scraping.main
python -m practice.m6_web_scraping.standalone_api
python -m practice.m5_additional_topics.parsing_serialization_task.task_json
```

Concurrency templates:

```bash
python -m practice.m7_concurrency.task1_fibonacci.template
python -m practice.m7_concurrency.task2_apod_api.template
```

#### Module-specific notes

| Module | Notes |
|--------|-------|
| `m5_additional_topics/parsing_serialization_task` | See [module README](practice/m5_additional_topics/parsing_serialization_task/README.md). Validate XML with `python practice/m5_additional_topics/parsing_serialization_task/tests/validate_xml.py`. |
| `m6_web_scraping` | Requires network access. See [module README](practice/m6_web_scraping/README.md). |
| `m7_concurrency/task2_apod_api` | Requires a [NASA API key](https://api.nasa.gov/). Store it with keyring: `keyring set nasa_concurrent_task NASA_API_KEY`. |

### Capstone

Run the Console Data Generator CLI:

```bash
python -m capstone.main
```

Show available options and defaults:

```bash
python -m capstone.main --help
```

Example with custom arguments:

```bash
python -m capstone.main \
  --path_to_save_files ./capstone/output \
  --files_count 2 \
  --file_name export \
  --data_lines 5
```

Default values are loaded from `capstone/default.ini`. Generated files are written to `capstone/output/` by default.

---

## Running tests

Tests use [pytest](https://docs.pytest.org/). Run them from the repository root with the virtual environment activated.

### All tests

```bash
pytest
```

or:

```bash
python -m pytest
```

### Practice tests only

```bash
pytest practice/
```

Practice tests live mainly in `practice/m3_python_testing/` and `practice/m6_web_scraping/test_scraper.py`.

### Capstone tests only

```bash
pytest capstone/
```

### Single file or test

```bash
pytest practice/m3_python_testing/test_task_classes.py
pytest capstone/test_app.py
pytest practice/m3_python_testing/test_task_parametrize.py::test_fibonacci_2
pytest practice/m3_python_testing/test_task_classes.py::TestTeacher::test_init
```

### Useful pytest options

```bash
pytest -v          # verbose output
pytest -q          # quiet output
pytest -x          # stop on first failure
pytest --collect-only   # list tests without running them
```

### Running tests for a specific task

Not every module has automated tests. Use the table below to run tests for the task you are working on.

| Module | Task / topic | What to run |
|--------|----------------|-------------|
| **m1** | `task1`–`task6` | No automated tests — run scripts manually, e.g. `python practice/m1_python_part_1/task1.py` |
| **m2** | `task_read_write` | `pytest practice/m3_python_testing/test_read_write.py` |
| **m2** | `task_read_write_2` | `pytest practice/m3_python_testing/test_read_write_2.py` |
| **m2** | `task_exceptions` | `pytest practice/m3_python_testing/test_task_exceptions.py` |
| **m2** | `task_input_output` | `pytest practice/m3_python_testing/test_task_input_output.py` |
| **m2** | `task_classes` | `pytest practice/m3_python_testing/test_task_classes.py` |
| **m3** | All testing exercises | `pytest practice/m3_python_testing/` |
| **m3** | Parametrize (`test_task_parametrize`) | `pytest practice/m3_python_testing/test_task_parametrize.py` |
| **m4** | `task_1` | `pytest practice/m4_python_part_3/task_1.py` |
| **m4** | `task_2` | `pytest practice/m4_python_part_3/task_2.py` |
| **m4** | `task_3` | `pytest practice/m4_python_part_3/task_3.py` |
| **m4** | `task_4` | `pytest practice/m4_python_part_3/task_4.py` |
| **m4** | `task_5` | `pytest practice/m4_python_part_3/task_5.py` |
| **m4** | All m4 tasks | `pytest practice/m4_python_part_3/` |
| **m5** | XML parsing (`parsing_serialization_task`) | `python practice/m5_additional_topics/parsing_serialization_task/tests/validate_xml.py` |
| **m6** | Web scraping | `pytest practice/m6_web_scraping/test_scraper.py` |
| **m7** | Fibonacci / APOD API | No automated tests — run templates manually (see [Running commands](#running-commands)) |
| **capstone** | Console Data Generator | `pytest capstone/test_app.py` |

**Examples — run one test inside a file:**

```bash
# Single test function
pytest practice/m3_python_testing/test_task_exceptions.py::test_division_by_zero

# Single test method in a test class
pytest practice/m3_python_testing/test_task_classes.py::TestStudent::test_is_active_before_dealine

# Single parametrized case (by index)
pytest practice/m3_python_testing/test_task_parametrize.py::test_fibonacci_2[3]

# Single capstone test
pytest capstone/test_app.py::test_inline_arguments
```

**Note:** m2 tasks are tested via files in `practice/m3_python_testing/` — that module contains the tests you write (or run) for m2 homework.

---
