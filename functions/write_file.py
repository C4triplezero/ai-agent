import os

def write_file(working_directory, file_path, content):
    working_directory_abs = os.path.abspath(working_directory)
    file_path_abs = os.path.abspath(os.path.join(working_directory, file_path))
    if not file_path_abs.startswith(working_directory_abs):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(file_path_abs):
        try:
            os.makedirs(file_path_abs.rsplit("/", 1)[0], exist_ok=True)
        except Exception as e:
            return f'Error: creating "{file_path}": {e}'
    else:
        if not os.path.isfile(file_path_abs):
            return f'Error: Cannot write to "{file_path}" as it is a not a file'

    try:  
        with open(file_path_abs, "w") as f:
            f.write(content)
    except Exception as e:
        return f'Error: writing to "{file_path}": {e}'
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
