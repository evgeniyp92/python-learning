import functions
import FreeSimpleGUI as gui

label = gui.Text('Type in a todo')
input_box = gui.InputText(tooltip='Enter a todo', key='todo')
add_button = gui.Button('Add')
list_box = gui.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10))
edit_button = gui.Button('Edit')

window = gui.Window('My Todo App',
                    layout=[
                        [label],
                        [input_box, add_button],
                        [list_box, edit_button]
                        ],
                    font=('Helvetica', 16)
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
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case gui.WIN_CLOSED:
            break
        case _:
            pass

window.close()
