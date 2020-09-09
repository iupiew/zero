from googletrans import Translator
import requests

token = '1285338925:AAHNKRvc53_CpZ09Ufy5_i21SjGL4cdqswg'

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot1285338925:AAHNKRvc53_CpZ09Ufy5_i21SjGL4cdqswg/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

trans_bot = BotHandler(token)
translator = Translator()

def main():  
    new_offset = None
    
    while True:

        trans_bot.get_updates(new_offset)

        last_update = trans_bot.get_last_update()
        
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        
        if last_chat_text.lower():
        	
            trans_bot.send_message(last_chat_id, translator.translate(last_chat_text).text)
        
        new_offset = last_update_id + 1

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()        