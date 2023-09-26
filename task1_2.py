from argparse import ArgumentParser
import sys
from methods import get_message

parser = ArgumentParser()
parser.add_argument('-m', '--message', help='path to message | default in - console')
parser.add_argument('-s', '--stego', help='path to the stegocontainer | default out - console')

args = parser.parse_args()

get_message(args.message, args.stego)
