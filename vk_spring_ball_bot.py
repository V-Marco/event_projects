from flask import Flask, request, json
import vk

orgs = {#*#}

session = vk.Session()
api = vk.API(session, v = 5.0)

def send_message(user_id, message, attachment = ""):
    api.messages.send(access_token = '#*#', user_id = str(user_id), message = message, attachment = attachment)

def create_answer(data):
    user_id = data['user_id']

    org_list = orgs[str(user_id)]
    message = 'Вам написал(а) ' + org_list[1]  + ': vk.com/id' + str(user_id)
    send_message(org_list[0], message)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    
    if 'type' not in data.keys():
        return 'Type is not found.'
    if data['type'] == 'confirmation':
        return '#*#'
    elif data['type'] == 'message_new':
        create_answer(data['object'])
        return 'Success'
