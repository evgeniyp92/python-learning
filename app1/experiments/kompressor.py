import FreeSimpleGUI as sg
import zipper

label1 = sg.Text('Enter files to compress')
input1 = sg.Input()
choose_button1 = sg.FilesBrowse('...', key='files')

label2 = sg.Text('Enter destination folder')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('...', key='outDir')

compress_button = sg.Button('Compress')

window = sg.Window(
    'Kompressor',
    layout=[
        [label1, input1, choose_button1],
        [label2, input2, choose_button2],
        [compress_button]
    ]
)

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(';')
    folder = values['outDir']
    zipper.make_arch(filepaths, folder)

window.close()
