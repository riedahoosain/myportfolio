# This program will allow users to compress and uncompress files

import PySimpleGUI as sg


def create_gui():

    # Theme
    sg.theme('Black')

    # GUI Buttons and labels
    label1 = sg.Text("Choose and option to Extract or Compress Files")
    compress_button = sg.Button("Compress")
    extract_button = sg.Button("Extract")
    exit_button = sg.Button("Exit")

    # GUI Design
    menu_layout = [[label1],
                   [compress_button],
                   [extract_button],
                   [exit_button],]

    # Show the GUI
    window = sg.Window('InnoZip File Extract or Compress',
                       layout=menu_layout)
    return window


# Main Program

window = create_gui()

while True:
    event, values = window.read()

    match event:

        case 'Compress':
            sg.popup('File Compression Function will be written here')

        case 'Extract':
            sg.popup('File Extraction Function will be written here')

        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break

window.close()
