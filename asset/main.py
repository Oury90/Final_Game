from question import Question
from data import questions_data
from quiz_brain import QuizBrain
from ascii_table import ascii

question_bank = []

for question in questions_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    inco_answer = question["incorrect_answers"]
    new_question = Question(question_text, question_answer, inco_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

print(ascii)
while quiz.still_answer():
    quiz.get_question()

print(f"Your final score was: {quiz.score}/{quiz.question_number}")
