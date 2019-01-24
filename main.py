#!/usr/bin/env python3.7

from argparse import ArgumentParser
from do_command import do_command

top_parser = ArgumentParser(prog='clam')
top_subparsers = top_parser.add_subparsers(title='actions', dest='action', required=True)
top_parser.add_argument('-s', '--session-name', type=str, default='default')
top_parser.add_argument('-D', '--sessions_directory', type=str, default='/tmp/clam-1000')

login_parser = top_subparsers.add_parser('login')

send_parser = top_subparsers.add_parser('send')
send_parser.add_argument('chat', type=int, nargs='+')
send_parser.add_argument('-t', '--text', nargs='*', default=[])
send_parser.add_argument('-f', '--file', nargs='*', default=[])
send_parser.add_argument('-i', '--image', nargs='*', default=[])

start_parser = top_subparsers.add_parser('start')

kill_parser = top_subparsers.add_parser('kill')

list_parser = top_subparsers.add_parser('list')
list_parser.add_argument('-d', '--dialogs', action='store_true')
list_parser.add_argument('-s', '--short', action='store_true')
list_parser.add_argument('-c', '--total-count', action='store_true')
list_parser.add_argument('-l', '--limit', type=int, default=15)
list_parser.add_argument('-o', '--offset', type=int, default=0)
list_parser.add_argument('-u', '--username', action='store_true')
list_parser.add_argument('-t', '--type', action='store_true')
list_parser.add_argument('--id', action='store_true')
list_parser.add_argument('-m', '--minimal', action='store_true')

do_command(top_parser.parse_args())
