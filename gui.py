import functions
import PySimpleGUI as sg

label = sg.Text("Enter a Todo : ")
input_box = sg.InputText(tooltip="Enter Todo")
add_button = sg.Button("add")


window = sg.Window("My To-do App " , layout= [[label],[input_box , add_button]])
window.read()
window.close()