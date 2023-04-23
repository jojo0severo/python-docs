import os


print("This is the name of the script: ", os.path.basename(__file__))
print("This is the name of the OS: ", os.name)
print("This is the current working directory: ", os.getcwd())
print("This is the user's home directory: ", os.path.expanduser('~'))
print("This is the path to the current file: ", os.path.abspath(__file__))
print("This is the current process id: ", os.getpid())
print("This is the parent process id: ", os.getppid())
