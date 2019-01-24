#!/usr/bin/env python3.7

import socket
import os
import sys
from command_line_telegram.actions import do as do_action
from command_line_telegram.client import get_client
import json

session = sys.argv[1]
name = os.path.basename(session)
dirname = os.path.dirname(session)

client = get_client(name)
client.tg.start()

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
server.close()
os.remove(session)
