"""Gets the requirements files from data file"""
import os

def get_requirements_files():
    """Gets the requirements files from data file"""
    requirements_files = os.listdir("requirements")
    print(requirements_files)
    return requirements_files


def get_file(file_name):
    """Gets the file contents from the file name"""
    return open("requirements/" + file_name)
