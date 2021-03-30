import tkinter as tk
import requests
import json
import pyautogui
import time
from random import seed
from random import randint

seed()

def minorSleep():
    return time.sleep(randint(2, 4))
 
def nap(): 
    return time.sleep(randint(3, 6))

def majorSleep():
    return time.sleep(randint(5, 10))


def click_on_random_profile():
    majorSleep()
    foundProfile = False
    while foundProfile == False:
        minorSleep()
        pyautogui.scroll(-100)
        if(str(pyautogui.locateCenterOnScreen('moreOptionsBtn.png')) != 'None'):
            a, b = pyautogui.locateCenterOnScreen('moreOptionsBtn.png')
            foundProfile = True
    nap()
    pyautogui.moveTo(a - 513, b)
    minorSleep()
    pyautogui.click()
    nap()
    if(str(pyautogui.locateCenterOnScreen('homeBtn.png')) == 'None'):
        pyautogui.moveTo(a - 513, b - 10)
        pyautogui.click()
    nap()


def click_on_image(imageName):
    majorSleep()
    if(str(pyautogui.locateCenterOnScreen(imageName)) == 'None'):
        print("Py did not find the image")
        return
    pyautogui.moveTo(pyautogui.locateCenterOnScreen(imageName))
    print('Image found')
    nap()
    pyautogui.click()
    majorSleep()


def go_to_page(webpage):

    nap()
    pyautogui.moveTo(250, 50)
    minorSleep()
    pyautogui.click()
    minorSleep()
    if 'https://' in webpage:
        minorSleep()
        pyautogui.write(webpage)
    else:
        pyautogui.write('https://' + webpage)
    minorSleep()
    pyautogui.press('enter')


def open_navigator():
    pyautogui.moveTo(660, 1050)
    minorSleep()
    pyautogui.click()
    majorSleep()


def go_to_profile():

    open_navigator()
    go_to_page('instagram.com')

    time.sleep(15)

    user_id = accountToFollow.get()

    minorSleep()

    pyautogui.moveTo(950, 130)

    minorSleep()
    pyautogui.click()
    pyautogui.write(user_id)
    minorSleep()
    pyautogui.press('enter')
    minorSleep()
    pyautogui.press('enter')

    x = quantityToFollow.get()
    x = int(x)
    click_on_followers(x)

    # Once on profile


def click_on_followers(num):

    minorSleep()
    pyautogui.moveTo(980, 250)
    minorSleep()
    pyautogui.click()
    majorSleep()
    i = 0
    while num > i:

        if str(pyautogui.locateCenterOnScreen('ok.png')) != 'None':
            minorSleep()
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('ok.png'))
            minorSleep()
            pyautogui.click()

        else:
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('followBtn.png'))
            minorSleep()
            pyautogui.click()
            majorSleep()
            pyautogui.scroll(-100)
            minorSleep()
            i = i + 1
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('close_followers_btn.png'))
    pyautogui.click()

def unfollow_people(answer):
    minorSleep()
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('profile.png'))
    minorSleep()
    pyautogui.click()
    minorSleep()
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('following_btn.png'))
    minorSleep()
    pyautogui.click()

def go_home():
    pyautogui.scroll(-100)
    click_on_image('homeBtn.png')
    minorSleep()
def like_image():
    click_on_image('likeBtn.png')

def likeImages():
    pyautogui.moveTo(randint(800, 1050), 500)
    pyautogui.click()
    pyautogui.click()
    nap()

    

def basic_activity():
    print('basic_activity: looking for home button')
    go_home()
    print('basic_activity: moving to random part of the screen out of the feed')
    pyautogui.moveTo(70, 400)
    minorSleep()
    pyautogui.click()
    minorSleep()
    i = 0
    print('basic_activity: loop initiated')
    while( i < 5 ) :
        nap()
        print('basic_activity: liking images', i)
        likeImages()
        majorSleep()
        pyautogui.scroll(randint(-1300, -700))
        nap()
        i = i + 1
        minorSleep()
