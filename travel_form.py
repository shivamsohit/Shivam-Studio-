import os 
from fpdf import FPDF
from tkinter import*
from tkinter.messagebox import*
from tkinter.simpledialog import*
#chdir('/storage/emulated/0')

a=os.path.exists('/storage/emulated/0/Android/data/shiva+m_transport')

if a==False:
    os.mkdir('/storage/emulated/0/Android/data/shiva+m_transport')
    print('Shiva+m_transport folder created Successfully!')
    
else:
    print('Shiva+m_transport folder exists Already!')




def submit():    
    sure=askyesno(title='Submit!', message='Are you sure to submit details!')
    
    #Making pdf objects
    pdf=FPDF('P','cm','A4')
    pdf.add_page()
    pdf.set_font('courier', 'B', 16)
    pdf.set_text_color(30,144,255)
    
    if sure==True:
           #Creating variables for values
           name='Name : '+name_value.get()
           age='Age : '+age_value.get()
           gender='Gender : '+gender_value.get()
           phone='Phone no : '+phone_value.get()
           aadhar='Aadhar no : '+aadhar_value.get()
           adress='Adress : '+adress_value.get() 
                           
                                                         
           if check.get()==1:
                txt=open('/storage/emulated/0/Android/data/shiva+m_transport/travel_forms_fast.txt', 'a')
                txt.write(f'\n\n-------------Travel form----------\nName : {name_value.get()}\nAge : {age_value.get()}\nGender : {gender_value.get()}\nPhone no : {phone_value.get()}\nAadhar no : {aadhar_value.get()}\nAdress : {adress_value.get()}\nMode of booking : Fast\n\n')
                txt.close()                
                                
                #Adding same details in pdf
                pdf.cell(0,1,'--------------------Travel form-------------------------' , ln=True)
                pdf.cell(0,1,name,ln=True)
                pdf.cell(0,1,age,ln=True)
                pdf.cell(0,1,gender,ln=True)
                pdf.cell(0,1,phone,ln=True)
                pdf.cell(0,1,aadhar,ln=True)
                pdf.cell(0,1,adress,ln=True)
                pdf.cell(0,1,'Mode of booking : Fast',ln=True)
                pdf.output('/storage/emulated/0/Android/data/shiva+m_transport/travel_forms_fast.pdf')
            
           elif check.get()==0:
                txt=open('/storage/emulated/0/Android/data/shiva+m_transport/travel_forms_normal.txt', 'a')
                txt.write(f'\n\n-------------Travel form----------\nName : {name_value.get()}\nAge :{age_value.get()}\nGender : {gender_value.get()}\nPhone no : {phone_value.get()}\nAadhar no : {aadhar_value.get()}\nAdress : {adress_value.get()}\nMode of booking :Normal\n\n')
                txt.close()
                
                #Adding same details in pdf
                pdf.cell(0,1,'--------------------Travel form-------------------------' , ln=True)
                pdf.cell(0,1,name,ln=True)
                pdf.cell(0,1,age,ln=True)
                pdf.cell(0,1,gender,ln=True)
                pdf.cell(0,1,phone,ln=True)
                pdf.cell(0,1,aadhar,ln=True)
                pdf.cell(0,1,adress,ln=True)
                pdf.cell(0,1,'Mode of booking : Normal',ln=True)
                pdf.output('/storage/emulated/0/Android/data/shiva+m_transport/travel_forms_normal.pdf')
                
           else:
                showerror(title='Error!', message='We are soory to say,\nbut some error has occurred')
                
                
           print('Details appended successfully')    
            
           name_value.set('')
           age_value.set('')
           gender_value.set('')
           phone_value.set('')
           aadhar_value.set('')
           adress_value.set('')
           check.set(0)
           print('Page details cleared')
            
           #Showing that details submitted
           submitted=showinfo(title='Submitted', message='Your details has been submitted, we will \ncontact you as soon as possible.\n Thanks for choosing our service.')    
             

def reset():
    name_value.set('')
    age_value.set('')
    gender_value.set('')
    phone_value.set('')
    aadhar_value.set('')
    adress_value.set('')
    check.set(0)
    
                                                                                
    

root=Tk()

open_app=askyesno(title='Shiva+m Travels', message='Welcome to Shiva+m Travels\nAre you sure to continue.')

if open_app==False:
    root.self.destroy()



Label(root,text='Shiva+m Travels', font='arial 10 bold').grid(padx=10,pady=20,row=0, column=1)


name_value=StringVar()
age_value=StringVar()
gender_value=StringVar()
phone_value=StringVar()
aadhar_value=StringVar()
adress_value=StringVar()
check=IntVar()



#Labels
name_label=Label(root,text='Name :').grid(row=1, column=0, padx=10, pady=10)

age_label=Label(root,text='Age :').grid(row=2, column=0, padx=10, pady=10)

gender_label=Label(root,text='Gender :').grid(row=3, column=0, padx=10, pady=10)

phone_label=Label(root,text='Phone no :').grid(row=4, column=0, padx=10, pady=10)

aadhar_label=Label(root,text='Aadhar no :').grid(row=5, column=0, padx=10, pady=10)

adress_label=Label(root,text='Adress :').grid(row=6, column=0, padx=10, pady=10)

#Entry
name_entry=Entry(root,textvariable=name_value ,
).grid(row=1, column=1, padx=0, pady=0)

age_entry=Entry(root,textvariable=age_value ,
).grid(row=2, column=1, padx=0, pady=0)

gender_entry=Entry(root,textvariable=gender_value ,
).grid(row=3, column=1, padx=0, pady=0)

phone_entry=Entry(root,textvariable=phone_value ,
).grid(row=4, column=1, padx=0, pady=0)

aadhar_entry=Entry(root,textvariable=aadhar_value ,
).grid(row=5, column=1, padx=0, pady=0)

adress_entry=Entry(root,textvariable=adress_value ,
).grid(row=6, column=1, padx=0, pady=0)

fast_book=Checkbutton(text='Want to book in a fast mode', variable=check).grid(row=7, column=1, padx=0, pady=0)


#Making frame for submit and reset buttons
#btn_frame=Frame(root, bg='red').grid(row=8, column=0, padx=0, pady=0)

#Adding reset buttons using a loop
reset_btn=Button(root,text='Reset', font='arial 10 bold', command=reset).grid(row=8, column=1,padx=0,pady=0)

#Adding submit button
submit_btn=Button(root,text='SUBMIT', font='arial 10 bold', command=submit).grid(row=9, column=1, padx=0, pady=20)



root.mainloop()