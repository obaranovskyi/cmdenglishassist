# def read_markdown(file):
#     questions = []
#     is_question_section = False
#     is_answer_section = False
#     question_start = '# (QS):'
#     answer_start = '# (AS)'
#     divider = '---'
#
#     try:
#         with open(file, 'r') as markdown_file:
#             markdown_lines = markdown_file.readlines()
#             q = { 'question': '', 'answer': '' }
#             for index, ml in enumerate(markdown_lines):
#                 if ml.startswith(question_start):
#                     is_answer_section = False
#                     is_question_section = True
#                 elif ml.startswith(answer_start):
#                     is_question_section = False
#                     is_answer_section = True
#                 elif ml.startswith(divider):
#                     is_question_section = False
#                     is_answer_section = False
#                     if q['question'] and q['answer']:
#                         questions.append(q)
#                         q = { 'question': '', 'answer': '' }
#                 elif is_question_section:
#                     q['question'] += ml
#                 elif is_answer_section:
#                     q['answer'] += ml
#                 if index == len(markdown_lines) - 1 and q['question'] and q['answer']:
#                     questions.append(q)
#             return questions
#     except Exception as e:
#         print(e)
 
 
def read_markdown_lines(file):
    try:
        with open(file, 'r') as markdown_file:
            markdown_lines = markdown_file.readlines()
            return markdown_lines
    except Exception as e:
        print(e)


