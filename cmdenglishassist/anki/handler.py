from . import anki_generator
from ..shared.url_core import parse_encoded_url_to_words
from ..shared.read_json import read_json
from ..translation.core import translate_multiple_words


def handle(args):
    is_url = args.url_or_json.startswith('http')
    anki_generator.generate_anki(
        get_word_translations(args.url_or_json) if is_url else get_questions_from_json(args.url_or_json)
    )

def get_word_translations(url):
    words = parse_encoded_url_to_words(url)
    return translate_multiple_words(words)

def get_questions_from_json(json):
    questions = read_json(json)
    return questions if questions else []
    
