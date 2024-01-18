import argparse, logging, os, json, multiprocessing
import configparser
import uuid
import random
import regex as re
import time
import string

list_pattern = re.compile(r'^\[(.*)]$')
rand_pattern = re.compile(r'rand\((\d+), (\d+)\)')


def delete_directory(directory_path: str):
    try:
        # Remove files in the directory
        for root, dirs, files in os.walk(directory_path, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)

            for dr in dirs:
                dir_path = os.path.join(root, dr)
                os.rmdir(dir_path)

        # Remove the top-level directory
        os.rmdir(directory_path)
    except Exception as e:
        logging.error(f'Error deleting directory {directory_path}: {e}')
        exit(1)


def clear_existing_files(directory_path: str):
    delete_directory(directory_path)
    logging.info(f'`{directory_path}` folder is cleaned up')
    os.makedirs(directory_path)


parsing_schema_err = "Parsing schema error: {t}:{tv} can`t be used for {t} type"
parsing_schema_warning = "Parsing schema warning: {t} does not support any values. {tv} will be ignored"


def parse_str(t: str, tv: str):
    if tv == 'rand':
        return 'str(uuid.uuid4())'
    elif list_pattern.match(tv):
        return f'random.choice(list_pattern.findall("{tv}")[0].split(",")).strip()'
    elif rand_pattern.match(tv):
        logging.error(parsing_schema_err.format(t=t, tv=tv))
        exit(1)
    else:
        return f'str("{tv}")'


def parse_int(t: str, tv: str):
    if tv == '':
        return 'None'
    elif tv == 'rand':
        return 'random.randint(0, 10000)'
    elif list_pattern.match(tv):
        return f'int(random.choice(list_pattern.findall("{tv}")[0].split(",")))'
    elif rand_pattern.match(tv):
        return f'random.randint(int(rand_pattern.findall("{tv}")[0][0]), int(rand_pattern.findall("{tv}")[0][1]))'
    elif tv.isdigit():
        return f'int({tv})'
    else:
        logging.error(parsing_schema_err.format(t=t, tv=tv))
        exit(1)


def parse_timestamp(t: str, tv: str):
    if rand_pattern.match(tv):
        logging.error(parsing_schema_err.format(t=t, tv=tv))
        exit(1)
    elif tv > '':
        logging.warning(parsing_schema_warning.format(t=t, tv=tv))
    return 'time.time()'


parsers = {'str': parse_str, 'int': parse_int, 'timestamp': parse_timestamp}


def parse_data_schema(data_schema: dict):
    schema = {}

    for key, ktype in data_schema.items():
        schema[key] = {}
        # print(key, ktype)
        if len(ktype.split(':')) == 1:
            logging.error("Parsing schema error: Right part of value must be provided!")
            exit(1)
        t = ktype.split(':')[0].strip()
        tv = ktype.split(':')[1].strip()

        if t in parsers:
            schema[key] = parsers[t](t, tv)
        else:
            logging.error(f'Parsing schema error: {t} is out of schema types scope')
            exit(1)

    return schema


def generate_data(schema):
    res = {}
    for d, g in schema.items():
        res[d] = eval(g)
    return res


def load_defaults_from_config():
    config = configparser.ConfigParser()
    config.read('default.ini')
    defaults = dict(config['DEFAULT'])
    return defaults


def save(data: json, path_to_save_files: str, file_name: str, file_prefix: str):
    file_prefix = f'_{file_prefix}' if file_prefix > '' else ''
    file_name = file_name.replace('.json', '')
    with open(os.path.join(path_to_save_files, f'{file_name}{file_prefix}.json'), 'w') as file:
        json.dump(data, file, indent=4)


def get_file_prefix(file_prefix, i):
    if file_prefix == 'uuid':
        return str(uuid.uuid4())
    elif file_prefix == 'count':
        return str(i)
    elif file_prefix == 'random':
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    else:
        logging.error("file_prefix must me one of ['count', 'random', 'uuid']")
        exit(1)


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    defaults = load_defaults_from_config()

    parser = argparse.ArgumentParser(prog='magicgenerator',
                                     description='Utility for generating test data based on the provided data schema',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--path_to_save_files', required=True,
                        help='Where all files need to save (Relative or absolute path). `.` - means current path.')
    parser.add_argument('--files_count', type=int, default=defaults.get('files_count'),
                        help='How much JSON files will be generated. 0 will print output to console. 1 is Default '
                             'value.')
    parser.add_argument('--file_name', required=True,
                        help='Base file_name. If there is no prefix, the final file name will be `<file_name>.json`. '
                             'With prefix full file name will be `<file_name>_<file_prefix>.json`')
    parser.add_argument('--file_prefix', choices=['count', 'random', 'uuid'],
                        default=defaults.get('file_prefix', 'uuid'),
                        help='What prefix for file name to use if more than 1 file needs to be generated')
    parser.add_argument('--data_schema', required=True, type=str,
                        help='String with json schema. It could be 1) Path to json file with schema or '
                             '2) Schema entered to command line.')
    parser.add_argument('--data_lines', type=int, default=defaults.get('data_lines', 1000),
                        help='Count of lines for each file.')
    parser.add_argument('--clear_path', action='store_true',
                        help='Delete existing files with the same name in the path.')
    parser.add_argument('--multiprocessing', type=int, default=defaults.get('multiprocessing', 1),
                        help='Number of processes used to create files.')

    args = parser.parse_args()

    if not os.path.exists(args.path_to_save_files):
        os.makedirs(args.path_to_save_files)
    elif not os.path.isdir(args.path_to_save_files):
        logging.error('Provided path is not a directory. Please provide a valid directory path.')
        exit(1)

    if args.clear_path:
        clear_existing_files(args.path_to_save_files)

    if args.files_count < 0:
        logging.error('Files count cannot be negative.')
        exit(1)

    if args.multiprocessing < 0:
        logging.error('Multiprocessing value cannot be negative.')
        exit(1)
    elif args.multiprocessing > os.cpu_count():
        args.multiprocessing = os.cpu_count()
        logging.info(f'multiprocessing arg set greater than  cpu count. Corrected value is {args.multiprocessing}')

    if os.path.exists(args.data_schema):
        with open(args.data_schema, 'r') as schema_file:
            data_schema = json.load(schema_file)
    elif args.data_schema:
        data_schema = json.loads(args.data_schema)
    else:
        logging.error('Please provide either a data schema or a path to a schema file.')
        exit(1)

    logging.info('Schema parsing...')
    schema = parse_data_schema(data_schema)
    logging.info('Schema parsing completed.')

    logging.info('Starting data generation...')
    with multiprocessing.Pool(args.multiprocessing) as pool:
        res = [pool.map(generate_data,
                        [schema for _ in range(args.data_lines)])
               for _ in range(1 if args.files_count == 0 else args.files_count)]
    logging.info('Data generation complete.')

    if args.files_count == 0:
        logging.info('Printing results to console...')
        for r in res[0]:
            logging.info(r)
        logging.info('Printing results completed.')
    else:
        logging.info(f'Saving results to {args.files_count} files...')
        with multiprocessing.Pool(args.multiprocessing) as pool:
            pool.starmap(save, [(res[i],
                                 args.path_to_save_files,
                                 args.file_name,
                                 get_file_prefix(args.file_prefix, i)) for i in range(len(res))])


if __name__ == '__main__':
    main()