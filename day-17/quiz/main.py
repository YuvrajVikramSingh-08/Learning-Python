from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    q_text = i["text"]
    q_answer = i["answer"]
    new_question = Question(q_text=q_text, q_answer=q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final Score was {quiz.score}/{quiz.question_number}")