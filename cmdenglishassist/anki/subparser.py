from .handler import handle
from ..shared.parser import subparsers


def anki_subparser():
    json = subparsers.add_parser('anki', help='Generate anki deck/package.')
    json.add_argument('url', type=str, help='Google translate url.')
    json.set_defaults(func=handle)
