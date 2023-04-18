from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for thing in question_data[0]["results"]:
    obj = Question(q_text= thing["question"], q_answer= thing["correct_answer"])
    question_bank.append(obj)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("\n\n\nYou have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
