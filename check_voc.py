import os
from os.path import exists
import random
import string
import requests
from time import sleep

# pyinstaller --onefile --key Aswasw -i gojek.ico check_voc.py
ver = "v3.4"

art = """
     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
    ██║     ███████║█████╗  ██║     █████╔╝ 
    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
    ██╗   ██╗ ██████╗  ██████╗              
    ██║   ██║██╔═══██╗██╔════╝              
    ██║   ██║██║   ██║██║                   
    ╚██╗ ██╔╝██║   ██║██║                   
     ╚████╔╝ ╚██████╔╝╚██████╗              
      ╚═══╝   ╚═════╝  ╚═════╝              
                                            
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
    cek = cek['check_voc']
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

def lokasi():
  lat = -7.779671
  lon = 110.364365
  dec_lat = random.random()
  dec_lon = random.random()
  result = f"{lat+dec_lat},{lon+dec_lon}"
  return result

def rantext(length):
  result = ''.join((random.choice(string.ascii_lowercase + string.digits) for x in range(length))) 
  return result

list_version = ["5.0","5.0.2","5.1","5.1.1","6.0","6.0.1","7.0","7.1","7.1.2","8.0","8.1","9","10","11","12"]
list_brand = ["Samsung","Google","Xiaomi","Oppo","Vivo","Asus"]
uniqueid = rantext(16)
xm1 = rantext(600)
sessionid = f"{rantext(8)}-{rantext(4)}-{rantext(4)}-{rantext(4)}-{rantext(12)}"
model = rantext(5).upper()
version = list_version[random.randint(0,len(list_version)-1)]
brand = list_brand[random.randint(0,len(list_brand)-1)]
accuracy = random.randint(1,10)

def get_voc(token=None):
    headers = {
    "X-AppVersion": "4.47.1",
    "X-AppId": "com.gojek.app",
    "Accept": "application/json",
    "Content-Type": "application/json; charset=UTF-8",
    "X-User-Type": "customer",
    "Host": "api.gojekapi.com",
    "User-Agent": "okhttp/3.12.13",
    "X-Location-Accuracy": f"{accuracy}.0",
    "X-Location": lokasi(),
    "X-UniqueId": uniqueid,
    "X-Platform": "Android",
    "X-Session-Id": sessionid,
    "x-deviceos": f"Android,{version}",
    "x-phonemake": brand,
    "x-phonemodel": f"{brand},{model}",
    "x-m1": xm1,
    "gojek-timezone": "Asia/Jakarta",
    "gojek-service-area": "9",
    }
    if token is not None:
        headers["Authorization"] = f"Bearer {token}"

    requests.get(f"https://api.gojekapi.com/gofood/v2/deals/home?picked_loc={lokasi()}", headers=headers)
    get = requests.get("https://api.gojekapi.com/gopoints/v3/wallet/vouchers?limit=10&page=1", headers=headers)
    result = get.json()
    if 'success' in result:
        total_voucher = result['voucher_stats']['total_vouchers']
        return total_voucher
    else:
        return "Token Expired"

try: 
    os.system('@echo off')
    os.system('MODE 80,30')
    os.system(f'title Check VOUCHER {ver}')
    # check()
    file = exists("result.txt")
    if file == False:
        print()
        print(error)
        print("\tresult.txt tidak ditemukan")
        sleep(3)
        exit()
    print(art)
    print("#############################")
    print("# Created by : Anonim #")
    print("# Publish by : @tahaluindo #")
    print("#############################")
    print()
    no = 1
    data = {}
    cek = open("result.txt", "r")
    split = cek.read().split("\n")
    for x in split:
        if x != "":
            token = x.split(" ")
            nmr = token[0]
            access = token[4]
            resfresh = token[2]
            tgl = ""
            if len(token) == 5:
                tgl = ""
            else:
                tgl = f" | {token[6]}"
            print(f"[{no}] {nmr} => {get_voc(access)}{tgl}")
            data[no] = [resfresh, access]
            no += 1
    cek.close()
    print()
    print("Check Selesai...")
    print()
    ok = input("[?] Ingin membuat file AuthPreference? (y/n) : ")
    if ok == "y":
        print("[*] Pilih nomor token untuk membuat AuthPreference")
        pilihan = input(f"[*] Nomor (1-{no-1}) => ")

        if int(pilihan) not in range(1, no):
            print("[!] Pilihan tidak valid")
            sleep(5)
            exit()
        else:
            refresh_token = data[int(pilihan)][0]
            access_token = data[int(pilihan)][1]
            xml = f"""<?xml version='1.0' encoding='utf-8' standalone='yes' ?>
            <map>
                <string name="locale">en</string>
                <string name="accessToken">{access_token}</string>
                <string name="refreshToken">{refresh_token}</string>
            </map>"""
            f = open("AuthPreferences.xml", "w")
            f.write(xml)
            f.close()
            print("[*] Berhasil membuat AuthPreferences.xml")
            print()
            input("Tekan Enter untuk keluar...")
    else:
        print()
        input("Tekan Enter untuk keluar...")
except:
  pass
# except Exception as x:
#   print(x)
#   input()
