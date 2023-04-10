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
        self.score_text = self.canvas.create_text(250, 10, text="Score: 0")
        self.canvas.create_rectangle(0, 50, 300, 300, fill="white")
        self.question_text = self.canvas.create_text(150, 150, text="1234567890123456789",
                                                     font=("Ariel", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=0, columnspan=2)

        img_true = PhotoImage(file="images/true.png")
        button_true = Button(image=img_true, highlightthickness=0, borderwidth=0)
        button_true.grid(column=0, row=1)

        img_false = PhotoImage(file="images/false.png")
        button_false = Button(image=img_false, highlightthickness=0, borderwidth=0)
        button_false.grid(column=1, row=1)

        self.update_question()

        self.window.mainloop()

    def update_question(self):
        self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())


# window = Tk()
# window.title("Flashy")
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
#
# canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
# card_front = PhotoImage(file="images/card_front.png")
# card_back = PhotoImage(file="images/card_back.png")
# img = canvas.create_image(400, 263, image=card_front)
# text1 = canvas.create_text(400, 150, text="text1", font=("Ariel", 40, "italic"))
# text2 = canvas.create_text(400, 263, text="text2", font=("Ariel", 60, "bold"), fill="black")
# canvas.grid(column=0, row=0, columnspan=2)
#
# img_right = PhotoImage(file="images/right.png")
# button_right = Button(image=img_right, highlightthickness=0, command=approve_pressed)
# button_right.grid(column=1, row=1)
#
# img_wrong = PhotoImage(file="images/wrong.png")
# button_wrong = Button(image=img_wrong, highlightthickness=0, command=decline_pressed)
# button_wrong.grid(column=0, row=1)


# def get_random_word():
#     global selection
#     selection = random.choice(translations) #list(translations.items())
#     canvas.itemconfig(img, image=card_front)
#     canvas.itemconfig(text1, text="Dutch", fill="black")
#     canvas.itemconfig(text2, text=selection["Dutch"], fill="black")
#     start_timer()
#
#
# def approve_pressed():
#     translations.remove(selection)
#     data = pandas.DataFrame(translations)
#     data.to_csv("data/dutch_words_to_learn.csv", index=False)
#     get_random_word()
#
#
# def decline_pressed():
#     get_random_word()
#
#
# def flip_card():
#     canvas.itemconfig(img, image=card_back)
#     canvas.itemconfig(text1, text="English", fill="white")
#     canvas.itemconfig(text2, text=selection["English"], fill="white")