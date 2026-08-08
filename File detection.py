# SIMPLE FILE DETECTION IN PYTHON

import os

file_path = 'test.txt'

if os.path.exists(file_path):
    print(f"The file {file_path} exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")

else:
    print(f"The file {file_path} does not exist")