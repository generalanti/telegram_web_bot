import requests, json
from bs4 import BeautifulSoup

class menu:
    def __init__(self, chat_id, bot):
        self.chat_id = chat_id
        self.bot = bot
        
    def gen_ngrok(self):
        req = requests.get('http://127.0.0.1:4040/api/tunnels')
        soup = BeautifulSoup(req.text, 'lxml')
        tunnelsjson = json.loads(soup.find('p').text)
        self.url = tunnelsjson['tunnels'][0]['public_url']
        
    def inline(self):
        self.get_ngrok()
        text = 'Web Apps'
        requests.get('https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s&reply_markup=\
            {"inline_keyboard":[[{"text":"My Web App","web_app":{"url":"%s/oxcash.php"}}]]}'%(self.bot, self.chat_id, text, self.web_url))