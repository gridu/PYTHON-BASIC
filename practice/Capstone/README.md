This app is a console utility to generate test data based on provided schema. 

Arguments available in app:

--path_to_save_files, help: Where all files need to save; can be defined relatively or absolutely,
                            uploaded from default.ini file if not provided.

--files_count, help: How much json files to generate; if < 0 then error, if = 0 then output in console,
                     uploaded from default.ini file if not provided.

--file_name, help: Base file_name. If there is no prefix, uploaded from default.ini file if not provided.

--file_prefix, help: What prefix for file name to use if more than 1 file needs to be generated',
                     possible choices: ['count', 'random', 'uuid']. 

--data_schema, help: It’s a string with json schema. It could be loaded in two ways: with path to json file with schema
                     or with schema entered to command line. Uploaded from default.ini file if not provided.

--data_lines, help: Count of lines for each file, uploaded from default.ini file if not provided.

--clear_path, help: If this flag is on, before the script starts creating new data files,
                    all files in path_to_save_files that match file_name will be deleted.

--multiprocessing, help: The number of processes used to create files. Divides the “files_count” value equally and starts N processes
                         to create an equal number of files in parallel.

All arguments can be set up from console. Some of them are provided with default values (as mentioned in help). 
Data schema should support special notation: 'type:what_to_generate', where type is one of \['str', 'int, 'timestamp'\]
If type == 'str' then possible what_to_generate values are: 'rand', \['str1', 'str2', ... \], 'some_str', ''.
If type == 'int' then possible what_to_generate_values are: 'rand', 'rand(a, b)', '', where of course a and b are some integers.
If type == 'timestamp' then what_to_generate value should be empty (if provided then it will be ignored). 

