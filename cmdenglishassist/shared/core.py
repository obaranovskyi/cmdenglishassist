import uuid

def convert_words_to_json_with_uuid(words): 
    return list(
        map(
            lambda value : { 
                "wordId": str(uuid.uuid4()),
                "translation": value["translation"],
                "originalValue": value["original_value"]
            },
            words
        )
    )

