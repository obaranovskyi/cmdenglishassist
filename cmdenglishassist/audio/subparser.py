from .handler import handle
from ..shared.parser import subparsers


def audio_subparser():
    audio = subparsers.add_parser('audio', help='Generate audio files along with translations.')
    audio.add_argument('url', type=str, help='Google translate url.')
    audio.set_defaults(func=handle)
