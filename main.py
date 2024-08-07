from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card={}
to_learn={}

try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/Spanish_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="Spanish",fill="black")
    canvas.itemconfig(card_word,text=current_card["Spanish"],fill="black")
    canvas.itemconfig(card_background, image=img)
    flip_timer=window.after(3000, func=flip)

def flip():
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=imgback)

def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

window=Tk()
window.title("Flash")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000, func=flip)

canvas=Canvas(width=800,height=526)
img=PhotoImage(file="images/card_front.png")
imgback=PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400,263,image=img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title=canvas.create_text(400,150,text="", font=("Arial",40,"italic"))
card_word=canvas.create_text(400,263,text="", font=("Arial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

known=PhotoImage(file="images/right.png")
known_but=Button(image=known,highlightthickness=0,command=is_known)
known_but.grid(row=1,column=0)

unknown=PhotoImage(file="images/wrong.png")
unknown_but=Button(image=unknown,highlightthickness=0,command=next_card)
unknown_but.grid(row=1,column=1)

next_card()

window.mainloop()