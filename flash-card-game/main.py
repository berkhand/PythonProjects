from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
try:
    df = pandas.read_csv("data/dutch_words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/dutch_words.csv")

translations = df.to_dict(orient="records")  # {row.Dutch: row.English for (index, row) in df.iterrows()}
print(translations)
print(type(translations))
selection = {}
timer_id = None


def start_timer():
    global timer_id
    if timer_id is not None:
        window.after_cancel(timer_id)
    timer_id = window.after(3000, flip_card)


def get_random_word():
    global selection
    selection = random.choice(translations) #list(translations.items())
    canvas.itemconfig(img, image=card_front)
    canvas.itemconfig(text1, text="Dutch", fill="black")
    canvas.itemconfig(text2, text=selection["Dutch"], fill="black")
    start_timer()


def approve_pressed():
    translations.remove(selection)
    data = pandas.DataFrame(translations)
    data.to_csv("data/dutch_words_to_learn.csv", index=False)
    get_random_word()


def decline_pressed():
    get_random_word()


def flip_card():
    canvas.itemconfig(img, image=card_back)
    canvas.itemconfig(text1, text="English", fill="white")
    canvas.itemconfig(text2, text=selection["English"], fill="white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
img = canvas.create_image(400, 263, image=card_front)
text1 = canvas.create_text(400, 150, text="text1", font=("Ariel", 40, "italic"))
text2 = canvas.create_text(400, 263, text="text2", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)

img_right = PhotoImage(file="images/right.png")
button_right = Button(image=img_right, highlightthickness=0, command=approve_pressed)
button_right.grid(column=1, row=1)

img_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=img_wrong, highlightthickness=0, command=decline_pressed)
button_wrong.grid(column=0, row=1)

get_random_word()


window.mainloop()
