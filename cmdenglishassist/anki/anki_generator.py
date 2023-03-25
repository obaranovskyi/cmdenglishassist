import genanki
import random
from datetime import datetime
from ..shared.date_core import format_dt
from .templates import to_base_template, to_base_highlight_template
from .question_type import QuestionType


def generate_anki(words_or_questions):
    date = format_dt(datetime.now()).replace(' ', '_')
    deck_id = get_id()
    deck_name = f"English_{date}"
    my_deck = genanki.Deck(deck_id, deck_name)
    for w_or_q in words_or_questions:
        model = get_model(deck_name)
        anki_question = None
        anki_answer = None
        question_type = w_or_q.get('type')
        if question_type:
            if question_type == QuestionType.SIMPLE_QUESTION.value:
                anki_question, anki_answer = generate_simple_question(w_or_q)
            if question_type == QuestionType.HIDDEN_WORD_IN_SENTENCE.value:
                anki_question, anki_answer = generate_hidden_word_in_sentence(w_or_q)
            if question_type == QuestionType.RANDOM_WORD_SENTENCE.value:
                anki_question, anki_answer = generate_random_word(w_or_q)
        else:
            anki_question, anki_answer = generate_translations(w_or_q)
        my_note = genanki.Note(model=model, fields=[anki_question, anki_answer])
        my_deck.add_note(my_note)
    anki_folder = './'
    anki_questions_file = anki_folder + f"anki_question{date}.apkg"
    genanki.Package(my_deck).write_to_file(anki_questions_file)


def get_model(deck_name):
    model_id = get_id()
    model = genanki.Model(
        model_id,
        deck_name,
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
        ]
    )
    return model

def get_id():
    return random.randrange(1 << 30, 1 << 31)

def get_titles(question): 
    next_line = '<br>'
    question_title = f"{question.get('questionTitle')}{next_line}" if question.get('questionTitle') else ''
    answer_title = f"{question.get('answerTitle')}{next_line}" if question.get('answerTitle') else ''
    return question_title, answer_title

def generate_simple_question(question):
    question_title, answer_title = get_titles(question)
    anki_question = to_base_template(f"{question_title}{question.get('question')}")
    anki_answer = to_base_template(f"{answer_title}{question.get('answer')}")
    return anki_question, anki_answer

def generate_hidden_word_in_sentence(question):
    question_title, answer_title = get_titles(question)
    anki_question = question.get('src')
    anki_answer = question.get('src')
    for i, q in enumerate(question.get('questions')):
        anki_question = anki_question.replace('{'+str(i)+'}', q)
        anki_answer = anki_answer.replace('{'+str(i)+'}', f"<mark>{question.get('answers')[i]}</mark>")
    anki_question = to_base_template(f'{question_title}{anki_question}')
    anki_answer = to_base_highlight_template(f'{answer_title}{anki_answer}')
    return anki_question, anki_answer

def generate_random_word(question):
    question_title, answer_title = get_titles(question)
    is_question = True if question.get('src').find('?') > -1 else False
    sentence_in_words = question.get('src').replace('?', '').split()
    random.shuffle(sentence_in_words)
    if is_question:
        sentence_in_words.append('?')
    anki_question = to_base_template(f"{question_title}{' / '.join(sentence_in_words)}")
    anki_answer = to_base_template(f"{answer_title}{question.get('src')}")
    return anki_question, anki_answer

def generate_translations(word):
    anki_question = to_base_template(word.get('translation'))
    anki_answer = to_base_template(word.get('original_value'))
    return anki_question, anki_answer
    
