"""Gets the requirements files from data file"""
import os

def get_requirements_files():
    """Gets the requirements files from data file"""
    file_path = os.path.dirname(os.path.realpath(__file__))
    requirements_files = os.listdir(file_path + "/requirements")
    print(requirements_files)
    return requirements_files


def get_file(group):
    """Gets the file contents from the file name"""
    file_path = os.path.dirname(os.path.realpath(__file__))
    return open(file_path + "/requirements/bounswe.bounswe2023group" + str(group) + ".md", "r", encoding="utf-8")
