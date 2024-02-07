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
        system("adb connect {phone_ip}:9999")

def run_scrcpy():
    system("scrcpy")
        
def run_tcpip():
    system("adb tcpip 9999")

layout = [
        [sg.VPush()],
     [sg.Push(),sg.Text('Welcome to Phone Controller'), sg.Push()],
     [sg.VPush()],
     [sg.Push(), sg.Button('Connect to Phone', size = (10, 2), font=('young 15 bold')), sg.Push()]
     ]
        
window = sg.Window('Phone Controller', layout, size=(300, 300), font=('young 12'))

while True:
     event, value = window.read()

     if event == sg.WINDOW_CLOSED:
          break

window.close()

