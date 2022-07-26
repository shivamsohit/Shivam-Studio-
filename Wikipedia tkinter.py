from tkinter import *
import wikipedia

def on_click():
  q = get_q.get()
  text.insert(INSERT, wikipedia.summary(q))

root = Tk()
question = Label(root, text="Question")
question.pack()
get_q = Entry(root, bd =5)
get_q.pack()
submit = Button(root,text='Submit',command=on_click)
submit.pack()
text = Text(root)
text.pack()

root.mainloop()
