import functions
import FreeSimpleGUI as gui

label = gui.Text('Type in a todo')
input_box = gui.InputText(tooltip='Enter a todo', key='todo')
add_button = gui.Button('Add')

window = gui.Window('My Todo App',
                    layout=[
                        [label], [input_box], [add_button]
                        ],
                    font=('Helvetica', 20)
                    )

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case 'Edit':
            pass
        case gui.WIN_CLOSED:
            break
        case _:
            pass

window.close()
