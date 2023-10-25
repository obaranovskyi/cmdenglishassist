from .handler import handle
from ..shared.parser import subparsers


def read_subparser():
    audio = subparsers.add_parser('read', help='Generate audio file from provided content.')
    audio.add_argument('filename', type=str, help='File with content to read.')
    audio.set_defaults(func=handle)
