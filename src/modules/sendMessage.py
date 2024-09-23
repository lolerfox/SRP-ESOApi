import subprocess as sp

import requests
import json
import time

from src.modules.file_descriptor import file_descriptor
CREATE_NO_WINDOW = 0x08000000
server = sp.Popen("python src/modules/app.py", creationflags=CREATE_NO_WINDOW)
# server = sp.Popen("python src/modules/app.py")

cfg = file_descriptor("src/config/config.json", 'json', 'r')

url = f"http://{cfg['settings']['server_ip']}:{cfg['settings']['server_port']}/{cfg['settings']['endpoint']}"
headers = cfg['settings']['headers']

session = requests.Session()
session.get(url)


def sendMessage(type, text, arg=None, skillcount=None, skillsLine=None,):

    def response(payload):
        response = session.post(url, headers=headers, data=json.dumps(payload))


    if type == 'sendMessage':
        payload = {"type": "sendMessage", "data": {"text": text}}
        response(payload)

    elif type == 'dice':
        if skillcount > 25:
            text = f'\\\{skillsLine} Показатели данного игрока слишком высоки (сумма скилов больше 25 на {skillcount-25}!!!))'
            payload = {"type": "sendMessage", "data": {"text": text}}
            response(payload)
        else:
            payload1 = {"type": "sendMessage", "data": {"text": text}}
            response(payload1)
            payload2 = {"type": "sendMessage", "data": {"text": arg}}
            time.sleep(1.3)
            response(payload2)
