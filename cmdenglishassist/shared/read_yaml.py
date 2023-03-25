import yaml


def read_yaml(file):
    try:
        with open(file, 'r') as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)
            return yaml_data
    except Exception:
        print('Something wrong with yaml file.')
