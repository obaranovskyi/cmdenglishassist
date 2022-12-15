from ..shared.url_core import parse_encoded_url_to_words
from ..translation.core import translate_multiple_words
from .audio_generator import AudioGenerator


def handle(args):
    words = parse_encoded_url_to_words(args.url)
    word_translations = translate_multiple_words(words)
    audio_generator = AudioGenerator()
    audio_generator.convert(word_translations)

