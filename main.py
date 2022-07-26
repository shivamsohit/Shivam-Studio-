from tkinter import*
from tkinter import filedialog
from pygame import mixer
from time import*
from random import*
from webbrowser import*
from os import*
import ctypes
import sys
#import androidhelper 
import time 

#Taking wake lock
#droid = androidhelper.Android() 
#droid.wakeLockAcquireFull() 


mixer.init()
root=Tk()
song_dict = {} # Empty dict to assign values to it
count = 0 # An idx number to it increase later

root.geometry("600x600+0+0")
root.configure(background='black')
root.title('SHIVA+M STUDIO Music_player')


#Adding code for digital clock
root.overrideredirect(1)
def start():
	a=strftime("%A\n%d||%m||%y\n%H:%M:%S %p")
	label.config(text=a)
	label.after(200,start)

label=Label(root,font=("arial",10,"bold"),bg="black",fg="yellow",)
label.place(anchor=CENTER,x=900,y=100)
start()


#---------------------------------------------------------------------------------------------------------------------------#


#Functions
def display_on():
    global root
    print("Always On")
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
    root.iconify()
    
def display_off():
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
    sys.exit(0)
    
    
def add_song():
    global count
    
    song_path = filedialog.askopenfilename(initialdir='/storage/emulated/0', title="Choose a song!",filetypes=(("mp3 Files", "*.mp3"), ))
    song_name = song_path.split("/")[-1].split(".mp3")[0]
    song_box.insert(END, song_name+'.mp3') # Insert just the song_name to the Listbox

    count += 1 # Increase the idx number 

def play():
    name=song_box.get(ACTIVE)
    for root2,firs,files in os.walk(path):
        for i in files:
            if '.mp3' in i:
                if name==i:
                    mixer.music.load(root2+'/'+i)
                    mixer.music.play()
                

            
def stop():
    mixer.music.stop()
    song_box.selection_clear(ACTIVE)       
    
def pause():
    mixer.music.pause()
    
def resume():
    mixer.music.unpause()                                                                
    
    

#Function for shivam studio website
def site():
    open_new_tab('https://shivam6662.w3spaces.com')
    
#Images of control buttons
#logo_img=PhotoImage(file='/storage/emulated/0/Python/Python_Files/Music_player/Images/logo.png')

play_btn_img=PhotoImage(file='/storage/emulated/0/Python/Python_Files/Music_player/Images/play50.png')      

pause_btn_img=PhotoImage(file='/storage/emulated/0/Python/Python_Files/Music_player/Images/pause50.png')      

forward_btn_img=PhotoImage(file='/storage/emulated/0/Python/Python_Files/Music_player/Images/forward50.png')        

backward_btn_img=PhotoImage(file='/storage/emulated/0/Python/Python_Files/Music_player/Images/backward50.png')      

stop_btn_img=PhotoImage(file='/storage/emulated/0/Python/Python_Files/Music_player/Images/stop50.png')      
    
#Buttons
b1=Button(root,text='SHIVA+M STUDIO',fg='black',bg='yellow',font=("arial",10,"bold"), activebackground='red',command=site)
b1.place(anchor=CENTER,x=300,y=100)  

#Add songs buttons
b2=Button(root,text='Add song',fg='black',bg='yellow',font=("arial",10,"bold"), activebackground='red', command=add_song)
b2.place(anchor=CENTER,x=226,y=268)  




#Control buttons
play_btn=Button(root,image=play_btn_img,borderwidth=10,bg='yellow',activebackground='red',width=100, height=100, command=play)
play_btn.place(anchor=CENTER,x=500,y=1350)


pause_btn=Button(root,image=pause_btn_img,borderwidth=10,bg='yellow',activebackground='red',width=100, height=100,command=pause)
pause_btn.place(anchor=CENTER,x=350,y=1350)

stop_btn=Button(root,image=stop_btn_img,borderwidth=10,bg='yellow',activebackground='red',width=100, height=100, command=stop)
stop_btn.place(anchor=CENTER,x=650,y=1350)

backward_btn=Button(root,image=backward_btn_img,borderwidth=10,bg='yellow',activebackground='red',width=100, height=100)
backward_btn.place(anchor=CENTER,x=200,y=1350)

forward_btn=Button(root,image=forward_btn_img,borderwidth=10,bg='yellow',activebackground='red',width=100, height=100,command=resume)
forward_btn.place(anchor=CENTER,x=800,y=1350)

#Screen always on button
screen_on_btn=Button(root,text='ON',borderwidth=10,bg='yellow',activebackground='red', command=display_on)
screen_on_btn.place(anchor=CENTER,x=350,y=1550)

screen_off_btn=Button(root,text='OFF',borderwidth=10,bg='yellow',activebackground='red', command=display_off)
screen_off_btn.place(anchor=CENTER,x=650,y=1550)



#Play list
song_box=Listbox(root,fg='black',bg='yellow',font=("arial",10,"bold"),height=14,width=30)
song_box.place(anchor=CENTER,x=540,y=800)

path='/storage/emulated/0/'
chdir(path)
for root2,firs,files in walk(path):
    for i in files:
        if '.mp3' in i:
            full_path=root2+'/'+i
            song_box.insert(END, i)
            
#if __name__='__main__':
root.mainloop()