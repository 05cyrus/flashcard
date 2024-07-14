from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, card_flip)


def card_flip():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
canvas = Canvas(window, width=800, height=526)
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 270, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

flip_timer = window.after(3000, card_flip)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

wrong_icon_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_icon_img, bg=BACKGROUND_COLOR, borderwidth=0, command=next_card)
wrong_button.grid(row=1, column=0)
right_icon_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_icon_img, bg=BACKGROUND_COLOR, borderwidth=0, command=is_known)
right_button.grid(row=1, column=1)
next_card()
flip_timer = window.after(3000, card_flip)
window.mainloop()
