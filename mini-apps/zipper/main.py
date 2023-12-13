# This app zips a list of files
# This is a GUI application
import PySimpleGUI as sg
from zip_creater import make_archive


def create_gui():

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

window = create_gui()

while True:
    event, values = window.read()
    print(event, values)

    match event:

        case "Compress":
            filepaths = values["files"].split(";")
            folder = values["folder"]
            window["output"].update(value="Compression in progress")
            make_archive(filepaths, folder)
            window["output"].update(value="Compression has been completed")

        case sg.WIN_CLOSED:
            break

window.close()
