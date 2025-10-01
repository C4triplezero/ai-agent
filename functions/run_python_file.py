import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    working_directory_abs = os.path.abspath(working_directory)
    file_path_abs = os.path.abspath(os.path.join(working_directory, file_path))
    if not file_path_abs.startswith(working_directory_abs):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(file_path_abs):
        return f'Error: File "{file_path}" not found.'
    if not file_path_abs.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        cmd = ["uv", "run", file_path_abs] + args
        result = subprocess.run(cmd, cwd=working_directory_abs, timeout=30, capture_output=True, text=True)
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f'Error: Running file "{file_path}": {e}'