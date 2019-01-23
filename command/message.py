from lib.tg.client import telegram as tg
import os

def send_text(chats, text, parse_mode='markdown'):
    for chat in chats:
        tg.send_message(chat, text, parse_mode=parse_mode)

def send_image(chats, images):
    for chat in chats:
        for img in images:
            tg.send_photo(chat, os.path.realpath(img))

def send_file(chats, files):
    for chat in chats:
        for f in files:
            tg.send_document(chat, os.path.realpath(f))
