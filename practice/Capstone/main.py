import argparse
import configparser
import json
import logging
import os
import random
import re
import time
import uuid
from uuid import uuid4
import sys
import multiprocessing
from functools import partial
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Any, Callable, NamedTuple


class Args(NamedTuple):
    path_to_save_files: str
    files_count: int
    file_prefix: str
    file_name: str
    data_lines: int
    multiprocessing: int
    data_schema: str
    clear_path: bool

    def check_values(self):
        if self.files_count > 1 and not self.file_prefix:
            raise ValueError('If files_count > 1, then file_prefix argument needs to be provided.')
        if self.data_lines < 1:
            raise ValueError("Number of data lines must be at least 1")
        if self.multiprocessing < 1:
            raise ValueError("Number of processes must be at least 1")
        if self.files_count < 0:
            raise ValueError('Number of files cannot be negative.')
        return


def return_timestamp_fun(value: str) -> Callable:
    if value == '':
        return time.time
    logger.warning('Timestamp does not support any values.')
    return time.time


def return_int_fun(value: str) -> Any:
    if value == 'rand':
        return lambda: random.randint(0, 100000)
    elif value.startswith('[') and value.endswith(']'):
        values_to_choose = value.strip('[]').split(',')
        for number, item in enumerate(values_to_choose):
            values_to_choose[number] = item.replace('\'', '').replace('\"', '').strip()
        return lambda: random.choice(values_to_choose)
    elif re.search(r'^rand\(\d+, \d+\)$', value):
        lst = re.findall(r'\d+', value)
        a, b = int(lst[0]), int(lst[1])
        return lambda: random.randint(a, b)
    elif value == '':
        return lambda: None
    else:
        try:
            value = int(value)
        except ValueError:
            logger.error(f'Wrong type of data, {value} cannot be converted to int')
            sys.exit(1)
        return lambda: value


def return_str_fun(value: str) -> Any:
    if value == 'rand':
        return lambda: str(uuid4())
    elif value.startswith('[') and value.endswith(']'):
        values_to_choose = value.strip('[]').split(',')
        for number, item in enumerate(values_to_choose):
            values_to_choose[number] = item.replace('\'', '').replace('\"', '').strip()
        return lambda: random.choice(values_to_choose)
    elif re.search(r'^rand\(\d+, \d+\)$', value):
        logger.error('Wrong type of data')
        sys.exit(1)
    elif value == '':
        return lambda: ''
    else:
        return lambda: value


logging.basicConfig(level='INFO', format='[%(levelname)s] %(process)d %(filename)s -- %(message)s')
logger = logging.getLogger('Console app')
GENERATORS = {'timestamp': return_timestamp_fun, 'int': return_int_fun, 'str': return_str_fun}


def parse_args(config, default_name='default values') -> Args:
    args = argparse.ArgumentParser(prog='Console app', description='Some description')
    args.add_argument('--path_to_save_files',
                      help='Where all files need to save; can be defined relatively or absolutely.',
                      type=str,
                      default=config.get(default_name, 'path_to_save_files'))
    args.add_argument('--files_count',
                      help='How much json files to generate; if < 0 then error, if = 0 then output in console',
                      type=int,
                      default=config.get(default_name, 'files_count'))
    args.add_argument('--file_name',
                      help='Base file_name. If there is no prefix, the final file name will be file_name.json.'
                           'With prefix full file name will be file_name_file_prefix.json',
                      type=str,
                      default=config.get(default_name, 'file_name'))
    args.add_argument('--file_prefix',
                      help='What prefix for file name to use if more than 1 file needs to be generated',
                      choices=['count', 'random', 'uuid']
                      )
    args.add_argument('--data_schema',
                      help='It’s a string with json schema.It could be loaded in two ways:'
                           ' with path to json file with schema or with schema entered to command line.',
                      default=config.get(default_name, 'data_schema'))
    args.add_argument('--data_lines',
                      help='Count of lines for each file',
                      type=int,
                      default=config.get(default_name, 'data_lines'))
    args.add_argument('--clear_path',
                      help='If this flag is on, before the script starts creating new data files,'
                           ' all files in path_to_save_files that match file_name will be deleted.',
                      action='store_true')
    args.add_argument('--multiprocessing',
                      help='The number of processes used to create files.'
                           'Divides the “files_count” value equally and starts N processes to create an equal'
                           'number of files in parallel.',
                      type=int,
                      default=config.get(default_name, 'multiprocessing'))
    return Args(**vars(args.parse_args()))


