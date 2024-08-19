# Create a class called QuizBrain
# Write an __init__() method
# Initialize teh question_number to 0
# Initialize the question_list to an input
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{current_question}: {current_question.question} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("You got it wrong.")
        print(f"The corect answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")
