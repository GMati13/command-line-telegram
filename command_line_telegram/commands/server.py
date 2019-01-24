import sys
import socket
import os
from command_line_telegram.client import get_client
import socket

actions = ['start', 'kill']

__dirname = os.path.dirname(os.path.realpath(__file__))
__server = os.path.join(__dirname, '..', 'server.py')

def do(args):
    if args.action == 'start':
        start(args)
    if args.action == 'kill':
        kill(args)

def start(args):
    client = get_client(args.session_name)
    session = os.path.join(args.sessions_directory, args.session_name)
    if not os.path.exists(client.clam_session):
        print('Error: can not start session. use \'clam login --help\'')
        sys.exit()
    if not os.path.exists(args.sessions_directory):
        os.mkdir(args.sessions_directory)
    if os.path.exists(session):
        print('Error: session {s} already started'.format(
            s=args.session_name
        ))
        sys.exit()
    os.system('setsid python3.7 {s} {session} > /tmp/null 2> {errlog} &'.format(
        s=__server,
        session=session,
        errlog=os.path.join(os.path.dirname(client.clam_session), args.session_name + '.log')
    ))
    sys.exit()

def kill(args):
    session = os.path.join(args.sessions_directory, args.session_name)
    if os.path.exists(session):
        client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        client.connect(session)
        client.send({
            'action': 'kill'
        })
