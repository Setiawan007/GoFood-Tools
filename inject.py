from lib2to3.pgen2.token import RPAR
from os.path import exists
import os
import sys
import tempfile
from time import sleep
import requests 

# pyinstaller --onefile --key Aswasw -i inject.ico --add-data "adb;adb" inject.py
ver = "v2.3"

art = """
    ██╗███╗   ██╗     ██╗███████╗ ██████╗████████╗
    ██║████╗  ██║     ██║██╔════╝██╔════╝╚══██╔══╝
    ██║██╔██╗ ██║     ██║█████╗  ██║        ██║   
    ██║██║╚██╗██║██   ██║██╔══╝  ██║        ██║   
    ██║██║ ╚████║╚█████╔╝███████╗╚██████╗   ██║   
    ╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   
    ███╗   ███╗███████╗███╗   ███╗██╗   ██╗       
    ████╗ ████║██╔════╝████╗ ████║██║   ██║       
    ██╔████╔██║█████╗  ██╔████╔██║██║   ██║       
    ██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██║   ██║       
    ██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║╚██████╔╝       
    ╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝        
                                                  
"""

error = """
    ███████╗██████╗ ██████╗  ██████╗ ██████╗     ██╗██╗██╗
    ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    ██║██║██║
    █████╗  ██████╔╝██████╔╝██║   ██║██████╔╝    ██║██║██║
    ██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗    ╚═╝╚═╝╚═╝
    ███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║    ██╗██╗██╗
    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝╚═╝╚═╝
                                                          
"""

expired = """
        ███████╗██╗  ██╗██████╗ ██╗██████╗ ███████╗██████╗     ██╗██╗██╗
        ██╔════╝╚██╗██╔╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗    ██║██║██║
        █████╗   ╚███╔╝ ██████╔╝██║██████╔╝█████╗  ██║  ██║    ██║██║██║
        ██╔══╝   ██╔██╗ ██╔═══╝ ██║██╔══██╗██╔══╝  ██║  ██║    ╚═╝╚═╝╚═╝
        ███████╗██╔╝ ██╗██║     ██║██║  ██║███████╗██████╔╝    ██╗██╗██╗
        ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝     ╚═╝╚═╝╚═╝
                                                                        
"""

def check():
    cek = requests.get("https://raw.githubusercontent.com/aarzaary/aarzaary.github.io/main/version.json").json()
    cek = cek['inject']
    try:
        if cek != ver:
            print()
            print(expired)
            print("\tAplikasi Dinonaktifkan :)")
            print("\tYuk Download Versi Terbaru :)")
            print()
            sleep(3)
            exit()
    except:
        pass
        exit()

try:
    os.system('@echo off')
    os.system('MODE 80,30')
    os.system(f'title Inject Gojek Memu {ver}')
    # check()
    file_xml = exists("AuthPreferences.xml")
    if file_xml == False:
        print()
        print(error)
        print("\tAuthPreferences.xml tidak ditemukan")
        sleep(3)
        exit()
    print(art)
    print("#############################")
    print("# Github : Tahaluindo #")
    print("#############################")
    print()
    os.system(f'{sys._MEIPASS}\\adb\\adb.exe connect 127.0.0.1:21503 > nul')
    os.system(f'{sys._MEIPASS}\\adb\\adb.exe devices')
    input("Tekan Enter untuk Inject...")
    print()
    push = os.system(f'{sys._MEIPASS}\\adb\\adb.exe push AuthPreferences.xml /data/data/com.gojek.app/shared_prefs/AuthPreferences.xml > nul')
    os.system(f'{sys._MEIPASS}\\adb\\adb.exe shell am force-stop com.gojek.app')
    print()
    if push == 0:
        print("Inject Berhasi...")
    else:
        print("Inject Gagal...")
    os.system(f'{sys._MEIPASS}\\adb\\adb.exe kill-server')
    sleep(3)
except:
    pass
