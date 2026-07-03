PATH_SAVE_HELP = """\
Target directory where all generated files will be stored.
Accepts two path formats:
  1. Relative: Formatted from the Current Working Directory (CWD)
               Example: './generated'
  2. Absolute: Full system path
               Example: '/var/log/generator' or 'C:\\Data\\Output'"""

FILES_COUNT_HELP = """\
The number of JSON files to generate.
Rules:
  * Count > 0  : Generates the specified number of files.
  * Count == 0 : Disables file writing; outputs all data directly to the console.
  * Count < 0  : Invalid input. Will throw an error and terminate execution."""

FILE_NAME_HELP = """\
The base name for the generated JSON files.
  * Without prefix: Saves directly as '[file_name].json'
  * With prefix   : Saves as '[file_name]_[file_prefix].json'"""

FILE_PREFIX_HELP = """\
The naming modifier applied when more than 1 file is being generated.
Must be chosen from the following explicit set:
  * count  : Appends an incrementing index (e.g., base_1.json, base_2.json)
  * random : Appends a random modifier
  * uuid   : Appends a completely unique UUID string identifier"""

SCHEMA_HELP = """
DATA SCHEMA FORMAT GUIDE
================================================================================
Your schema must be a valid JSON object. Every key defined in the schema will
map exactly to a key in the generated output lines.

Format pattern: "key": "type:instruction"
Allowed types:  timestamp, str, int (any other type will cause an error)

--------------------------------------------------------------------------------
THE 5 GENERATION RULES
--------------------------------------------------------------------------------

1. Reserved 'rand' Keyword
   Generates completely random data based on the data type.
   * If type is 'str'       -> Generates a unique UUIDv4 string.
   * If type is 'int'       -> Generates a random integer between 0 and 10,000.
   * Example: "uuid_id": "str:rand"

2. Value Lists [val1, val2, ...]
   Picks a random item from the provided list for each line.
   * Example: "status": "str:['client', 'partner', 'government']"
   * Example: "multiplier": "int:[1, 5, 10]"

3. Integer Ranges: rand(from, to)
   Generates a random integer between the specified inclusive bounds.
   * CRITICAL: This is only compatible with the 'int' type.
   * Example: "age": "int:rand(1, 90)"

4. Standalone/Static Values
   Hardcodes a specific value that will repeat on every single line.
   * CRITICAL: The value must match the declared type. (e.g., "int:head" is
     invalid and will throw an error because 'head' cannot become an integer).
   * Example: "species": "str:cat" (Outputs "cat" every time)
   * Example: "code": "int:200"     (Outputs 200 every time)

5. Empty Values
   Leaving the instruction blank after the colon is allowed.
   * If type is 'str'       -> Outputs an empty string ""
   * If type is 'int'       -> Outputs null (None)
   * Example: "middle_name": "str:"
   * Example: "optional_id": "int:"

================================================================================
COMPLETE VALID SCHEMA EXAMPLE:
================================================================================
{
  "date": "timestamp:",
  "name": "str:rand",
  "type": "str:['client', 'partner', 'government']",
  "age": "int:rand(1, 90)"
}
================================================================================
"""

DATA_LINES_HELP = """\
The number of data rows/event lines to generate inside each JSON file.
Must be a positive integer greater than 0."""

CLEAR_PATH_HELP = """\
[FLAG] Safety purge toggle.
If this flag is provided, the utility will automatically delete all existing
files in 'path_to_save_files' that match your 'file_name' BEFORE creating
the new ones. Use with caution!"""

MULTIPROCESSING_HELP = """\
The number of concurrent CPU worker processes used to generate the files.
Rules:
  * N > 0              : Spawns N parallel worker processes.
  * N > os.cpu_count() : Overrides and caps the value to your system's maximum
                         available CPU cores to prevent system instability.
  * N < 0              : Invalid input. Will throw an error and terminate."""
