import os

def write_file(working_directory, file_path, content):
    working_directory_path = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Make sure directory path is not outside working directory
    if not target_file_path.startswith(working_directory_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    # Make file if it doesn't already exist
    if not os.path.exists(target_file_path):
        try:
            os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"

    # Make sure target file path is to a file, not a directory
    if os.path.exists(target_file_path) and os.path.isdir(target_file_path):
        return f'Error: "{file_path}" is a directory, not a file'

    # Write to file
    try:
        with open(target_file_path, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: writing to file: {e}"
