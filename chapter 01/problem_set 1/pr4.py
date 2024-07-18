import os

def list_directory_contents(path):
    try:
        # Get the list of files and directories
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")
    except PermissionError:
        print(f"Permission denied to access {path}.")

# Specify the path to the directory
directory_path = "/"

# Call the function to list the contents
list_directory_contents(directory_path)
