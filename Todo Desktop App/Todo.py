import todoFile
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todo.txt"):
    with open("todo.txt" , "w") as file:
        pass

sg.theme("Black")
clock = sg.Text('',key='clock')
label = sg.Text("Type in a work to do: ")
input_box = sg.InputText(tooltip="Enter Todo", key="todoItem")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=todoFile.get_todos(),
                      key="todo",
                      enable_events=True,
                      size=[45,10])
edit_btn = sg.Button("Edit")
complete_btn = sg.Button("Complete")
exit_btn = sg.Button("Exit")

window = sg.Window('ToDo APP',
                   layout = [[clock],
                             [label], 
                             [input_box], 
                             [add_button], 
                             [list_box,edit_btn, complete_btn],
                             [exit_btn]],
                   font = ("Roboto", 14))
while True:
    btn_label, values = window.read(timeout=900)
    window['clock'].update(value = time.strftime("%b %d, %Y %H:%M:%S"))
    match btn_label:
        case "Add":
            todo = todoFile.get_todos()
            new_todo = values["todoItem"] + "\n"
            todo.append(new_todo)
            todoFile.write_todos(todo)

            window['todo'].update(values=todo)
            window["todoItem"].update(value="")

        case "Edit":
            try:
                edit_todo = values["todo"][0]
                new_todo = values['todoItem'] + "/n"

                todos = todoFile.get_todos()
                index = todos.index(edit_todo)
                todos[index] = new_todo
                todoFile.write_todos(todos)

                window['todo'].update(values=todos)
            
            except IndexError:
                sg.popup("Please select an item")
        
        case 'todo':
            window["todoItem"].update(value=values['todo'][0])

        case 'Complete':
            try:
                completed_todo = values["todo"][0]
                todos = todoFile.get_todos()
                todos.remove(completed_todo)
                todoFile.write_todos(todos)
                window["todo"].update(values=todos)
                window["todoItem"].update(value="")
            
            except IndexError:
                sg.popup("Please select an item")
            
        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break

    
window.close()