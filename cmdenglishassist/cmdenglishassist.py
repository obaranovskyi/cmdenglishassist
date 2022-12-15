import sys

from .shared.parser import parser
from .json.subparser import json_subparser
from .card.subparser import card_subparser
from .audio.subparser import audio_subparser


def set_default_to_help():
    if len(sys.argv) == 1:
        sys.argv.append('-h')

def register_subparsers():
    json_subparser()
    card_subparser()
    audio_subparser()

def main():
    set_default_to_help()
    register_subparsers()
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
