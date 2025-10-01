import os
from config import MAX_CHARACTERS as max_char

def get_file_content(working_directory, file_path):
    working_directory_path = os.path.abspath(working_directory)
    file_path_abs = os.path.abspath(os.path.join(working_directory, file_path))
    if not file_path_abs.startswith(working_directory_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_path_abs):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(file_path_abs, "r") as f:
            contents = f.read(max_char)
    except Exception as e:
        return f'Error: Reading file "{file_path}": {e}'
    if len(contents) == max_char:
        contents += f'[...File "{file_path}" truncated at {max_char} characters]'
    
    return contents
