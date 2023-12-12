# This program will allow users to compress and uncompress files

import PySimpleGUI as sg
from zipper import make_archive, extract_archive


def main_gui():

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
                   [exit_button]]

    # Show the GUI
    window = sg.Window('InnoZip File Extract or Compress',
                       layout=menu_layout, font=('Helvetica', 20))
    return window


def extract_gui():
    # Theme
    sg.theme('Black')

    # GUI Buttons and labels
    label1 = sg.Text("Select archive")
    input1 = sg.Input()
    choose_button1 = sg.FileBrowse("Choose", key="archive")

    label2 = sg.Text("Select destination folder")
    input2 = sg.Input()
    choose_button2 = sg.FolderBrowse("Choose", key="folder")

    extract_button = sg.Button("Extract")
    output_label = sg.Text("Hit Extract after choosing files and folder", key="output")

    # GUI Design
    menu_layout = [[label1, input1, choose_button1],
                   [label2, input2, choose_button2],
                   [extract_button, output_label]]

    # Show the GUI
    window = sg.Window('Archive Extractor', 
                       layout=menu_layout)
    return window
    

def compress_gui():
     # GUI Buttons
    label1 = sg.Text("Select files to compress")
    input1 = sg.Input()
    choose_button1 = sg.FilesBrowse("Choose", key="files")

    label2 = sg.Text("Select destination folder")
    input2 = sg.Input()
    choose_button2 = sg.FolderBrowse("Choose", key="folder")

    compress_button = sg.Button("Compress")
    output_label = sg.Text(
        "Hit Compress after choosing files and folder", key="output")

    # GUI Design
    menu_layout = [[label1, input1, choose_button1],
                   [label2, input2, choose_button2],
                   [compress_button, output_label]]

    # Show the GUI
    window = sg.Window('My Zipper App', layout=menu_layout)

    return window
    

# Main Program

main_window = main_gui()

while True:   
    event, values = main_window.read()
    print(event, values)


    match event:

        case 'Compress':            
            compress_window = compress_gui()
            compress_window.read()
            compress_window.close            

        case 'Extract':
            extract_window = extract_gui()
            extract_window.read()
            extract_window.close()            

        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break

main_window.close()
