import os
from collections import namedtuple
from pyrogram import Client

def get_client(session_name):
    clam_workdir = os.path.join(os.environ['HOME'], '.clam')
    clam_session = os.path.join(clam_workdir, '{s}.session'.format(s=session_name))
    return namedtuple('client', [
        'clam_session',
        'clam_workdir',
        'tg'
    ])(
        clam_session,
        clam_workdir,
        Client(
            session_name,
            api_id='403859',
            api_hash='118250775a656486d2bb61f85746168e',
            workdir=clam_workdir
        )
    )

