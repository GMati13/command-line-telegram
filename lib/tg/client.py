import os
import sys
from pyrogram import Client
from pyrogram.api import functions as api
import config

class FilterOut(object):
    def __init__(self):
        self.stream = sys.stdout

    def __getattr__(self, attr_name):
        return getattr(self.stream, attr_name)
    
    def write(self, data:str):
        if data.find('Pyrogram') == 0 or data.find('Licensed') == 0 or data.find('\n\n') == 0:
            self.stream.flush()
            return
        self.stream.write(data)
        self.stream.flush()

class Telegram(Client):
    def __init__(self):
        self.__session_file = os.path.join(config.app_dir, '{s}.session'.format(s=config.session_name))
        super().__init__(
            config.session_name,
            workdir=config.app_dir,
            app_version='0.0.1',
            device_model='',
            system_version='Linux',
            api_id='403859',
            api_hash='118250775a656486d2bb61f85746168e'
        )

    def start(self):
        stdout = sys.stdout
        sys.stdout = FilterOut()
        super().start()
        sys.stdout = stdout
    
telegram = Telegram()
