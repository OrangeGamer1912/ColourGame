from tkinter import *
from ttkthemes import ThemedTk
import random


colours = ['red', 'orange', 'black', 'white', 'brown', 'yellow', 'blue', 'green', 'pink', 'purple',  'gray', ]
timeleft = 30
score = 0
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -=1
        lbl3.config(text="Time left:"+ str(timeleft))
        print("TimeLeft=" + str(timeleft))
        lbl3.after(1000,countdown)




def nextColour():
    print("Nextcolour activated")
    global score
    global timeleft
    if timeleft > 0:
        if txt.get().lower() == colours[1].lower():
            score += 1
            lbl2.config(text="Score: " + str(score))

            random.shuffle(colours)
            lbl4.config(fg=str(colours[1]), text=str(colours[0]))
            txt.delete(0, 'end')




def startGame(event):
    print("StartGame activated")
    if timeleft == 30:
        countdown()
    nextColour()
window = ThemedTk(theme="")
window.configure(themebg ="")
window.title("Game")

lbl = Label(window, text="Type in the colour of the words, and not the word text! (1st time write orange) ",font=("Helvetica", 10))
lbl.place(x=70, y= 0)

lbl2 = Label(window, text="Score: 0")
lbl2.place(x= 125, y = 50)

lbl3 = Label(window, text="Time left: Press enter")
lbl3.place(x= 125, y = 100)

lbl4 = Label(window, text="Orange", fg="red", font=("Helvetica", 30))
lbl4.place(x= 125, y = 150)

txt = Entry(window,width=20)
txt.place(x= 125, y = 200)

















window.geometry('550x300')
window.bind('<Return>', startGame)
window.mainloop()