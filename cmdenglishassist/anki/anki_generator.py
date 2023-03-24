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
          templates = [
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
            question_title = f"{w_or_q.get('questionTitle')}<br><br>" if w_or_q.get('questionTitle') else ''
            answer_title = f"{w_or_q.get('answerTitle')}<br><br>" if w_or_q.get('answerTitle') else ''

            if question_type == QuestionType.SIMPLE_QUESTION.value:
                anki_question = to_base_template(f"{question_title}{w_or_q.get('question')}")
                anki_answer = to_base_template(f"{answer_title}{w_or_q.get('answer')}")

            if question_type == QuestionType.HIDDEN_WORD_IN_SENTENCE.value:
                anki_question = w_or_q.get('src')
                anki_answer = w_or_q.get('src')
                for i, q in enumerate(w_or_q.get('questions')):
                    anki_question = anki_question.replace('{'+str(i)+'}', q)
                    anki_answer = anki_answer.replace('{'+str(i)+'}', f"<mark>{w_or_q.get('answers')[i]}</mark>")
                anki_question = to_base_template(f'{question_title}<br><br>{anki_question}')
                anki_answer = to_base_highlight_template(f'{answer_title}<br><br>{anki_answer}')

            if question_type == QuestionType.RANDOM_WORD_SENTENCE.value:
                is_question = True if w_or_q.get('src').find('?') > -1 else False
                sentence_in_words = w_or_q.get('src').replace('?', '').split()
                random.shuffle(sentence_in_words)
                if is_question:
                    sentence_in_words.append('?')
                anki_question = to_base_template(f"{question_title}{' / '.join(sentence_in_words)}")
                anki_answer = to_base_template(f"{answer_title}{w_or_q.get('src')}")
                
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
