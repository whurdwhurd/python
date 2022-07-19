BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import random
import pandas as pd

class Gui():
    def __init__(self):
        #background GUI
        self.canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.frontlogo_img = PhotoImage(file="/Users/willhurd/Downloads/flash-card-project-start/images/card_front.png")
        self.backlogo_img = PhotoImage(file="/Users/willhurd/Downloads/flash-card-project-start/images/card_back.png")
        self.canvas_image = self.canvas.create_image(400, 263, image=self.frontlogo_img)
        self.canvas.grid(row=1, column=1, columnspan=2)

        #label for language
        self.forlang_label = Label(bg="#ffffff", fg="#000000", font=("ariel", 40, "italic"))
        self.forlang_label.place(relx=.5, rely=.25, anchor="center")

        #label for word
        self.forword_label = Label(bg="#ffffff", fg="#000000", font=("ariel", 60, "bold"))
        self.forword_label.place(relx=.5, rely=.45, anchor="center")

        #button for known answer
        self.right_img = PhotoImage(file="/Users/willhurd/Downloads/flash-card-project-start/images/right.png")
        self.right_button = Button(image=self.right_img, height=95, width=95, highlightthickness=0, command=self.got_it)
        self.right_button.config(borderwidth=0)
        self.right_button.grid(row=2, column=1)

        #button for unknown answer
        self.wrong_img = PhotoImage(file="/Users/willhurd/Downloads/flash-card-project-start/images/wrong.png")
        self.wrong_button = Button(image=self.wrong_img, height=90, width=90, highlightthickness=0, command=self.missed_it)
        self.wrong_button.grid(row=2, column=2)

        #generate text
        current_card = random.choice(fr_words1)
        self.forlang_label.config(text="French", bg='#ffffff')
        self.forword_label.config(text=current_card["French"], bg='#ffffff')
        curr_card.update(current_card)
        window.after(3000, self.flip)

    def new_word(self):
        self.canvas.itemconfig(self.canvas_image, image=self.frontlogo_img)
        current_card = random.choice(fr_words1)
        self.forlang_label.config(text="French", bg='#ffffff')
        self.forword_label.config(text=current_card["French"], bg='#ffffff')
        curr_card.update(current_card)
        window.after(3000, self.flip)

    def flip(self):
        self.canvas.itemconfig(self.canvas_image, image=self.backlogo_img)
        self.forlang_label.config(text="English", bg='#91c2af')
        self.forword_label.config(text=curr_card["English"], bg='#91c2af')

    def got_it(self):
        self.new_word()
        fr_words1.remove(curr_card)
        df = pd.DataFrame(fr_words1)
        df.to_csv('words_to_learn.csv')

    def missed_it(self):
        self.new_word()

try:
    fr_words = pd.read_csv("/Users/willhurd/Downloads/flash-card-project-start/words_to_learn.csv.csv")
except:
    fr_words = pd.read_csv("/Users/willhurd/Downloads/flash-card-project-start/data/french_words.csv")
fr_words1 = fr_words.to_dict(orient="records")
starting_card = random.choice(fr_words1)
curr_card = {}

window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

start = Gui()


window.mainloop()