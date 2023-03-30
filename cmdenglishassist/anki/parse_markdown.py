import markdown


def parse_markdown_to_questions(markdown_lines):
    questions = []
    is_question_section = False
    is_answer_section = False
    question_start = '# (QS):'
    answer_start = '# (AS):'
    divider = '---'
    q = { 'question': '', 'answer': '' }
    for index, ml in enumerate(markdown_lines):
        if ml.startswith(question_start):
            is_answer_section = False
            is_question_section = True
        elif ml.startswith(answer_start):
            is_question_section = False
            is_answer_section = True
        elif ml.startswith(divider):
            is_question_section = False
            is_answer_section = False
            if q['question'] and q['answer']:
                append_question(questions, q)
                q = {'question': '', 'answer': ''}
        elif is_question_section:
            q['question'] += ml
        elif is_answer_section:
            q['answer'] += ml
        if index == len(markdown_lines) - 1 and q['question'] and q['answer']:
            append_question(questions, q)
    return questions


def append_question(questions, question):
    question_to_html_question(question)
    questions.append(question)
    

def question_to_html_question(question):
    question['question'] = markdown.markdown(question['question'], extensions=['tables'])
    question['answer'] = markdown.markdown(question['answer'], extensions=['tables'])
    return question

