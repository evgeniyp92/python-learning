import functions
import FreeSimpleGUI as gui

label = gui.Text('Type in a todo')
input_box = gui.InputText(tooltip='Enter a todo')
add_button = gui.Button('Add')

window = gui.Window('My Todo App', layout=[[label], [input_box], [add_button]])
window.read()
window.close()