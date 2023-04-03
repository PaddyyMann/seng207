import PySimpleGUI as sg
import qrcode
import io
from PIL import Image

layout = [
    [sg.Text('Enter data to encode:')],
    [sg.Input(key='-DATA-')],
    [sg.Button('Generate QR code'), sg.Button('Exit')],
    [sg.Image(key='-IMAGE-')],
    [sg.Text('', key='-STATUS-')],
]

window = sg.Window('QR Code Generator', layout,background_color='blue')

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'): 
        break
    if event == 'Generate QR code':
        data = values['-DATA-']
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')

        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        window['-IMAGE-'].update(data=img_bytes.read())

window.close()