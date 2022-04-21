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

my_tokens = {"korzza(hediwl)" : "OTU3Mzk2Mjk3ODAxOTMyOTAw.Ylv4bg.oOx6204G7kJGQwCRnzD41RihBbU",
"bilbasse" : "OTU3Mzk4MjAwNjczNzkyMDQw.YmBeiw.uh2zbvq-eLz2pNawpO2Utdd9btM",
"armsl" : "OTU3NDAxNzU3OTU1MjgwOTg2.YmBfww.wwzURPtf6spgxOC82U9gRYJ-SDM",
#"tmatemtal" : "OTU3Mzk0MTE5MDcwNzQ0NjI3.YmBgRQ.8I-dGJzV75_YD-12jpHLDO4ccL0",
"PASTark" : "ODUzMzAyMjA0MzA3MzQxMzI3.YmBjHw.GQ5NWXBMy-0JjF_OhgaTl5i8hhE",
"toastv2(alopoalopo98)" : "ODM0ODgxNzg2NjEzNDY1MTE4.YmBjkw.PTRxsmyh082Gj7R7AW6Jlz_PlHU",
"svens_7awet" : "OTY2NDI3MjcyMDUzNjc0MDg1.YmBluA.ui5Z8-CCa6zDbS0o3UIUfRl-rRk"}



channelid = "938640740077158441"
print(welcome)
start_bot(my_tokens,channelid)

