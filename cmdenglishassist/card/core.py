def add_next_line_on_long_phrase(value):
    if len(value) < 30:
        return value
    words = value.split(' ')
    lines = ''
    line = ''
    for index, word in enumerate(words):
        is_first = index == 0
        is_last = index == len(words) - 1
        line += word if is_first else f' {word}'
        if len(line) >= 30 or is_last:
            lines += line.lstrip() + '\n'
            line = ''
    return lines
