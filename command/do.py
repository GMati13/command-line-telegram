import sys
from command.auth import login
from command.message import send_text, send_image, send_file
from command.history import get_dialogs, get_chat
from lib.tg.client import telegram as tg

def do_command(values):
    tg.start()
    if sys.argv[1] == 'send':
        if values.text:
            send_text(values.chat, values.text)
        if values.image:
            send_image(values.chat, values.image)
        if values.file:
            send_file(values.chat, values.file)
        if not values.text and not values.image and not values.file:
            send_text(values.chat, '\n'.join(map(lambda s: '`'+s[:-1]+'`', sys.stdin.readlines())))
    elif sys.argv[1] == 'history':
        if values.dialogs:
            get_dialogs(values)
        elif values.chat:
            get_chat(values)

    tg.stop()
