from argparse import ArgumentParser
import sys
from methods import put_message

parser = ArgumentParser()
parser.add_argument('-m', '--message', help='path to message | default in - console')
parser.add_argument('-s', '--stego', help='path to the stegocontainer | default out - console')
parser.add_argument('-c', '--container', help='path to container', required=True)

args = parser.parse_args()

put_message(args.message, args.container, args.stego)
