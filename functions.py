def get_todo(filePath="todos.txt"):
    with open(filePath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filePath="todos.txt"):
    with open(filePath, 'w') as file:
        file.writelines(todos_arg)
