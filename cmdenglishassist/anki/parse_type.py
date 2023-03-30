from enum import Enum 

class ParseType(Enum):
    URL = 1
    JSON = 2
    YAML = 3
    MARKDOWN = 4

def get_type(value):
    if value.startswith('http'):
        return ParseType.URL
    elif value.endswith('.json'):
        return ParseType.JSON
    elif value.endswith('.yml') or value.endswith('.yaml'):
        return ParseType.YAML
    elif value.endswith('.md'):
        return ParseType.MARKDOWN
