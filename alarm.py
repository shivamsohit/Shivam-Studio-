import androidhelper 
import time 
droid = androidhelper.Android() 
droid.wakeLockAcquireFull() 
arrived = 0 
while True: 
    t = time.strftime("%I:%M %p") 
    if t == "10:27 PM": 
        print ('Time arrived') 
        droid.phoneCallNumber("8950097115") 
        print('calling') 
        t_end = time.time() + 60 
        while time.time() < t_end: 
            arrived = 1 
            print('talking') 
            droid.ttsSpeak("Hi Shivam, please wake up") 
            time.sleep(4)     
        if arrived == 1: 
            exit(0) 
    print('Time not arrived') 
    time.sleep(20) 


