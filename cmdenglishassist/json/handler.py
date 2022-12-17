import json
from ..shared.url_core import parse_encoded_url_to_words
from ..shared.core import convert_words_to_json_with_uuid
from ..translation.core import translate_multiple_words


def handle(args):
    words = parse_encoded_url_to_words(args.url)
    word_translations = translate_multiple_words(words)
    dict_words = convert_words_to_json_with_uuid(word_translations)
    print(json.dumps(dict_words))
