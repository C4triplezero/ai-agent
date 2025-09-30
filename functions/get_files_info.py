import os

def get_files_info(working_directory, directory="."):

    try:
        working_directory_path = os.path.abspath(working_directory)
    except:
        return f'Error: "{working_directory}" is not a valid working directory'
    if not directory in os.listdir(working_directory_path) and not directory == ".":
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    directory_path = os.path.join(working_directory_path, directory)
    if not os.path.isdir(directory_path):
        return f'Error: "{directory}" is not a directory'

    try:
        return_strings = []
        for file in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file)
            return_strings.append(f'- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}')
        return "\n".join(return_strings)
    except Exception as e:
        return f"Error listing files: {e}"
