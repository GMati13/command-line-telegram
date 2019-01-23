#!/usr/bin/env python3

from argparse import ArgumentParser
from command.do import do_command
import sys

parser = ArgumentParser(prog='clam')
parser.add_argument('--logout', action='store_true', help='sign out from telegram account')

subparsers = parser.add_subparsers()

send_parser = subparsers.add_parser('send', help='send message')
send_parser.add_argument('-t', '--text', help='text of message')
send_parser.add_argument('-f', '--file', nargs='*', help='path to file or files',)
send_parser.add_argument('-i', '--image', nargs='*', help='path to image file or files')
send_parser.add_argument('chat', nargs='+', type=int, help='username, user id or chat id')

history_parser = subparsers.add_parser('history', help='see history --help for more')
history_parser.add_argument('-d', '--dialogs', action='store_true', help='show dialogs list')
history_parser.add_argument('-u', '--chat', type=int, help='show chat messages list')
history_parser.add_argument('--short', action='store_true', help='display short message')
history_parser.add_argument('-n', '--number', type=int, default=10, help='number of dialogs/messages')
history_parser.add_argument('--offset', type=int, default=0, help='offset number of dialogs/messages')
history_parser.add_argument('--ids', action='store_true', help='show ids of chats')
history_parser.add_argument('-r', '--reverse', action='store_true', help='reverse dialogs/messages list')

values = parser.parse_args()

if len(sys.argv) > 1:
    do_command(values)
sys.exit()
