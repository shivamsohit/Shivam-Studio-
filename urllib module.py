from urllib.request import*


#returns html or source code of given url
print(urlopen('https://mohitkhatak6662.wixsite.com/mohitkhatak').read())


#returns http status code where 200 means all okay, 301,302 means redirection happened.
print(urlopen('https://mohitkhatak6662.wixsite.com/mohitkhatak').getcode())


#stores metadata about opened url
print(urlopen('https://mohitkhatak6662.wixsite.com/mohitkhatak').headers)


#returns some information as stored by headers
print(urlopen('https://mohitkhatak6662.wixsite.com/mohitkhatak').info())


#returns url string
print(urlopen('https://mohitkhatak6662.wixsite.com/mohitkhatak').geturl())