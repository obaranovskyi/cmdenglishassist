from . import anki_generator
from ..shared.url_core import parse_encoded_url_to_words
from ..shared.read_json import read_json
from ..shared.read_yaml import read_yaml
from ..shared.read_markdown import read_markdown_lines
from ..translation.core import translate_multiple_words
from .parse_type import get_type, ParseType
from .parse_markdown import parse_markdown_to_questions


def handle(args):
    url_or_file = args.url_or_file
    words_or_questions = None
    parse_type = get_type(url_or_file).value 
    if parse_type == ParseType.URL.value:
        words_or_questions = get_word_translations(url_or_file)
    elif parse_type == ParseType.JSON.value:
        words_or_questions = get_questions_from_json(url_or_file)
    elif parse_type == ParseType.YAML.value:
        words_or_questions = get_questions_from_yaml(url_or_file)
    elif parse_type == ParseType.MARKDOWN.value:
        words_or_questions = get_questions_from_markdown(url_or_file)
    anki_generator.generate_anki(words_or_questions, parse_type)


def get_word_translations(url):
    words = parse_encoded_url_to_words(url)
    return translate_multiple_words(words)


def get_questions_from_json(json):
    questions = read_json(json)
    return questions if questions else []

    
def get_questions_from_yaml(yaml):
    questions = read_yaml(yaml)
    return questions if questions else []

def get_questions_from_markdown(markdown_file):
    markdown = read_markdown_lines(markdown_file)
    questions = parse_markdown_to_questions(markdown)
    return questions
    
