import sys

from .shared.parser import parser


def set_default_to_help():
    if len(sys.argv) == 1:
        sys.argv.append('-h')

def register_subparsers():
    # register subparsers here
    pass

def main():
    set_default_to_help()
    register_subparsers()
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
