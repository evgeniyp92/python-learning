import time

import functions
import FreeSimpleGUI as gui
import os



clock = gui.Text('', key='clock')
label = gui.Text('Type in a todo')
input_box = gui.InputText(tooltip='Enter a todo', key='todo')
add_button = gui.Button('Add')
list_box = gui.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10))
edit_button = gui.Button('Edit')
complete_button = gui.Button('Complete')
exit_button = gui.Button('Exit', size=60)

window = gui.Window('My Todo App',
                    layout=[
                        [clock],
                        [label],
                        [input_box, add_button],
                        [list_box, edit_button, complete_button],
                        [exit_button],
                        ],
                    font=('Helvetica', 16)
                    )

while True:
    event, values = window.read(timeout=500)
    window['clock'].update(value=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                gui.popup('Please select an item first', font=("Helvetica", 16))
        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            break
        case gui.WIN_CLOSED:
            break
        case _:
            pass

window.close()
