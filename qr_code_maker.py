import os
import qrcode 
os.chdir('/storage/emulated/0')
data = 'https://shivam6662.w3spaces.com'
 
img = qrcode.make(data)
img.save('MyQRCode1.png')
