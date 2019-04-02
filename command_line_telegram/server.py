#!/usr/bin/env python3.7

import socket
import os
import sys
from command_line_telegram.actions import do as do_action
from command_line_telegram.client import get_client
import json
from shlex import quote

session = sys.argv[1]
name = os.path.basename(session)
dirname = os.path.dirname(session)

client = get_client(name)
tg = client.tg

favorites = os.path.join(client.clam_workdir, 'favorites')

@tg.on_message()
def on_message(c, msg):
    global favorites

    if not os.path.exists(favorites):
        return

    with open(favorites) as f:
        fav = list(map(lambda id: id[:-1], f.readlines()))
        if msg['chat']['type'] == 'private' and str(msg['from_user']['id']) in fav:
            if msg['text']:
                os.system('talk ' + quote(msg['text']))
            else:
                os.system('talk media')
        f.close()

tg.start()

if not os.path.exists(dirname):
    os.mkdir(dirname)
if os.path.exists(session):
    os.remove(session)

server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind(session)
server.listen(socket.SOMAXCONN)

while True:
    conn, addr = server.accept()
    data = conn.recv(1048576)
    if not data:
        break
    else:
        args = eval(data.decode('utf-8'))
        if args['action'] == 'kill':
            break
        do_action(client.tg, args, conn)
tg.stop()
server.close()
os.remove(session)
