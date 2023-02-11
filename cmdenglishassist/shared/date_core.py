DATE_FORMAT = '%Y-%m-%d'
DATETIME_FORMAT = f'{DATE_FORMAT} %H:%M:%S'

def format_dt(dt):
    return dt.strftime(DATETIME_FORMAT)
