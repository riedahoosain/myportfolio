import PySimpleGUI as sg
from extract_archive import extract_archive


def create_gui():

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


# Main Program

window = create_gui()

while True:
    event, values = window.read()
    #print(event, values)
    match event:

        case "Extract":
            archivefilepath = values['archive']            
            destinationfolder = values['folder']          
            window["output"].update(value="extraction in progress")
            extract_archive(archivefilepath, destinationfolder)
            window["output"].update(value="extraction has been completed")

        case sg.WIN_CLOSED:
            break




window.close()
