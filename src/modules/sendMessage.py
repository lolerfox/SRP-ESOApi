import subprocess as sp

import requests
import json
import time

from src.modules.file_descriptor import file_descriptor


config = file_descriptor("src/config/config.json", 'json', 'r')

url = f"http://{config['settings']['server_ip']}:{config['settings']['server_port']}/{config['settings']['endpoint']}"
headers = config['settings']['headers']

server = sp.Popen("python src/modules/app.py", shell=False)

session = requests.Session()
session.get(url)


def sendMessage(type, text, arg=None, skillcount=None, skillsLine=None,):
    if skillcount is None or skillcount < 25:
        skillWarn = False
    elif skillcount > 25:
        skillWarn = True

    if skillWarn:
        text = f'\\\{skillsLine} Показатели данного игрока слишком высоки (сумма скилов больше 25 на {skillcount-25}!!!))'
        payload = {"type": "sendMessage", "data": {"text": text}}
        response = session.post(url, headers=headers, data=json.dumps(payload))

    if type == 'sendMessage':
        payload = {"type": "sendMessage", "data": {"text": text}}
        response = session.post(url, headers=headers, data=json.dumps(payload))

    elif type == 'dice' and not skillWarn:
        payload1 = {"type": "sendMessage", "data": {"text": text}}
        payload2 = {"type": "sendMessage", "data": {"text": arg}}

        response = session.post(url, headers=headers, data=json.dumps(payload1))
        time.sleep(1.5)
        response = session.post(url, headers=headers, data=json.dumps(payload2))
