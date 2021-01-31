import requests
from urllib.parse import quote
import json
from googletrans import Translator
import pyperclip

def process_message(message):
    if message is not None:
        translator = Translator()
        result = translator.translate(message, dest='en')
        message = result.text
        qt_message = quote(message)

        url = "https://robomatic-ai.p.rapidapi.com/api.php"

        payload = "SessionID=RapidAPI1&in={}&op=in&cbid=1&cbot=1&ChatSource=RapidAPI&key=RHMN5hnQ4wTYZBGCF3dfxzypt68rVP".format(qt_message)
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'x-rapidapi-key': "0b5aecd98emshcd88d6a68b53e49p10edc8jsn182d65fecc8f",
            'x-rapidapi-host': "robomatic-ai.p.rapidapi.com"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        try:
            res = json.loads(response.text)
            res = translator.translate(res["out"],dest='gu')
            pyperclip.copy(res.text)
            return res.text.encode().decode("utf-8")
        except Exception as e:
            print(str(e))
            res = translator.translate(message, dest='gu')
            pyperclip.copy(res.text)
            return message
    else:
        return "please do not use it again!!"
