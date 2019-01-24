import json
import socket
import os
from command_line_telegram.client import get_client
import sys

actions = ['login', 'send', 'list']

client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

def do(args):
    session = os.path.join(args.sessions_directory, args.session_name)
    if args.action == 'login':
        login(args)
        sys.exit()
    check_session(session, args.session_name)
    client.connect(session)
    if args.action == 'send':
        send(args)
    if args.action == 'list':
        get_list(args)
    client.close()

def login(args):
    client = get_client(args.session_name)
    if os.path.exists(client.clam_session):
        print('Warning: already logged')
        sys.exit()
    client.tg.start()
    client.tg.stop()

def send(args):
    check_login(args.session_name)
    text = ' '.join(args.text)
    if not args.text and not args.file and not args.image:
        text = '\n'.join(map(lambda l: '`'+l[:-1]+'`', sys.stdin.readlines()))
    client.send(str({
        'action': 'send',
        'chat': args.chat,
        'text': text,
        'file': list(map(lambda f: os.path.realpath(f), args.file)),
        'image': list(map(lambda i: os.path.realpath(i), args.image))
    }).encode('utf-8'))

def get_list(args):
    check_login(args.session_name)
    client.send(str({
        'action': 'list',
        'dialogs': args.dialogs,
        'short': args.short,
        'limit': args.limit,
        'offset': args.offset,
        'username': args.username,
        'type': args.type,
        'id': args.id,
        'minimal': args.minimal,
        'history': args.history
    }).encode('utf-8'))
    if args.dialogs:
        dialogs = eval(client.recv(1048576).decode('utf-8'))
        for dialog in dialogs['dialogs'][::-1]:
            print(dialog)
        if args.total_count:
            print('total:', dialogs['total'])
    if args.history:
        history = eval(client.recv(1048576).decode('utf-8'))
        for message in history['messages'][::-1]:
            print(message)
        if args.total_count:
            print('total:', history['total'])

def check_session(session, session_name):
    if not os.path.exists(session):
        print('Error: session {s} are not started'.format(
            s=session_name
        ))
        sys.exit()

def check_login(session_name):
    client = get_client(session_name)
    if not os.path.exists(client.clam_session):
        print('Warning: you are not logged')
        sys.exit()
