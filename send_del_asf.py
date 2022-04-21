import requests
import time
import json 
import re 


welcome ='''                                                                                                       _ _                   
 _____ _____ ____  _____    _____ __ __            _   _                  _    _       _   _ _       _| | |_ ___ ___ ___ ___ 
|     |  _  |    \|   __|  | __  |  |  |   ___ ___| |_| |___    _ _ _ ___| |  | |_ ___| |_|_| |_ ___|_     _|_  |_  |_  |  _|
| | | |     |  |  |   __|  | __ -|_   _|  | . | .'| . | | . |  | | | | -_| |  | '_| -_|  _| | . | .'|_     _| | |  _|_  |_  |
|_|_|_|__|__|____/|_____|  |_____| |_|    |  _|__,|___|_|___|  |_____|___|_|  |_,_|___|_| |_|___|__,| |_|_|   |_|___|___|___|
                                          |_|                                                                                '''


def sendMessage(token, channel_id, message):
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id)
    data = {"content": message}
    header = {"authorization": token}
    r = requests.post(url, data=data, headers=header)
    #print(r.status_code)
    data = json.loads(r.text)
    message_id = data["id"]
    url_del = url + "/" + message_id
    
    r_del = requests.delete(url_del,headers=header)
    #print(r_del.status_code)
    

def start_bot(my_token,channel_id):
    while True:
        for token in my_tokens.values():
            #print(token)
            sendMessage(token,channel_id,"hi")
        time.sleep(61)

my_tokens = {"korza" : "OTU3Mzk2Mjk3ODAxOTMyOTAw.YmCmcg.Hhc-n3sJwLG_3sbW2S_wVMq6n8E",
"bilbasse" : "OTU3Mzk4MjAwNjczNzkyMDQw.YmE3xw.EEMq8du7EBO8V5PLMiIBZR2mp50",
"armsl" : "OTU3NDAxNzU3OTU1MjgwOTg2.YmE4Qw.3eCdyyN2pG4Yz-Y5JlhSMkaIQ_M",
"toastv2" : "ODM0ODgxNzg2NjEzNDY1MTE4.YmE40Q.9-Pci82kDt9nT-G7YKg2RBL_WBY",
"pastARK" : "ODUzMzAyMjA0MzA3MzQxMzI3.YmE-NQ.CuvCviFhoiBaEC9aAIQkiqIryRE",
"svens" : "OTY2NDI3MjcyMDUzNjc0MDg1.YmE-gA.vK9hywTwjR9Rdr1nFNA2tF9KIVQ"}



channelid = "938640740077158441"
print(welcome)
start_bot(my_tokens,channelid)

