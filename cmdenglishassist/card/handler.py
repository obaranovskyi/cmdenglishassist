from cmdenglishassist.shared.url_core import parse_encoded_url_to_words
from cmdenglishassist.translation.core import translate_multiple_words
from .card_generator import CardGenerator


def handle(args):
    words = parse_encoded_url_to_words(args.url)
    word_translations = translate_multiple_words(words)
    card_generator = CardGenerator()
    card_generator.convert(word_translations)

