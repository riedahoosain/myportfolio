import PySimpleGUI as sg
import convert_to_meters

# GUI Buttons
label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text("0m", key="meters")


# GUI Layout
menu_layout = [[label1, input1],
               [label2, input2],
               [convert_button, output_label]]

# Show the GUI
window = sg.Window('Convertor', layout=menu_layout)

while True:
    event, values = window.read()

    match event:
        case "Convert":
            feet = float(values["feet"])
            inches = float(values["inches"])
            meters = convert_to_meters.convert(feet,inches)
            window["meters"].update(value=f"{meters} m")

        case sg.WIN_CLOSED:
            break

window.close()
