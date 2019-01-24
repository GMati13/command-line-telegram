from commands.server import actions as server_actions, do as server_do
from commands.client import actions as client_actions, do as client_do

def do_command(args):
    if args.action in server_actions:
        server_do(args)
    if args.action in client_actions:
        client_do(args)
