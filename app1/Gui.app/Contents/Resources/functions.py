# Functions are exported by default

def get_todos(filepath='todos.txt'):
    """Open file and return list of todos"""
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath='todos.txt'):
    """Write todos to file"""
    with open(filepath, "w") as file:
        file.writelines(todos)