def unfollow():

    unfollowNum = quantityToUnfollow.get()
    
    open_navigator()
    print('open navigator completed')
    nap()
    go_to_page('instagram.com/'+ usernameEntry.get())
    print('navigate to page completed')
    majorSleep()
    i = 0
    pyautogui.moveTo(1100, 240)
    nap()
    pyautogui.click()
    
    while i < int(unfollowNum):
        click_on_image("following.png")
        minorSleep()
        click_on_image("unfollow.png")
        minorSleep()
        pyautogui.scroll(-100)
        nap()
        i = i + 1


def worker():
    open_navigator()
    print('open navigator completed')
    nap()
    go_to_page('instagram.com')
    print('navigate to page completed')
    majorSleep()
    i = 0
     
    while i < 100:
        print('main loop began')
        basic_activity()
        print('basic activity done')
        minorSleep()
        click_on_random_profile()
        print('move to a new profile done')
        minorSleep()
        click_on_followers(randint(10, 20))
        print('click on new followers done')
        go_to_page('instagram.com')
        nap()
        pyautogui.moveTo(85, 50)
        minorSleep()
        pyautogui.click()
        i = i + 1

def authenticateUser():
    
    rPost = requests.post('https://limitless-fjord-99628.herokuapp.com/api/auth/login',
                          json={ 'email' : usernameEntry.get(), 'password' : passwordEntry.get() })
    
    if ("authToken" not in rPost.text):
        error = tk.Toplevel(loginScreen)
        error.title("Error")
        error.geometry("200x50")
        tk.Label(error, fg="red", text="Wrong credentials",  font="bold").pack()
        return
    automation()
      
def automation():
    mainScreen = tk.Toplevel(loginScreen)
    mainScreen.geometry("500x400")
    mainScreen.title("InstaAu")

    global accountToFollow
    global quantityToFollow
    global quantityToUnfollow


    tk.Label(mainScreen, text='Function one: Follow people', font='Helvetica 13 bold').pack()

    tk.Label(mainScreen, text= 'Enter account to follow:').pack(padx = 100, side=tk.TOP)
    accountToFollow = tk.Entry(mainScreen)
    accountToFollow.pack()

    tk.Label(mainScreen, text = 'Enter how many people to follow(number):').pack()
    quantityToFollow = tk.Entry(mainScreen)
    quantityToFollow.pack()
    
    tk.Label(mainScreen, text="").pack()
    
    tk.Button(mainScreen, text = "Follow", width= 18, command = go_to_profile).pack()

    tk.Label(mainScreen, text="").pack()

    tk.Label(mainScreen, text="").pack()
     
    #unfollow functionallity

    tk.Label(mainScreen, text='Function two: Unfopllow people', font='Helvetica 13 bold').pack()
    
    tk.Label(mainScreen, text = 'Enter how many people to unfollow(number):').pack()
    quantityToUnfollow = tk.Entry(mainScreen)
    quantityToUnfollow.pack()
    

    tk.Label(mainScreen, text="").pack()
    
    tk.Button(mainScreen, text = "Unfollow", width= 18, command = unfollow).pack()

def hello():
    print(accountToFollow.get())


global loginScreen

loginScreen = tk.Tk()
loginScreen.geometry("300x250")
loginScreen.title("Login")
tk.Label(loginScreen, text="InstaBot").pack()
tk.Label(loginScreen, text="").pack()

global auth_username
global auth_password


auth_username = tk.StringVar()
auth_password = tk.StringVar()

global usernameEntry
global passwordEntry


tk.Label(loginScreen, text = "Username", font=("Calibri", 13)).pack()
usernameEntry = tk.Entry( loginScreen, textvariable=auth_username)
usernameEntry.pack()

tk.Label(loginScreen, text = "Password", font=("Calibri", 13)).pack()
passwordEntry = tk.Entry( loginScreen, textvariable=auth_password, show="*")
passwordEntry.pack()
tk.Label(loginScreen, text="").pack()

tk.Button(text = "Login", command = authenticateUser).pack()
tk.Label(loginScreen, text="").pack()
tk.Label(loginScreen, text="").pack()

tk.Label(loginScreen, text = "Powered by The Root Haus", font=("Calibri", 8)).pack()

loginScreen.mainloop()

