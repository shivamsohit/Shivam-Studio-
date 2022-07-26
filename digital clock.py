from tkinter import*
from time import*
from random import*




root=Tk()
root.geometry("300x100+0+0")
root.configure(background="black")
root.resizable(0,0)
root.overrideredirect(1)
def start():
	a=strftime("%A\n%d||%m||%y\n%H:%M:%S %p")
	label.config(text=a)
	label.after(200,start)

label=Label(root,font=("arial",20,"bold"),bg="black",fg="green")
label.place(anchor=CENTER,x=535,y=920)
start()


#---------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------------#



l1=Button(root,text='SHIVA + M STUDIO',bd=0.5,height=1,width=20,fg="blue",bg="black",activebackground="red",activeforeground="black",font=("Arail",15,'bold')).place(anchor=CENTER,x=535,y=70)

l2=Button(root,text='SHIVA + M STUDIO',bd=0.5,height=1,width=20,fg="blue",bg="black",activebackground="indigo",activeforeground="black",font=("Arail",15,'bold')).place(anchor=CENTER,x=535,y=220)

l3=Button(root,text='SHIVA + M STUDIO',bd=0.5,height=1,width=20,fg="blue",bg="black",activebackground="yellow",activeforeground="black",font=("Arail",15,'bold')).place(anchor=CENTER,x=535,y=370)

l4=Button(root,text='SHIVA + M STUDIO',bd=0.5,height=1,width=20,fg="blue",bg="black",activebackground="green",activeforeground="black",font=("Arail",15,'bold')).place(anchor=CENTER,x=535,y=520)

l5=Button(root,text='SHIVA + M STUDIO',bd=0.5,height=1,width=20,fg="blue",bg="black",activebackground="blue",activeforeground="black",font=("Arail",15,'bold')).place(anchor=CENTER,x=535,y=670)


#---------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------------#




l2=Button(root,text='SHIVA + M STUDIO',bd=0.5,height=1,width=20,fg="blue",bg="black",activebackground="blue",activeforeground="black",font=("Arail",15,'bold')).place(anchor=CENTER,x=535,y=1189)

l2=Button(root,text='SHIVA + M STUDIO',bd=0.5,height=1,width=20,fg="blue",bg="black",activebackground="green",activeforeground="black",font=("Arail",15,'bold')).place(anchor=CENTER,x=535,y=1339)

l2=Button(root,text='SHIVA + M STUDIO',bd=0.5,height=1,width=20,fg="blue",bg="black",activebackground="yellow",activeforeground="black",font=("Arail",15,'bold')).place(anchor=CENTER,x=535,y=1489)

l2=Button(root,text='SHIVA + M STUDIO',bd=0.5,height=1,width=20,fg="blue",bg="black",activebackground="indigo",activeforeground="black",font=("Arail",15,'bold')).place(anchor=CENTER,x=535,y=1639)

l2=Button(root,text='SHIVA + M STUDIO',bd=0.5,height=1,width=20,fg="blue",bg="black",activebackground="red",activeforeground="black",font=("Arail",15,'bold')).place(anchor=CENTER,x=535,y=1789)


#---------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------------#


mainloop()
