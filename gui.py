import functions
import PySimpleGUI as sg

label = sg.Text("Enter a Todo : ")
input_box = sg.InputText(tooltip="Enter Todo" , key="todo")
add_button = sg.Button("Add")


window = sg.Window("My To-do App " ,
                  layout= [[label],[input_box , add_button]] , 
                  font=('Helvetica' ,15))

while True:

    event , values = window.read() 
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        
        case sg.WIN_CLOSED:
            break


window.close() 