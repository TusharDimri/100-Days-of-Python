from cgitb import text
from tkinter import * 
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.window =  Tk()
        self.window.title("Quizzler ")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.quiz = quiz_brain

        # Score
        self.score = Label(text=f"Score: 0", background=THEME_COLOR, fg="white", font=("arial", 10, "bold"))
        self.score.grid(column=1, row=0)

        # Canvas/Question:
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # Question:
        self.question_text = self.canvas.create_text(150, 125, text="", fill=THEME_COLOR, font=("arial", 20, "italic"), width=280)

        # Buttons(True and False):
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=self.true_image, highlightthickness=0, relief="flat" ,bd=0, command=lambda answer="True":self.checkAnswer(answer))
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=self.false_image, highlightthickness=0, relief="flat", bd=0, command=lambda answer="False":self.checkAnswer(answer))
        self.false_button.grid(row=2, column=1)

        self.getNextQuestion()

        self.window.mainloop()

    def getNextQuestion(self):
        self.canvas.configure(bg='white')
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=question)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def checkAnswer(self, answer):
        check = self.quiz.check_answer(answer)
        if check:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")

        self.window.after(1000, self.getNextQuestion)