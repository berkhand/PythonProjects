from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=350, highlightthickness=0, bg=THEME_COLOR)
        self.score_text = self.canvas.create_text(250, 10, text="Score: 0", fill="white")
        self.rect = self.canvas.create_rectangle(0, 50, 300, 300, fill="white")
        self.question_text = self.canvas.create_text(150, 150, text="question",
                                                     font=("Ariel", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=0, columnspan=2)

        img_true = PhotoImage(file="images/true.png")
        button_true = Button(image=img_true, highlightthickness=0, borderwidth=0, command=self.check_reply_true)
        button_true.grid(column=0, row=1)

        img_false = PhotoImage(file="images/false.png")
        button_false = Button(image=img_false, highlightthickness=0, borderwidth=0, command=self.check_reply_false)
        button_false.grid(column=1, row=1)

        self.update_question()
        self.is_last_question_graded = False

        self.window.mainloop()

    def update_question(self):
        self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())

    def check_reply_logic(self, reply: str):
        if self.quiz.still_has_questions() or (self.quiz.is_last_question() and not self.is_last_question_graded):
            if self.quiz.check_answer(reply):
                self.update_bg_green()
            else:
                self.update_bg_red()
            self.update_score(self.quiz.get_score())
        # if self.quiz.still_has_questions():
        #     self.update_question()

    def check_reply_true(self):
        self.check_reply_logic("True")

    def check_reply_false(self):
        self.check_reply_logic("False")

    def update_score(self, new_score):
        self.canvas.itemconfig(self.score_text, text=f"Score: {new_score}")
        if self.quiz.is_last_question():
            self.is_last_question_graded = True

    def update_bg_green(self):
        self.canvas.itemconfig(self.rect, fill="green")
        self.window.after(1000, self.update_bg_white)

    def update_bg_red(self):
        self.canvas.itemconfig(self.rect, fill="red")
        self.window.after(1000, self.update_bg_white)

    def update_bg_white(self):
        self.canvas.itemconfig(self.rect, fill="white")
        if self.quiz.still_has_questions():
            self.update_question()