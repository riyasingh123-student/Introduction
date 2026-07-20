import os

#Select the directory whose contents you want to list
directory = '/'

#Use the os module to list the directory content
contents = os.listdir(directory)

#Print the contents for the directory
print(contents)