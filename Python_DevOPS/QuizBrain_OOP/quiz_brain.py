class QuizBrain:

    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        return False

    def check_answer(self, u_input, corr_answer):
        if u_input.lower() == corr_answer.lower():
            self.score +=1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer is: {corr_answer}")
        print(f"Your current score: {self.score}/{self.question_number}")

    def next_question(self):
        ques = self.question_list[self.question_number].text
        corr_ans = self.question_list[self.question_number].answer
        self.question_number +=1
        user_input = input(f"Q.{self.question_number}: {ques} (True/False)? ")
        self.check_answer(user_input, corr_ans)
