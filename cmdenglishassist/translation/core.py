from googletrans import Translator

    
def translate_word(value: str):
    translator = Translator()
    return translator.translate(text=value, dest='uk').text

def translate_multiple_words(value_list):
    result_list = []
    translator = Translator()
    translations = translator.translate(text=value_list, dest='uk')
    for index, translation in enumerate(translations):
        result_list.append({
            'original_value': value_list[index],
            'translation': translation.text
        })
    return result_list
