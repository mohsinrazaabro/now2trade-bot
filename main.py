
import os
#Enter your email & password here

email = ""
password = ""

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "email.txt"
abs_file_path = os.path.join(script_dir, rel_path)
emailR = open(abs_file_path, 'r')
email = emailR.read()

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "password.txt"
abs_file_path = os.path.join(script_dir, rel_path)
passwordR = open(abs_file_path, 'r')
password = passwordR.read()



from cProfile import label
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from selenium.webdriver.common.by import By
import threading 
import sys
from selenium import webdriver
sys.setrecursionlimit(100000)




driver = webdriver.Chrome()
limit = 0
loop = False
run_thread = False
started = False
times = 0
refreshTime = time.time()

def login():
    global email
    global password
    time.sleep(4)
    
    getStartedBtn = driver.find_element(By.LINK_TEXT,'GET STARTED')
    getStartedBtn.click()
    time.sleep(1)
    emailInput = driver.find_element(By.CLASS_NAME,'userId')
    passwordInput = driver.find_element(By.CLASS_NAME,'passW')
    emailInput.send_keys(email)
    passwordInput.send_keys(password)
    time.sleep(1)
    checkBox = driver.find_element(By.CLASS_NAME,"checkbox")
    checkBox.click()
    loginBtn = driver.find_element(By.CLASS_NAME,"button")
    loginBtn.click()



def startThread():
    global run_thread;
    global started;
    ttk.Button(frm, text="Stop", command=stopThread, style = 'TButton'  ).grid(column=0, row=2)
    if started == False:
        started = True
        run_thread = True
        t1 = threading.Thread(target=moveToCenter)
        t1.start()
    else:
        run_thread = True
    print("Started automation")

def stopThread():
    global run_thread;
    run_thread = False
    print("Stopped automation")
    ttk.Button(frm, text="Automate", command=startThread, style = 'W.TButton').grid(column=0, row=2)

def runThread():
    global run_thread;
    run_thread = True
    print("Started automation")
    ttk.Button(frm, text="Stop", command=stopThread, style = 'TButton'  ).grid(column=0, row=2)

def moveToCenter():
    global run_thread;    
    global times
    global refreshTime
    try:
        while True:
            if time.time() > refreshTime+180:
                refreshTime = time.time()
                driver.get('https://now2trade.com/arbitrage/en/')
                time.sleep(15)
            getStarted = driver.find_element(By.CLASS_NAME,"exCh")
            getStarted.send_keys(Keys.ENTER)
            time.sleep(1)
            percentage = driver.find_element(By.CLASS_NAME,"ff_100")
            percentage.send_keys(Keys.ENTER)
            time.sleep(1)
            loop = True 
            startBtn = driver.find_element(By.CLASS_NAME,"startbutton")
            limit = float(limitText.get())
            while loop:
                USDT = driver.find_element(By.CLASS_NAME,"farq2")
                time.sleep(0.1)
                try:
                    newPrice = USDT.text.split(" ")
                    newPrice = float(newPrice[0])
                except:
                    newPrice = ''
                if run_thread:
                    if newPrice:
                        if newPrice > limit:
                            print(limit, newPrice)
                            startBtn.send_keys(Keys.ENTER)
                            loop = False
                            time.sleep(2)

    except:
        moveToCenter()
                
                        
               

        
        
        

        
        

driver.get("https://now2trade.com/")

login()

root = Tk()
style = Style()
style1 = Style()
style2 = Style()
style.theme_use('clam')
style1.theme_use('clam')
style2.theme_use('clam')

style1.configure('W.TButton', font =
               ('calibri', 14, 'bold', ),
                foreground = 'white',background = 'green')
style2.configure('TButton', font =
               ('calibri', 14, 'bold', ),
                foreground = 'white', background = 'red')

limitText = StringVar()
frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text=f"USDT limit threshold:", font=("Helvetica", 14)).grid(column=0, row=0)
limitEntry = ttk.Entry(frm, textvariable=limitText,  font = ('courier', 15, 'bold'), justify = CENTER).grid(column=0, row=1)
ttk.Button(frm, text="Automate", command=startThread, style = 'W.TButton').grid(column=0, row=2)
root.mainloop()






