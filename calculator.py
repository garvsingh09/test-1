import PySimpleGUI as sg

# Set theme
sg.theme('DarkBlue3')

# Define the layout
layout = [
    [sg.Text('', size=(20, 1), key='-OUTPUT-', 
             font=('Arial', 24), justification='right', 
             relief=sg.RELIEF_SUNKEN, pad=(5, 15))],
    [sg.Button('7', key='7', size=(5, 2), button_color=('black', '#f0f0f0')), 
     sg.Button('8', key='8', size=(5, 2), button_color=('black', '#f0f0f0')), 
     sg.Button('9', key='9', size=(5, 2), button_color=('black', '#f0f0f0')), 
     sg.Button('/', key='/', size=(5, 2), button_color=('white', '#4CAF50'))],
    [sg.Button('4', key='4', size=(5, 2), button_color=('black', '#f0f0f0')), 
     sg.Button('5', key='5', size=(5, 2), button_color=('black', '#f0f0f0')), 
     sg.Button('6', key='6', size=(5, 2), button_color=('black', '#f0f0f0')), 
     sg.Button('*', key='*', size=(5, 2), button_color=('white', '#4CAF50'))],
    [sg.Button('1', key='1', size=(5, 2), button_color=('black', '#f0f0f0')), 
     sg.Button('2', key='2', size=(5, 2), button_color=('black', '#f0f0f0')), 
     sg.Button('3', key='3', size=(5, 2), button_color=('black', '#f0f0f0')), 
     sg.Button('-', key='-', size=(5, 2), button_color=('white', '#4CAF50'))],
    [sg.Button('0', key='0', size=(5, 2), button_color=('black', '#f0f0f0')), 
     sg.Button('.', key='.', size=(5, 2), button_color=('black', '#f0f0f0')), 
     sg.Button('=', key='=', size=(5, 2), button_color=('white', '#2196F3')), 
     sg.Button('+', key='+', size=(5, 2), button_color=('white', '#4CAF50'))],
    [sg.Button('C', key='C', size=(10, 2), button_color=('white', '#ff6b6b')), 
     sg.Button('⌫', key='BACK', size=(10, 2), button_color=('white', '#ff9999'))],
]

# Create window
window = sg.Window('Simple Calculator', layout, size=(320, 420), 
                   finalize=True)

expression = ""

# Event loop
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    
    if event == 'C':
        expression = ""
    elif event == 'BACK':
        expression = expression[:-1]
    elif event == '=':
        try:
            expression = str(eval(expression))
        except:
            expression = "Error"
    else:
        expression += event
    
    window['-OUTPUT-'].update(expression)

window.close()
