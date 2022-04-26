from telethon import TelegramClient,sync
from telethon import functions, types
from colorama import Fore
from telethon.errors.rpcerrorlist import *
from telethon.errors import *
# import python_socks
import os
#Bảng màu
R = Fore.RED 
B = Fore.BLUE
G = Fore.GREEN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
C = Fore.CYAN
BA = Fore.BLACK
api_id = 16084692
api_hash = 'd2854dd168da24ae3805cc6450488425'
if not os.path.exists("session"):
   os.makedirs("session")
def session():
    print(Y+"Input phone")
    phone = input("Nhập số điện thoại (định dạng như sau +84123456789): " + M)
    # ip = input("ip: " + M)
    # port = input("port: " + M)
    # username = input("username: " + M)
    # password = input("password:" + M)
    # proxy = (python_socks.ProxyType.SOCKS5, ip, int(port), True, username, password)
    # client = TelegramClient("session/" + phone, api_id, api_hash, proxy=proxy)
    client = TelegramClient("session/" + phone, api_id, api_hash)
    client.connect()
    if not client.is_user_authorized():
        try:
            client.send_code_request(phone)
            client.sign_in(phone, input(M + "Code login : "))
            print(G+"Create success session")
            print("Tạo thành công session "+Y+phone)
            with open("list.txt","a") as file:
                file.write(phone+"\n")
        except SessionPasswordNeededError:
            client.start(phone,input(M+'Password 2FA: '))
            print(G+"Create success session")
            print("Tạo thành công session "+Y+phone)
           
            with open("list.txt","a") as file:
                file.write(phone+"\n")
        except Exception as e:
            print(R,e," ",phone)
        client.disconnect()
    else:
        print(B+"Session has been created ")
        print("Session đã tạo từ trước "+phone)
        client.disconnect()
    print(C+"="*40)
while(True):
    session()