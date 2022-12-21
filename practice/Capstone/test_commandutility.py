import pytest
from main import *
import tempfile
from unittest.mock import Mock
import shutil
import re


config = configparser.ConfigParser()
config.read('test.ini')
correct_schemas = [config[section_name]['data_schema'] for section_name in config.sections()
                   if 'correct' in section_name]
correct_paths = ['.', './', os.path.join(os.getcwd(), 'output'), './output']
incorrect_paths = ['/Users', '/']
possible_str_values = ['rand', "['some1', 'some2', 'some3']", 'cat', '']
possible_int_values = ['rand', 'rand(35, 40)', '']

"""
For some reason test_parse_args works only when we invoke pytest in terminal. Perhaps there is some issue with passing
file name to argparse.argumentparser (which is done by default if params are not provided) and I have no idea how to fix
this. 
"""


def create_args():
    args = Mock()
    args.path_to_save_files = './test_output'
    args.files_count = 5
    args.file_prefix = 'count'
    args.file_name = 'super_cool_test_name'
    args.data_lines = 500
    args.multiprocessing = 1
    args.data_schema = json.dumps(
        {"date": "timestamp:", "some_int": "int:rand", "type": "int:[1, 2, 3]", "age": "int:rand(1, 90)",
         "some_str": "str:rand"})
    return args


def test_return_str_fun():
    data = [return_str_func(value)() for value in possible_str_values]
    regex = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}$", re.I)
    assert bool(regex.match(data[0])) is True
    assert data[1] in ['some1', 'some2', 'some3']
    assert data[2] == "cat"
    assert data[3] == ''


def test_return_int_fun():
    data = [return_int_func(value)() for value in possible_int_values]
    assert data[0] in range(100000)
    assert data[1] in range(35, 41)
    assert data[2] is None


@pytest.mark.parametrize('data_schema', correct_schemas)
def test_create_pattern_on_based_data(data_schema):
    data_schema = json.loads(data_schema)
    assert len(create_pattern_on_based_schema(data_schema)) == len(data_schema)


@pytest.mark.parametrize('incorrect', incorrect_paths)
@pytest.mark.parametrize('correct', correct_paths)
def test_check_path(correct, incorrect):
    assert check_path(correct) is True
    assert check_path(incorrect) is False


@pytest.mark.parametrize('number', [random.randint(1, 10) for _ in range(3)])
def test_create_count_prefixes(number):
    created_prefixes = create_prefixes(number, 'count')
    assert len(created_prefixes) == number
    for number, item in enumerate(created_prefixes):
        assert int(item) == number


@pytest.mark.parametrize('number', [random.randint(1, 10) for _ in range(3)])
def test_create_random_prefixes(number):
    created_prefixes = create_prefixes(number, 'random')
    assert len(created_prefixes) == number
    for item in created_prefixes:
        assert 0 < int(item) < 99999


@pytest.mark.parametrize('number', [random.randint(1, 10) for _ in range(3)])
def test_create_uuid_prefixes(number):
    created_prefixes = create_prefixes(number, 'uuid')
    assert len(created_prefixes) == number
    for item in created_prefixes:
        regex = re.compile("^[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}$", re.I)
        assert bool(regex.match(item)) is True


@pytest.fixture
def fake_file_with_json():
    file = tempfile.NamedTemporaryFile(delete=False)
    json_data = json.loads(
        '{"date": "timestamp:","some_int": "int:rand","type": "int:[1, 2, 3]","age": "int:rand(1, 90)"}')
    with open(file.name, 'w') as file:
        file.write(json.dumps(json_data))
    return file


def test_get_data_schema(fake_file_with_json):
    mock = Mock()
    mock.data_schema = fake_file_with_json.name
    data_schema = get_data_schema(mock)
    with open(fake_file_with_json.name, 'r') as file:
        data_from_file = json.load(file)
        assert data_schema == data_from_file
    os.remove(file.name)


@pytest.fixture
def fake_directory():
    return tempfile.mkdtemp()


def test_clear_path(fake_directory):
    file = tempfile.NamedTemporaryFile(dir=fake_directory)
    assert len(os.listdir(fake_directory)) == 1
    file_name = file.name[len(fake_directory) + 1::]
    clear_path(fake_directory, file_name)
    assert os.listdir(fake_directory) == []
    shutil.rmtree(fake_directory)


@pytest.mark.parametrize('number_of_processes', list(range(1, os.cpu_count() + 1)))
def test_output_manager(number_of_processes):
    args = create_args()
    if os.path.exists(args.path_to_save_files):
        shutil.rmtree(args.path_to_save_files)
    output_manager(args)
    assert len(os.listdir(args.path_to_save_files)) == args.files_count
    shutil.rmtree(args.path_to_save_files)
