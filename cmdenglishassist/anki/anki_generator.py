import genanki
import random
from datetime import datetime
from ..shared.date_core import format_dt
from .templates import to_base_template, to_base_highlight_template
from .question_type import QuestionType


def generate_anki(words_or_questions):
    date = format_dt(datetime.now()).replace(' ', '_')
    deck_id = random.randrange(1 << 30, 1 << 31)
    my_deck = genanki.Deck(deck_id, f"English_{date}")
    for w_or_q in words_or_questions:
        model_id = random.randrange(1 << 30, 1 << 31)
        my_model = genanki.Model(model_id,
          f'English_{date}',
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

        anki_question = None
        anki_answer = None

        question_type = w_or_q.get('type')

        if question_type:
            if question_type == QuestionType.HIDDEN_WORD_IN_SENTENCE.value:
                title = f"{w_or_q.get('title')}<br><br>" if w_or_q.get('title') else ''
                anki_question = w_or_q.get('src').replace('{?}', f" {w_or_q.get('question')} ")
                anki_question = to_base_template( f'{title}{anki_question}')
                answer = w_or_q.get('src').replace('{?}', f"<mark>{w_or_q.get('answer')}</mark>")
                anki_answer = to_base_highlight_template(answer)

            if question_type == QuestionType.RANDOM_WORD_SENTENCE.value:
                title = f"{w_or_q.get('title')}<br><br>" if w_or_q.get('title') else ''
                is_question = True if w_or_q.get('src').find('?') > -1 else False
                sentence_in_words = w_or_q.get('src').replace('?', '').split()
                random.shuffle(sentence_in_words)

                if is_question:
                    sentence_in_words.append('?')
                    
                anki_question = to_base_template(f"{title}{' / '.join(sentence_in_words)}")
                anki_answer = to_base_template(w_or_q.get('src'))
                
        else:
            anki_question = to_base_template(w_or_q.get('translation'))
            anki_answer = to_base_template(w_or_q.get('original_value'))

        my_note = genanki.Note(
          model=my_model,
          fields=[f'{anki_question}', f'{anki_answer}'])

        my_deck.add_note(my_note)

    anki_folder = './'
    anki_questions_file = anki_folder + f"anki_question{date}.apkg"
    genanki.Package(my_deck).write_to_file(anki_questions_file)
