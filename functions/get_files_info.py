import os

def get_files_info(working_directory, directory="."):
    working_directory_path = os.path.abspath(working_directory)
    target_directory_path = os.path.abspath(os.path.join(working_directory, directory))

    # Make sure directory path is not outside working directory
    if not target_directory_path.startswith(working_directory_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # Make sure directory path is a directory
    if not os.path.isdir(target_directory_path):
        return f'Error: "{directory}" is not a directory'

    try:
        # Create a string that represents the contents of the directory
        files_info = []

        for file_name in os.listdir(target_directory_path):
            file_path = os.path.join(target_directory_path, file_name)
            is_dir = os.path.isdir(file_path)
            file_size = os.path.getsize(file_path)
            files_info.append(f"- {file_name}: file_size={file_size} bytes, is_dir={is_dir}")

        return str.join("\n", files_info)

    except Exception as e:
        return f'Error listing files: {e}'

