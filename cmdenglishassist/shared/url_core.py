from urllib.parse import unquote_plus, urlparse, parse_qs


def parse_encoded_url_to_words(url_value: str):
    terminal_parse_result = replace_terminal_encoding(url_value)
    unquote_plus_result = unquote_plus(terminal_parse_result)
    parsed_result = urlparse(unquote_plus_result.replace('\n', ''))
    text_value = parse_qs(parsed_result.query.replace(';', '#'))['text'][0]

    return text_value.split('#')[0:-1]


def replace_terminal_encoding(value_to_decode: str):
    return value_to_decode.replace('\\&', '&').replace('\\?', '?').replace('\\=', '=').replace('\\(', '(').replace('\\)', ')')
