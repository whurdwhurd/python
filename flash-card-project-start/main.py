BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import random
import pandas as pd

try:
    fr_words = pd.read_csv("/Users/willhurd/Downloads/flash-card-project-start/words_to_learn.csv.csv")
except:
    fr_words = pd.read_csv("/Users/willhurd/Downloads/flash-card-project-start/data/french_words.csv")
fr_words1 = fr_words.to_dict(orient="records")
starting_card = random.choice(fr_words1)
curr_card = {}

def new_word():
    canvas.itemconfig(canvas_image, image=frontlogo_img)
    current_card = random.choice(fr_words1)
    forlang_label.config(text="French", bg='#ffffff')
    forword_label.config(text=current_card["French"], bg='#ffffff')
    curr_card.update(current_card)
    window.after(3000, flip)

def flip():
    canvas.itemconfig(canvas_image, image=backlogo_img)
    forlang_label.config(text="English", bg='#91c2af')
    forword_label.config(text=curr_card["English"], bg='#91c2af')

def got_it():
    new_word()
    fr_words1.remove(curr_card)
    df = pd.DataFrame(fr_words1)
    df.to_csv('words_to_learn.csv')

def missed_it():
    new_word()

window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

canvas=Canvas(width=800,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
frontlogo_img=PhotoImage(file="/Users/willhurd/Downloads/flash-card-project-start/images/card_front.png")
backlogo_img=PhotoImage(file="/Users/willhurd/Downloads/flash-card-project-start/images/card_back.png")
canvas_image = canvas.create_image(400,263,image=frontlogo_img)
canvas.grid(row=1,column=1,columnspan=2)

forlang_label=Label(bg="#ffffff", fg="#000000", font=("ariel", 40, "italic"))
forlang_label.place(relx=.5, rely=.25, anchor="center")

forword_label=Label(bg="#ffffff", fg="#000000", font=("ariel", 60, "bold"))
forword_label.place(relx=.5, rely=.45, anchor="center")

right_img = PhotoImage(file="/Users/willhurd/Downloads/flash-card-project-start/images/right.png")
right_button = Button(image=right_img, height=95, width=95, highlightthickness=0, command=got_it)
right_button.config(borderwidth=0)
right_button.grid(row=2, column=1)

wrong_img = PhotoImage(file="/Users/willhurd/Downloads/flash-card-project-start/images/wrong.png")
wrong_button = Button(image=wrong_img, height=90, width=90, highlightthickness=0, command=missed_it)
wrong_button.grid(row=2, column=2)

new_word()

window.mainloop()