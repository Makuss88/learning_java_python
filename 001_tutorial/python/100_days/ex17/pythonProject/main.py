from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(text=question_text, answer=question_answer)
    questions_bank.append(new_question)

quiz = QuizBrain(questions_bank)

while quiz.still_has_question():
    quiz.next_question()

print('end quiz')
print(f'you have {quiz.score}/{len(questions_bank)}')