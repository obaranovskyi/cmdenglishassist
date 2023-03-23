import json


def read_json(file):
    try:
        with open(file, 'r') as json_file:
            json_data = json.load(json_file)
            return json_data
    except Exception:
        print('Something wrong with json file.')
