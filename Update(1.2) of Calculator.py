from time import*
from tkinter import*
from tkinter.messagebox import*
from tkinter.simpledialog import*
from webbrowser import*



#Function for shivam studio website
def site():
    open_new_tab('https://shivam6662.w3spaces.com')

def owner():
    showinfo(title='Shiva+m Studio', message='This is a simple calculator\nimplemented in python\nDesigned by\nShiva+m Studio\nYou may visit our website\nhttps://shivam6662.w3spaces.com')        

		
def buttonClick(numbers):
	global operator
	operator=operator+str (numbers)
	text_Input.set (operator)
		
		
def button13clearDisplay():
	   global operator
	   operator
	   text_Input.set('')
	   
def button16EqualsInput():
	   global operator
	   sumup=str(eval(operator))
	   text_Input.set(sumup)
	   operator=''
	   
	   
root=Tk()
root.title('Shiva+m Studio  Calculator')
root.minsize(1050,1825)
root.maxsize(1100,1900)
operator=""
text_Input=StringVar()

#---------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------------#


root.configure(background="black")
root.resizable(0,0)
root.overrideredirect(1)
def start():
	a=strftime("%A\t%d||%m||%y\n%H:%M:%S %p")
	label.config(text=a)
	label.after(200,start)

label=Label(root,font=("arial",15,"bold"),bg="black",fg="green")
label.place(anchor=CENTER,x=535,y=100)
start()


#---------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------------#

	
	
txtDisplay=Entry (root,textvariable=text_Input,justify='right',bd=35,font=("arial",15,"bold"),width=20,bg="skyblue").place(anchor=CENTER,x=535,y=320)
	
	
button1 = Button(root, text=' 1 ', fg='black', bg='lightgreen',height=2,width=3,bd=3,font=("arial",15,"bold"),command=lambda:buttonClick (1))
button1.place(anchor=CENTER,x=155,y=550)
	
	
button2 = Button(root ,text=' 2 ', fg='black', bg='lightgreen',height=2,width=3,bd=3,font=("arial",15,"bold"),command=lambda:buttonClick(2))
button2.place(anchor=CENTER,x=405,y=550)
	
	
button3 =Button (root,text='3',fg='black',bg='lightgreen',height=2,width=3,bd=3,font=("arial",15,"bold"),command=lambda:buttonClick(3))
button3.place(anchor=CENTER,x=655,y=550)
	
	
button4= Button(root, text='+',fg='black',bg='orange',height=2,width=3,bd=3,font=("arial",15,"bold"),command=lambda:buttonClick('+'))
button4.place(anchor=CENTER,x=910,y=550)
	
	
button5 =Button (root,text='4',fg='black',bg='lightgreen',height=2,width=3,bd=3,font=("arial",15,"bold"),command=lambda:buttonClick(4))
button5.place(anchor=CENTER,x=155,y=800)
	
	
button6=Button (root,text='5',fg='black',bg='lightgreen',height=2,width=3,bd=3,font=("arial",15,"bold"),command=lambda:buttonClick(5))
button6.place(anchor=CENTER,x=405,y=800)
	
	
button7=Button (root,text='6',fg='black',bg='lightgreen',height=2,width=3,bd=3,font=("arial",15,"bold"),command=lambda:buttonClick(6))
button7.place(anchor=CENTER,x=655,y=800)
	
	
button8 = Button(root, text=' - ', fg='black', bg='orange',height=2,width=3,bd=3,font=("arial",15,"bold"),command=lambda:buttonClick('-'))
button8.place(anchor=CENTER,x=910,y=800)
	
	
button9=Button (root,text='7',fg='black',bg='lightgreen',height=2,width=3,bd=3,font=("arial",15,"bold"),command=lambda:buttonClick(7))
button9.place(anchor=CENTER,x=155,y=1050)
	
	
button10=Button (root,text='8',fg='black',bg='lightgreen',height=2,width=3,bd=3,font=("arial",15,"bold"),command=lambda:buttonClick(8))
button10.place(anchor=CENTER,x=405,y=1050)
	
	
button11=Button (root,text='9',fg='black',bg='lightgreen',height=2,width=3,bd=3,font=("arial",15,"bold"),command=lambda:buttonClick(9))
button11.place(anchor=CENTER,x=655,y=1050)
	
multiply1="×"
multiply2="*"
multiply1=multiply2
button12= Button(root, text=' × ', fg='black', bg='orange',height=2,width=3,bd=3,font=("arial",15,"bold"),command=lambda:buttonClick('*'))
button12.place(anchor=CENTER,x=910,y=1050)


button13=Button (root,text='C',fg='black',bg='orange',height=2,width=3,bd=3,font=("arial",15,"bold"),command=button13clearDisplay)
button13.place(anchor=CENTER,x=155,y=1300)
	
	
button14=Button (root,text='0',fg='black',bg="orange",height=2,width=3,bd=3,font=("arial",15,"bold"),command=lambda:buttonClick(0))
button14.place(anchor=CENTER,x=405,y=1300)
	
divide1="÷"
divide2="/"
divide1=divide2	
button15=Button (root,text='÷',fg='black',bg='orange',height=2,width=3,bd=3,font=("arial",15,"bold"),command=lambda:buttonClick('/'))
button15.place(anchor=CENTER,x=655,y=1300)
	
	
button16= Button(root, text='=', fg='black', bg='red',height=2,width=3,bd=3,font=("arial",15,"bold"),command=button16EqualsInput)
button16.place(anchor=CENTER,x=910,y=1300)
	

Owner=Button(root,text="Owner",bg="skyblue",fg="black",bd=5,font=('arail',10,'bold'), command=owner).place(anchor=CENTER,x=535,y=1500)
	
MOHIT=Button(root,text="SHIVA + M",bg="skyblue",fg="black",font=('arail',20,'bold'),bd=10, command=site).place(anchor=CENTER,x=535,y=1720)


	
root.mainloop()
	
