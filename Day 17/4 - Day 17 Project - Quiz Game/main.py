from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# question_bank will be a list of question objects.
for data in question_data:
    question_bank.append(Question(question=data["text"], answer=data["answer"]))

quiz = QuizBrain(question_bank)

while quiz.stillHasQuestions():
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score is: {quiz.score}/{quiz.question_number}")