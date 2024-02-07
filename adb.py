import os
from os import system
import socket
import PySimpleGUI as sg

ip_addr = socket.gethostbyname(socket.gethostname())

def get_phone_ip():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.connect(("8.8.8.8", 80))
        
        phone_ip = sock.getsockname()[0]
        
        return phone_ip
    except Exception as e:
        print("Error:", e)
        return None

phone_ip = get_phone_ip()
if phone_ip:
    print("IP address of your phone:", phone_ip)
else:
    print("Failed to retrieve the IP address of your phone.")

def run_adb():
    # return system(f"adb connect {phone_ip}:9999")
    system("adb connect 192.168.43.1:9999")
    return False


def run_scrcpy():
    return system("scrcpy")
        
def run_tcpip():
    system("adb tcpip 9999")
    return False

layout = [
        [sg.VPush()],
     [sg.Push(),sg.Text('Welcome to Phone Controller'), sg.Push()],
     [sg.VPush()],
     [sg.Push(), sg.Button('Connect to Phone', size = (10, 2), font=('young 15 bold'), key='connect'), sg.Button('PORT', key='port',visible=False ,size = (10, 2), font=('young 15 bold')), sg.Push()]
     ]
        
window = sg.Window('Phone Controller', layout, size=(300, 300), font=('young 12'))

connected = False
success = False

while True:
    event, value = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    
    if event == 'connect':
        if connected == False:
            connected = run_adb()
        else:
            sg.popup("""Please plug your phone to your \n computer through a usb cord.\n Please ensure you have Developer \n settings enabled on your phone""")
            window['connect'].update(visible=False)
            window['port'].update(visible = True)
    
    if event == 'port':
        if run_tcpip():
            success = True
        else:
            sg.popup("""Connect your phone to your computer through a USB cord and click PORT""")
        

window.close()