def create_pattern_on_based_schema(data_schema: dict) -> dict:
    data_structure = dict()
    for key, value in data_schema.items():
        try:
            left, right = value.split(':', 2)
        except ValueError:
            logger.error('Wrong type of data. All values should support special notation “type:what_to_generate”.')
            sys.exit(1)
        gen = GENERATORS.get(left)
        if gen is None:
            logger.error('Wrong type of data')
            sys.exit(1)
        else:
            data_structure[key] = gen(right)
    return data_structure


def check_path(path: str) -> bool:
    if os.getcwd() in os.path.abspath(path):
        return True
    return False


def create_prefixes(number_of_prefixes: int, prefix: str) -> list:
    if prefix == 'count':
        return [str(i) for i in range(number_of_prefixes)]
    elif prefix == 'random':
        return random.sample(range(100000), number_of_prefixes)
    elif prefix == 'uuid':
        return [str(uuid.uuid4()) for _ in range(number_of_prefixes)]
    else:
        logger.error('Prefixes can only have value within [\'count\', \'random\', \'uuid\']')
        sys.exit(1)


def single_data_creator(data_pattern: dict) -> dict:
    return {key: value() for key, value in data_pattern.items()}


def data_creator(data_schema: dict, number_of_lines: int) -> List[Dict]:
    data_pattern = create_pattern_on_based_schema(data_schema)
    return [single_data_creator(data_pattern) for _ in range(number_of_lines)]


def dump_data_to_json(path: str, data) -> None:
    with open(path + '.jsonl', 'a') as f:
        for record in data:
            f.write(json.dumps(record))
            f.write('\n')


def get_data_schema(args: Args) -> dict:
    try:
        data_schema = json.loads(args.data_schema)
    except json.decoder.JSONDecodeError:
        try:
            with open(args.data_schema, 'r') as f:
                data_schema = json.load(f)
        except FileNotFoundError:
            logger.error(f'Path {args.data_schema} is not correct')
            sys.exit(1)
    return data_schema


def clear_path(path_to_save_files: str, file_name: str) -> None:
    [os.remove(path_to_save_files + '/' + file) for file in os.listdir(path_to_save_files) if
     file.startswith(file_name)]


def output_manager(args: Args) -> None:
    data_schema = get_data_schema(args)
    if args.files_count == 0:
        logger.info('Creating data...')
        data = data_creator(data_schema, args.data_lines)
        logger.info('Printing output...')
        [print(json.dumps(data[i])) for i in range(len(data))]
    else:
        if not check_path(args.path_to_save_files):
            logger.error('Path need to be in directory.')
            sys.exit(1)
        if not os.path.exists(args.path_to_save_files):
            logger.info('Creating output directory...')
            os.makedirs(args.path_to_save_files)
        if args.clear_path:
            logger.info('Clearing path...')
            clear_path(args.path_to_save_files, args.file_name)
        logger.info('Creating data...')
        with multiprocessing.Pool(processes=min(os.cpu_count(), args.multiprocessing)) as pool:
            data = pool.starmap(partial(data_creator, data_schema=data_schema, number_of_lines=args.data_lines),
                                [() for _ in range(args.files_count)])
        if args.file_prefix:
            prefixes = create_prefixes(args.files_count, args.file_prefix)
            paths = [args.path_to_save_files + '/' + args.file_name + '_' + prefix
                     for prefix in prefixes]
            logger.info('Creating files with data...')
            with ThreadPoolExecutor(max_workers=min(os.cpu_count() + 4, 32)) as executor:
                executor.map(dump_data_to_json, paths, data)
        else:
            logger.info('Creating file with data...')
            path = args.path_to_save_files + '/' + args.file_name
            dump_data_to_json(path, data[0])
    logger.info('Everything was successful, exiting...')


def main():
    config = configparser.ConfigParser()
    config.read('default.ini')
    args = parse_args(config)
    try:
        args.check_values()
    except ValueError as exception:
        logger.error(exception)
        sys.exit(1)
    output_manager(args)


if __name__ == '__main__':
    main()
