import os

# Specify the directory you wantto list
directory = '/New Folder'

   # Lists all the files and directories in the specified directory
contents = os.listdir(directory)

   # Print each file and directory name
for item in contents:
    print(item)