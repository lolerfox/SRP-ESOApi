from quart import Quart, request, jsonify
from quart_cors import cors

from file_descriptor import file_descriptor

config = file_descriptor("src/config/config.json", 'json', 'r')

esoCommands = []


def pushCommand(esoCommand):
    global esoCommands
    esoCommands.append(esoCommand)


app = Quart(__name__)
app = cors(app)


@app.route('/commands', methods=['POST', 'GET'])
async def commands():
    global esoCommands
    list = []
    if request.method == "POST":
        data = await request.get_json()
        if data:
            if 'sendMessage' in data['type']:
                pushCommand(data)
    else:
        if len(esoCommands) > 0:
            list = esoCommands
            esoCommands = []

        result = {"commands": list}
        return jsonify(result), 200
    return 'OK', 200


if __name__ == '__main__':
    app.run(host=config['settings']['server_ip'], port=config['settings']['server_port'])
