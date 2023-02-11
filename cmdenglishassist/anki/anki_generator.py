import genanki
import random
from datetime import datetime
from ..shared.date_core import format_dt


def generate_anki(words):
    date = format_dt(datetime.now()).replace(' ', '_')
    deck_id = random.randrange(1 << 30, 1 << 31)
    my_deck = genanki.Deck(deck_id, f"Words_{date}")
    for wtr in words:
        model_id = random.randrange(1 << 30, 1 << 31)
        my_model = genanki.Model(model_id,
          f'Words_{date}',
          fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
          ],
          templates=[
            {
              'name': 'Card type 1',
              'qfmt': '{{Question}}',
              'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
          ])

        question = wtr.get('translation')
        ankiAnswer = wtr.get('original_value')
        my_note = genanki.Note(
          model=my_model,
          fields=[f'{question}', f'{ankiAnswer}'])

        my_deck.add_note(my_note)

    anki_folder = './'
    anki_questions_file = anki_folder + f"anki_question{date}.apkg"
    genanki.Package(my_deck).write_to_file(anki_questions_file)
