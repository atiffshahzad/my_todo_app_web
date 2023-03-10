FILEPATH = "Files/todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text and return the list of to-do items.
    """
    with open(filepath, 'r') as file_local:
        """this will write in a file"""
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
