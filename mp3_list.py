import os
path='/storage/emulated/0/'
os.chdir(path)

for root,firs,files in os.walk(path):
    for i in files:
        if '.mp3' in i:
            full_path=root+'/'+i+'\n'
            
        
        