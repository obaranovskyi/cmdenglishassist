from . import anki_generator
from ..shared.url_core import parse_encoded_url_to_words
from ..translation.core import translate_multiple_words


def handle(args):
    words = parse_encoded_url_to_words(args.url)
    word_translations = translate_multiple_words(words)
    anki_generator.generate_anki(word_translations)
