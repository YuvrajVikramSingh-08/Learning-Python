class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.q_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.q_list[self.question_number]
        self.question_number += 1
        u_answer = input(f"{self.question_number} {current_question.text}. (True/False)?: ")
        self.check_answer(u_answer, current_question.answer)

    def check_answer(self, u_answer, correct_answer):
        if u_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Your answer is correct!")
        else:
            print("That's Wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current Score: {self.score}/{self.question_number}")
        print("\n")

    def still_has_question(self):
        total_question = len(self.q_list)
        return self.question_number < total_question