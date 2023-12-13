import PySimpleGUI as sg
import convert_to_meters


sg.theme('Black')

# GUI Buttons
label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")
output_label = sg.Text("0m", key="meters")


# GUI Layout
menu_layout = [[label1, input1],
               [label2, input2],
               [convert_button, exit_button, output_label]]

# Show the GUI
window = sg.Window('Convertor', layout=menu_layout, font=('Helvetica', 20))

while True:
    event, values = window.read()

    match event:
        case "Convert":
            try:
                feet = float(values["feet"])
                inches = float(values["inches"])
                meters = convert_to_meters.convert(feet,inches)
                window["meters"].update(value=f"{meters} m")
            except ValueError:
                sg.popup('Please provide two numbers.', font=('Helvetica', 20))

        case "Exit":            
            break

        case sg.WIN_CLOSED:
            break

window.close()
