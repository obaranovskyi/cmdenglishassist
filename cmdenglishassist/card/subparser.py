from .handler import handle
from ..shared.parser import subparsers


def card_subparser():
    card = subparsers.add_parser('card', help='Generate cards in pdf for printing.')
    card.add_argument('url', type=str, help='Google translate url.')
    card.set_defaults(func=handle)
