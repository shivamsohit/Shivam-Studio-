from tkinter import*
from tkinter.messagebox import*
from tkinter.simpledialog import*
import pickle
import os

os.chdir('/storage/emulated/0/Android/data/shiva+m authenticate')
os.system('clear')

user_details={}
user_details_list=[]
admin_details={}
admin_details['shiva+m']='shivani'
#pickle.dump(admin_details, open('admin.dat', 'ab'))


#Functions
def admin_authenticate():
       def authenticate ():
           id=id_value.get()
           password=password_value.get()
           if id in admin_details.keys():
               if password in admin_details[id]:
                   showinfo(title='Login', message='Welcome back\n Shivam\nLogin successfull !')      
                   admin_panel()                  
               else:
                   showerror(title='Error!', message='Id and password did not match!')    
           else:
               showerror(title='Error!', message='Id and password did not match!')
           
       authenticate_panel=Toplevel(root)
       authenticate_panel.title('Please enter id and password')
       authenticate_panel.minsize(750,600)
       authenticate_panel.maxsize(751,601)
       id_value=StringVar()
       password_value=StringVar()
       
       Label(authenticate_panel,text='Shiva+m Studio\nLogin Panel', font='arial 10 bold').grid(row=0, column=1,padx=0, pady=20)
       
       Label(authenticate_panel,text='Id :',).grid(row=1, column=0,padx=0, pady=20)       
       Label(authenticate_panel,text='Password :').grid(row=2, column=0,padx=0, pady=20)
       
       Entry(authenticate_panel,textvariable=id_value,show='*').grid(row=1, column=1,padx=0, pady=20)
       Entry(authenticate_panel,textvariable=password_value,show='*').grid(row=2, column=1,padx=0, pady=20)
       
       Button(authenticate_panel,text='Submit', font='arial 8 bold', command=authenticate).grid(row=3, column=1,padx=0, pady=20)
    


def user_authenticate():
       def authenticate ():
           id=id_value.get()
           password=password_value.get()
           if id in user_details.keys():
               if password in user_details[id]:
                   showinfo(title='Login', message=f'Welcome {id}\nLogin successfull !')      
                   user_panel()
               else:
                   showerror(title='Error!', message='Id and password did not match!')    
           else:
               showerror(title='Error!', message='Id and password did not match!')           

       authenticate_panel=Toplevel(root)
       authenticate_panel.title('Please enter id and password')
       authenticate_panel.minsize(750,600)
       authenticate_panel.maxsize(751,601)
       id_value=StringVar()
       password_value=StringVar()
       
       Label(authenticate_panel,text='User\nLogin Panel', font='arial 10 bold').grid(row=0, column=1,padx=0, pady=20)
       
       Label(authenticate_panel,text='Id :',).grid(row=1, column=0,padx=0, pady=20)       
       Label(authenticate_panel,text='Password :').grid(row=2, column=0,padx=0, pady=20)
       
       Entry(authenticate_panel,textvariable=id_value).grid(row=1, column=1,padx=0, pady=20)
       Entry(authenticate_panel,textvariable=password_value).grid(row=2, column=1,padx=0, pady=20)
       
       Button(authenticate_panel,text='Submit', font='arial 8 bold', command=authenticate).grid(row=3, column=1,padx=0, pady=20)
    

def create_user():
    #Functions under this function
    def append():
        name=name_value.get()
        surname=surname_value.get()
        phone=phone_value.get()
        password=create_password_value.get()
        id=name+surname
        
        user_details[id]=[name,surname,phone, password]   
        user_details_list.append([id,name,surname,password,phone])
        print(user_details)
        #Adding value in binary files
        pickle.dump(user_details_list, open('user.dat', 'wb'))
             
        
        showinfo(title='User created', message=f'Id : {id}\nPassword : {password}\nYou may login now.')
    
    
    create_user_panel=Toplevel(root)    
    create_user_panel.title('Create User')
    create_user_panel.minsize(750,600)
    create_user_panel.maxsize(751,601)
    #create_user_panel.configure(background='black')
    name_value=StringVar()
    surname_value=StringVar()
    phone_value=StringVar()
    create_password_value=StringVar()
    
    Label(create_user_panel,text='Create User', font='arial 8 bold').grid(row=0, column=1, padx=0, pady=10)
    Label(create_user_panel,text='Name :').grid(row=1, column=0, padx=0, pady=10)    
    Label(create_user_panel,text='Surname :').grid(row=2, column=0, padx=0, pady=10)
    Label(create_user_panel,text='Phone :').grid(row=3, column=0, padx=0, pady=10)
    Label(create_user_panel,text='Password :').grid(row=4, column=0, padx=0, pady=10)
    
    Entry(create_user_panel, textvariable=name_value).grid(row=1, column=1, padx=0, pady=20)
    Entry(create_user_panel, textvariable=surname_value).grid(row=2, column=1, padx=0, pady=20)
    Entry(create_user_panel, textvariable=phone_value).grid(row=3, column=1, padx=0, pady=20)
    Entry(create_user_panel, textvariable=create_password_value, show='*').grid(row=4, column=1, padx=0, pady=20)
    
    Button(create_user_panel, text='Submit Details', font='arial 8 bold', command=append).grid(row=5, column=1,padx=0, pady=10)

def show_users():
    admin_show_user=Toplevel(root)
    admin_show_user.title('Users...')
    admin_show_user.minsize(750,600)
    #admin_show_user.maxsize(750,600)
    a=user_details.keys()
    for i in a:
        d=user_details[i]
        u_name= pswd=d[0]
        s_name=d[1]
        p_number=d[2]
        pswd=d[3]
        Label(admin_show_user,text=f'User id : {i}\nPassword : {pswd}\nName : {u_name}\nSurname : {s_name}\nPhone no : {p_number}', font='arial 8 bold', bg='blue', pady=26).pack()

    
def admin_panel():
    admin_panel_window=Toplevel(root)
    admin_panel_window.title('Admin Panel !')
    admin_panel_window.minsize(750,600)
    Label(admin_panel_window,text='Shiva+m Studio').pack()
    Button(admin_panel_window,text='Show users', font='arail 8 bold', command=show_users).pack()
    #admin_panel_window.maxsize()

def user_panel():    
    user_panel_window=Toplevel(root)
    user_panel_window.title('User Panel !')
    user_panel_window.minsize(750,600)
    #user_panel_window.maxsize()
        


root=Tk()
root.minsize(1000,1600)
root.maxsize(751,601)
root.title('Shiva+m Studio Authenticate')

Button(text='User Login',bd=10, activebackground='red', command=user_authenticate).pack(side=TOP, pady=20)

Button(text='Admin Login',bd=10, activebackground='red', command=admin_authenticate).pack(side=TOP, pady=20)


Button(text='Create User',bd=10,activebackground='red', command=create_user).pack(side=TOP, pady=20)


#Adding value in binary files
pickle.dump(user_details_list, open('user.dat', 'wb'))

root.mainloop()