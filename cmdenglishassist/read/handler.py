from .read_generator import ReadGenerator


def handle(args):
    read_generator = ReadGenerator()
    read_generator.convert(args.filename)

