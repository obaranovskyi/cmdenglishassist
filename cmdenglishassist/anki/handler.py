from . import anki_generator
from ..shared.url_core import parse_encoded_url_to_words
from ..shared.read_json import read_json
from ..shared.read_yaml import read_yaml
from ..translation.core import translate_multiple_words


def handle(args):
    words_or_questions = None
    is_url = args.url_or_json.startswith('http')
    is_json = args.url_or_json.endswith('.json')
    is_yaml = args.url_or_json.endswith('.yml') or args.url_or_json.endswith('.yaml')
    if is_url:
        words_or_questions = get_word_translations(args.url_or_json)
    elif is_json:
        words_or_questions = get_questions_from_json(args.url_or_json)
    elif is_yaml:
        words_or_questions = get_questions_from_yaml(args.url_or_json)
    anki_generator.generate_anki(words_or_questions)


def get_word_translations(url):
    words = parse_encoded_url_to_words(url)
    return translate_multiple_words(words)


def get_questions_from_json(json):
    questions = read_json(json)
    return questions if questions else []

    
def get_questions_from_yaml(yaml):
    questions = read_yaml(yaml)
    return questions if questions else []
