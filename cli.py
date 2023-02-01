import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ",now)

while True:
    user_input = input("Enter Add , Show , Edit ,complete or Exit : " ) + '\n'
    user_input = user_input.strip()

    if user_input.startswith('add'):
        todo = user_input[4:] + "\n" 
        """
            # Traditional Way

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

        """
        # With Context Manager
        todos = functions.get_todo()

        todos.append(todo)

        functions.write_todos(todos)
        
    elif user_input.startswith('show'):
        todos = functions.get_todo()
            
        i = 1
        for item in todos:
            item = item.strip('\n')
            print(f'{i}-{item}')
            i= i + 1
        
    elif user_input.startswith('edit'):
        try:
            number = int(user_input[5:])
            number = number - 1

            todos = functions.get_todo()

            new_todo = input("Enter the Todo : ") 
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

        
        except ValueError:
            print("You Entered invalid Operation") 
            continue

    elif user_input.startswith('complete'):
        try:
            number = int(user_input[9:])

            todos = functions.get_todo()

            index = number - 1
            removed_item = todos[index].strip('\n')
            todos.pop(index)
                
            functions.write_todos(todos)


            print(f'Todo "{removed_item}" Removed From the List')
        except IndexError:
            print("Entered Number is Not in a List ")
            
    elif user_input.startswith('exit'):
        break
    else:
        print("Command is Not Valid .......")

print("Bye!")