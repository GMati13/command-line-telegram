from lib.tg.client import Telegram
from getpass import getpass
import config

def login():
    tg = Telegram().start()
    tg.stop()
