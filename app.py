from flask import Flask, jsonify,request
import os, sys, random
from time import sleep
from telethon import TelegramClient, sync
from telethon.errors import SessionPasswordNeededError, FloodWaitError
from telethon.tl.functions.messages import  GetHistoryRequest

app = Flask(__name__)

@app.route('/get_code', methods=['GET','POST'])
def get_code():
    phone = request.args.get('phone')
    while True:
        if phone == 'xx':
            #
            return jsonify({
                "code": "xx",
                "message": "số điện thoại không hợp lệ",
                "phone": phone,
                "status": 0
            })
        else:
            api_id = 2015084
            api_hash = '24e8f34925604e25a9b8d695b21cf333'
            client = TelegramClient("session/"+phone,api_id,api_hash)
            client.connect()
            if not client.is_user_authorized():
                print (F"Session lỗi!" + phone)
                #client.log_out()
                client.disconnect()
                return jsonify({
                    "code": "xx",
                    "message": "Lỗi session",
                    "phone": phone,
                    "status": 0
                })
                    
            else:
                for message in client.get_messages(777000, limit=1):
                    msg = message.message
                    you_code = msg.split()[2].rstrip('.')
                    
                    client.disconnect()
                return jsonify({
                    "code": you_code,
                    "message": "Successfully",
                    "phone": phone,
                    "status": 1
                })  

# Start Flask Server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1911, debug=True)