import os

def do(client, args, conn):
    if args['action'] == 'send':
        send(client, args)
    if args['action'] == 'list':
        get_list(client, args, conn)

def send(client, data):
    for chat in data['chat']:
        if data['text']:
            client.send_message(chat, data['text'])
        if data['image']:
            for i in data['image']:
                client.send_photo(chat, i)
        if data['file']:
            for f in data['file']:
                client.send_document(chat, f)

def get_list(client, data, conn):
    if data['dialogs']:
        dialogs = client.get_dialogs(limit=data['limit']+data['offset'], pinned_only=data['pinned'])
        conn.sendall(str({
            'total': dialogs['total_count'],
            'dialogs': list(map(parse_dialog(data), dialogs['dialogs'][data['offset']:]))
        }).encode('utf-8'))
    if data['history']:
        history = client.get_history(data['history'], limit=data['limit'], offset=data['offset'])
        conn.sendall(str({
            'total': history['total_count'],
            'messages': list(map(parse_message(data), history['messages'][data['offset']:]))
        }).encode('utf-8'))

def parse_dialog(data):
    def parser(dialog):
        if dialog['chat']['type'] == 'private':
            name = dialog['chat']['first_name']
            if dialog['chat']['last_name']:
                name += ' ' + dialog['chat']['last_name']
        else:
            name = dialog['chat']['title']
        if data['type']:
            name += ' ({t})'.format(t=dialog['chat']['type'])
        if data['username'] and dialog['chat']['username']:
            name += ' [@{t}]'.format(t=dialog['chat']['username'])
        if data['id']:
            name += ' uid({uid})'.format(uid=dialog['chat']['id'])
        if data['minimal']:
            return name
        if dialog['top_message']['text']:
            text = dialog['top_message']['text']
            if data['short']:
                _t = text.replace('\n', '↲')
                text = _t[:100]
                if len(_t) > 100:
                    text += '...'
        else:
            text = '[ unsupported message type ]'
        return '{n}:\n\t{t}'.format(
            n=name,
            t=text
        )
    return parser

def parse_message(data):
    def parser(message):
        if message['chat']['type'] == 'private':
            name = message['from_user']['first_name']
            if message['from_user']['last_name']:
                name += ' ' + message['from_user']['last_name']
        else:
            name = message['from_user']['title']
        if data['type']:
            name += ' ({t})'.format(t=message['chat']['type'])
        if data['username'] and message['from_user']['username']:
            name += ' [@{t}]'.format(t=message['from_user']['username'])
        if data['id']:
            name += ' uid({uid})'.format(uid=message['from_user']['id'])
        if data['minimal']:
            return name
        if message['text']:
            text = message['text']
            if data['short']:
                _t = text.replace('\n', '↲')
                text = _t[:100]
                if len(_t) > 100:
                    text += '...'
        else:
            text = '[ unsupported message type ]'
        return '{n}:\n\t{t}'.format(
            n=name,
            t=text
        )
    return parser
