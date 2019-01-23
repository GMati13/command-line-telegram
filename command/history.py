from lib.tg.client import telegram as tg

def get_dialogs(args):
    dialogs = tg.get_dialogs(limit=args.number+args.offset)
    print('total:', dialogs['total_count'])
    for dialog in (dialogs['dialogs'][args.offset:] if not args.reverse else dialogs['dialogs'][args.offset:][::-1]):
        if dialog['chat']['type'] == 'private':
            label = dialog['chat']['first_name']
            if dialog['chat']['last_name']:
                label += ' ' + dialog['chat']['last_name']
        else:
            label = dialog['chat']['title']
        if args.ids:
            print('{l} {id}'.format(l=label, id=dialog['chat']['id']))
            continue
        if dialog['top_message']['text']:
            message = dialog['top_message']['text']
            if args.short:
                message = message.replace('\n', '↲')[:100]
        else:
            message = '[ error: unsupported message type ]'
        print('{l} ({t})\n\t{m}'.format(t=dialog['chat']['type'], l=label, m=message))

def get_chat(args):
    chat = tg.get_history(args.chat, limit=args.number, offset=args.offset, reversed=args.reverse)
    print('total:', chat['total_count'])
    for message in chat['messages']:
        label = message['from_user']['first_name']
        if message['from_user']['last_name']:
            label += ' ' + message['from_user']['last_name']
        if message['text']:
            msg = message['text']
            if args.short:
                msg = msg.replace('\n', '↲')[:100]
        else:
            msg = '[ error: unsupported message type ]'
        print('{l}\n\t{m}'.format(l=label, m=msg))
