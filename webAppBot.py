from tkinter import Y
from urllib import request
import requests
from definition_1 import menu 

#'http://t.me/CashbackExpress_bot'
bot = "5342176536:AAEknzzBVOeMu31IaPUogLs-98cpDFnPjYA"

r = requests.get('https://api.telegram.org/bot%s/getUpdates'%bot).json()
print(r)

for x in r['result']:
    update_id = x['update_id']
    print(update_id)
    if 'message' in x:
        if x['message']['text'] == '/inline':
            chat_id = x['message']['chat']['id']
            main = menu(chat_id, bot)
            main.inline()
            
    
    # delete the message
    requests.get('https://api.telegram.org/bot%s/getUpdates&offset=%s'%(bot,int(update_id)+1))