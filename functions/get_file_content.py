import os

def get_file_content(working_directory, file_path):
    working_directory_path = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Make sure directory path is not outside working directory
    if not target_file_path.startswith(working_directory_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # Make sure directory path is a directory
    if not os.path.isfile(target_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        MAX_CHARS = 10000

        with open(target_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) == MAX_CHARS:
                file_content_string += '\n...File "{file_path}" truncated at 10000 characters'
            return file_content_string

    except Exception as e:
        return f'Error reading files: {e}'

