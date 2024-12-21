import Functions
import FreeSimpleGUI as sg

label = sg.Text(" Type in a to do")
input_box = sg.InputText(tooltip="Enter a to do", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 14))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = Functions.get_todos()
            new_todo = values['todo']+ "\n"
            todos.append(new_todo)
            Functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()