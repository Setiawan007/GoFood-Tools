from datetime import date
from genericpath import exists
import json
import validators
import os
import platform
import string
import random
from time import sleep
import requests
from urllib.parse import urlparse
import keyboard
from sys import exit

# pyinstaller --onefile --key Aswasw -i gojek.ico gojek.py

ver = "v3.6"
art = """
     ██████╗  ██████╗      ██╗███████╗██╗  ██╗                
    ██╔════╝ ██╔═══██╗     ██║██╔════╝██║ ██╔╝                
    ██║  ███╗██║   ██║     ██║█████╗  █████╔╝                 
    ██║   ██║██║   ██║██   ██║██╔══╝  ██╔═██╗                 
    ╚██████╔╝╚██████╔╝╚█████╔╝███████╗██║  ██╗                
     ╚═════╝  ╚═════╝  ╚════╝ ╚══════╝╚═╝  ╚═╝                
     ██████╗██████╗ ███████╗ █████╗ ████████╗ ██████╗ ██████╗ 
    ██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
    ██║     ██████╔╝█████╗  ███████║   ██║   ██║   ██║██████╔╝
    ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██║   ██║██╔══██╗
    ╚██████╗██║  ██║███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
     ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                              
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
    cek = requests.get("https://raw.githubusercontent.com/setiawan007/setiawan007.github.io/main/version.json").json()
    cek = cek['gojek']
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

def clear():
  system = platform.system()
  if system == "Windows":
      os.system("cls")
  else:
      os.system("clear")

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

def send(url,payload,token=None,otp=None):
  host = urlparse(url).netloc
  headers = {
    "X-AppVersion": "4.47.1",
    "X-AppId": "com.gojek.app",
    "Accept": "application/json",
    "Content-Type": "application/json; charset=UTF-8",
    "X-User-Type": "customer",
    "Host": host,
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
  }
  if token is not None:
      headers["Authorization"] = f"Bearer {token}"
  if otp is not None:
      headers["otp"] = otp
  post = requests.post(url, json=payload, headers=headers)
  result = post.json()
  return result

def send_otp(nama,email,nmr):
  token = send("https://api.gojekapi.com/v5/customers", {"email":email,"name":nama,"phone":nmr,"signed_up_country":"ID"})
  if token['success'] == False:
    clear()
    print()
    print(error)
    print("\tNomor sudah terdaftar / tidak valid !!!")
    print()
    sleep(3)
    return 0
  token = token['data']['otp_token']
  return token

def smshub(url,api):
    req = requests.get(f'https://smshub.org/stubs/handler_api.php?api_key={api}&action={url}')
    return req.text

try:
  file_data = exists("data.txt")
  if file_data == False:
      clear()
      print()
      print(error)
      print("\tFile data.txt tidak ditemukan !!!")
      print()
      sleep(5)
      exit()
  data = json.loads(open('data.txt', 'r').read().split('###############################')[1])
  api = data['api']
  op_num = data['operator']
  domain_email = data['domain_email']
  pin = data['pin']

  list_operator = ["any", "axis", "indosat", "smartfren", "telkomsel", "three"]
  if op_num not in ["1", "2", "3", "4", "5", "6"]:
    op_num = 1
  operator = list_operator[int(op_num)-1]
  if (validators.domain(domain_email) != True):
    domain_email = "mail.com"

  ip = requests.get('https://api.ipify.org').text
  os.system('@echo off')
  os.system('MODE 80,30')
  os.system(f'title Gojek Tools {ver}')
  # check()
  print(art)
  print("#############################")
  print("# Created by : Anonim #")
  print("# Publish by : @tahaluindo #")
  print(f"# Your IP : {ip}  #")
  print("#############################")
  print()
  print("1. OTP Manual")
  print("2. OTP Auto ( Api SMSHUB )")
  print()
  mode = input("Pilih Mode (1/2): ")
  while mode not in ["1","2"]:
    clear()
    print(art)
    print("##################################")
    print("# Created by : Setiawan007 #")
    print(f"# Your IP :  {ip}      #")
    print("##################################")
    print()
    print("1. OTP Manual")
    print("2. OTP Auto ( Api SMSHUB)")
    print()
    mode = input("Pilih Mode (1/2): ")
  if mode == "2":
    if len(api) < 30:
      clear()
      print()
      print(error)
      print("\tAPI Key tidak valid !!!")
      print()
      sleep(5)
      exit()
  print()
  if mode == "2":
    req_balance = smshub("getBalance", api).split(':')
    balance = req_balance[1]
    total_otp = round(float(balance) / 3.5)
    print(f"Sisa Saldo: {balance}")
    print(f"Perkiraan sisa OTP: {total_otp}")
    print()
  data = requests.get('https://api.namefake.com/indonesian-indonesia/random').json()
  nama = data['name'].split(' ')
  nama = f"{nama[0]} {nama[1]}"
  email = f"{data['email_u']}@{domain_email}"
  print(f"Nama: {nama}")
  print(f"Email: {email}")
  if mode == "1":
    nmr = input("Nomor: 62")
    nmr = f"62{nmr}"
  else:
    nmr = smshub(f'getNumber&service=ni&operator={operator}&country=6', api).split(':')
    id = nmr[1]
    nmr = nmr[2]
    print(f"Nomor: {nmr}")
  
  otp_token = send_otp(nama,email,nmr)
  while otp_token == 0:
    clear()
    print(art)
    print("##################################")
    print("# Created by : Setiawan007 #")
    print(f"# Your IP :  {ip}      #")
    print("##################################")
    print()
    print(f"Nama: {nama}")
    print(f"Email: {email}")
    if mode == "1":
      nmr = input("Nomor: 62")
      nmr = f"62{nmr}"
    else:
      smshub(f'setStatus&status=8&id={id}', api)
      sleep(1)
      nmr = smshub(f'getNumber&service=ni&operator={operator}&country=6', api).split(':')
      sleep(1)
      id = nmr[1]
      nmr = nmr[2]
      print(f"Nomor: {nmr}")
    otp_token = send_otp(nama,email,nmr)
  print()
  print("Mengirimkan OTP...")
  if mode == "1":
    otp = input("OTP (R/r untuk resend): ")
    while otp.lower() == "r":
      otp_token = send_otp(nama,email,nmr)
      otp = input("OTP (R/r untuk resend): ")
  else:
    otp = smshub(f'getStatus&id={id}', api).split(':')
    print("Menunggu OTP...")
    print("Tekan B beberapa kali untuk Batal")
    while otp[0] == "STATUS_WAIT_CODE":
      if keyboard.is_pressed('b'):
        smshub(f'setStatus&status=8&id={id}', api)
        print("Berhasil dibatalkan...")
        sleep(5)
        exit()
      otp = smshub(f'getStatus&id={id}', api).split(':')
      sleep(1)
    print(f"OTP: {otp[1]}")
    otp = otp[1]

  print ("Memverifikasi OTP...")
  get_data = send("https://api.gojekapi.com/v5/customers/phone/verify", {"client_name":"gojek:consumer:app","client_secret":"pGwQ7oi8bKqqwvid09UrjqpkMEHklb","data":{"otp":otp,"otp_token":otp_token}})
  if mode == "1":
    while get_data['success'] == False:
      print("OTP salah !!!")
      otp = input("OTP (R/r untuk resend): ")
      print ("Memverifikasi OTP...")
      get_data = send("https://api.gojekapi.com/v5/customers/phone/verify", {"client_name":"gojek:consumer:app","client_secret":"pGwQ7oi8bKqqwvid09UrjqpkMEHklb","data":{"otp":otp,"otp_token":otp_token}})
  sleep(1)
  refresh_token = get_data['data']['refresh_token']
  access_token = get_data['data']['access_token']
  sleep(1)
  access_token = send("https://goid.gojekapi.com/goid/token", {"client_id":"gojek:consumer:app","client_secret":"pGwQ7oi8bKqqwvid09UrjqpkMEHklb","data":{"refresh_token": refresh_token},"grant_type":"refresh_token","scopes":[]}, access_token)
  sleep(1)
  refresh_token = access_token['refresh_token']
  access_token = access_token['access_token']

  print("Menyimpan Token...")
  tgl = date.today()
  tgl = tgl.strftime("%d-%m-%Y")
  f = open("result.txt", "a")
  if mode == "1":
    f.write(f"62{nmr} | {refresh_token} | {access_token} | {tgl}\n\n")
  else:
    f.write(f"{nmr} | {refresh_token} | {access_token} | {tgl}\n\n")
  f.close()

  print("Membuat AuthPreferences...")
  xml = f"""<?xml version='1.0' encoding='utf-8' standalone='yes' ?>
  <map>
      <string name="locale">en</string>
      <string name="accessToken">{access_token}</string>
      <string name="refreshToken">{refresh_token}</string>
  </map>"""
  f = open("AuthPreferences.xml", "w")
  f.write(xml)
  f.close()

  print()

  if mode == "1":
    print("Tekan Enter untuk set PIN...")
    input()
  print("Mengirimkan OTP...")
  sleep(1)
  set_pin = send('https://customer.gopayapi.com/v1/users/pin',{"pin":pin},access_token)
  if mode == "1":
    otp = input("OTP (R/r untuk resend): ")
    while otp.lower() == "r":
      set_pin = send('https://customer.gopayapi.com/v1/users/pin',{"pin":pin},access_token)
      otp = input("OTP (R/r untuk resend): ")
  else:
    smshub(f'setStatus&status=3&id={id}', api)
    otp = smshub(f'getStatus&id={id}', api).split(':')
    while otp[0] == "STATUS_WAIT_CODE" or otp[0] == "STATUS_WAIT_RETRY":
      otp = smshub(f'getStatus&id={id}', api).split(':')
    print(f"OTP: {otp[1]}")
    otp = otp[1]
  set_pin = send('https://customer.gopayapi.com/v1/users/pin',{"pin":pin},access_token,otp)

  if set_pin['success'] == True:
    print("Set PIN berhasil...")
    print()
    input("Tekan Enter untuk keluar...")
  else:
    print("Set PIN gagal...")
    print("Silahkan set PIN secara Manual")
    print()
    input("Tekan Enter untuk keluar...")

except:
  pass
# except Exception as x:
#   print(x)
#   input()
