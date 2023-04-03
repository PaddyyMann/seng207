import PySimpleGUI as sg
import pyttsx3

engine = pyttsx3.init()

layout = [
    [sg.Text('Enter text to speak:')],
    [sg.Input(key='-TEXT-')],
    [sg.Radio('Male', 'voice', key='-MALE-'), sg.Radio('Female', 'voice', key='-FEMALE-', default=True)],
    [sg.Button('Speak'), sg.Button('Exit')],
    [sg.Text('', key='-STATUS-')],
]

window = sg.Window('Text-to-Speech App', layout,background_color='cyan')

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'): 
        break
    voice=engine.getProperty('voices')
    if event == 'Speak':
        text = values['-TEXT-']
        if text.strip() != '':
            engine.setProperty('voice', voice[0].id if values['-MALE-'] else voice[1].id)
            engine.say(text)
            engine.runAndWait()
        else:
            window['-STATUS-'].update('Please enter some text.', text_color='red')

window.close()