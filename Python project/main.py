from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_bank = []
for q in question_data:
    question_text = q["question"]
    question_answer = q["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
quiz = Quiz(question_bank)

while quiz.still_has_question():
    quiz.next_question()



print("You have completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number + quiz.skipped_questions}")
