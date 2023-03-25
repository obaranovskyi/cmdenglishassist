from . import anki_generator
from ..shared.url_core import parse_encoded_url_to_words
from ..shared.read_json import read_json
from ..shared.read_yaml import read_yaml
from ..translation.core import translate_multiple_words


def handle(args):
    url_or_file = args.url_or_file
    words_or_questions = None
    is_url = url_or_file.startswith('http')
    is_json = url_or_file.endswith('.json')
    is_yaml = url_or_file.endswith('.yml') or url_or_file.endswith('.yaml')
    if is_url:
        words_or_questions = get_word_translations(url_or_file)
    elif is_json:
        words_or_questions = get_questions_from_json(url_or_file)
    elif is_yaml:
        words_or_questions = get_questions_from_yaml(url_or_file)
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
