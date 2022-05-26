from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
SCORE = 0


class QuizInterface:
    def __init__(self, quizz_brain: QuizBrain):
        self.quiz = quizz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score = Label(text=f"score: {SCORE}", fg="white", bg=THEME_COLOR, font=("Arial", 20, "italic"))
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125,
                                                width=280,
                                                font=("Arial", 20, "italic"),
                                                text="hello there", fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.right = PhotoImage(file="images/true.png")
        self.true = Button(image=self.right, command=self.true_pressed)
        self.true.config(bg=THEME_COLOR, highlightthickness=0)
        self.true.config(pady=20, padx=20)
        self.true.grid(column=0, row=2)

        self.wrong = PhotoImage(file="images/false.png")
        self.false = Button(image=self.wrong, command=self.false_pressed)
        self.false.config(bg=THEME_COLOR, highlightthickness=0)
        self.false.config(padx=20, pady=20)
        self.false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            global SCORE
            SCORE += 1
            self.score.config(text=f"score: {SCORE}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
