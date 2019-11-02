from datetime import datetime
import webbrowser, os, random, subprocess

helloIntent = ["hi", "hello", "namaste", "hola"]
timeIntent = ["time please", "what's the current time", "what's the time now"]
dateIntent = ["date please", "what's the date today", "can you tell me the date"]
songIntent = ["play some song", "play a bollywood song", "play a random song for me"]

while True:
    message = input("Enter your message: ")

    if message in helloIntent:
        print("hello")
    elif message in timeIntent:
        now = datetime.now()
        print(now.strftime( "%a %d %b %H:%M:%S %p" ))
    elif message in dateIntent:
        today = datetime.today()
        print(f"{today.day}/{today.month}/{today.year}" )
    elif message.startswith("open"):
        website = message.partition(' ')[-1]
        webbrowser.open("https://" + website + ".com")
    elif message.startswith("run"):
        appName = message.partition(' ')[-1]
        subprocess.call( [ 'open' , '/Applications/' + appName + '.app' ] )
    elif message in songIntent:
        print('''
        1. Play some random song
        2. Show me the list of songs''')
        os.chdir('/Users/anmolrajarora/Documents/python-wknd-sep' )
        choice = int(input( "Enter your choice: " ))
        songs = os.listdir( )
        if choice == 1:
            song = random.choice( songs )
            subprocess.call( [ 'open' , song ] )
        elif choice == 2:
            for i in range(len(songs)):
                print(f"{i+1}. {songs[i]}")
            songNo = int(input("Which one do you want to play: "))
            subprocess.call( [ 'open' , songs[songNo - 1] ] )
    elif message == "bye":
        print("See you soon!")
        quit()
    else:
        print("I don't understand. ")


'''Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> datetime.datetime
<class 'datetime.datetime'>
>>> datetime
<module 'datetime' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/datetime.py'>
>>> datetime.datetime.today()
datetime.datetime(2019, 11, 2, 11, 44, 24, 51973)
>>> print(datetime.datetime.today())
2019-11-02 11:44:44.924723
>>> today = datetime.datetime.today()
>>> today.year
2019
>>> today.month
11
>>> today.date
<built-in method date of datetime.datetime object at 0x104e81580>
>>> today.date()
datetime.date(2019, 11, 2)
>>> today.day
2
>>> print(f"{today.day} / {today.month} / {today.year}")
2 / 11 / 2019
>>> print(f"{today.day}/{today.month}/{today.year}")
2/11/2019
>>> from datetime import datetime
>>> datetime
<class 'datetime.datetime'>
>>> from datetime.datetime import today
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    from datetime.datetime import today
ModuleNotFoundError: No module named 'datetime.datetime'; 'datetime' is not a package
>>> from datetime import datetime.today
SyntaxError: invalid syntax
>>> from datetime import datetime
>>> datetime.today()
datetime.datetime(2019, 11, 2, 11, 48, 28, 957144)
>>> datetime.now()
datetime.datetime(2019, 11, 2, 11, 51, 9, 717320)
>>> now = datetime.now()
>>> now
datetime.datetime(2019, 11, 2, 11, 51, 23, 890796)
>>> now.strftime("%y")
'19'
>>> now.strftime("%Y")
'2019'
>>> now.strftime("%m")
'11'
>>> now.strftime("%M")
'51'
>>> now.strftime("%s")
'1572675683'
>>> now.strftime("%S")
'23'
>>> now.strftime("%h")
'Nov'
>>> now.strftime("%H")
'11'
>>> now.strftime("%a")
'Sat'
>>> now.strftime("%A")
'Saturday'
>>> now.strftime("%b")
'Nov'
>>> now.strftime("%B")
'November'
>>> now.strftime("%c")
'Sat Nov  2 11:51:23 2019'
>>> 
>>> now.strftime("%d")
'02'
>>> now.strftime("%D")
'11/02/19'
>>> now.strftime("%a %d %b %H:%M:%S %p")
'Sat 02 Nov 11:51:23 AM'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> msg = "open google"
>>> msg.partition(' ')
('open', ' ', 'google')
>>> msg.partition(' ')[-1]
'google'
>>> url = "https://" + msg.partition(' ')[-1] +".com"
>>> url
'https://google.com'
>>> msg = "open facebook"
>>> url = "https://" + msg.partition(' ')[-1] +".com"
>>> url
'https://facebook.com'
>>> 
>>> 
>>> 
>>> import os
>>> import subprocess
>>> os.getcwd()   #get current working directory
'/Users/anmolrajarora/Documents'
>>> os.path.extend('/python')
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    os.path.extend('/python')
AttributeError: module 'posixpath' has no attribute 'extend'
>>> 
>>> os.chdir('/Users/anmolrajarora/Documents/python')
>>> os.getcwd()
'/Users/anmolrajarora/Documents/python'
>>> os.listdir()
['01-PythonIntroduction.wmv', 'PythonPygame_2.wmv', '.DS_Store', 'PythonPygame_!.wmv', '01-Python.wmv', 'PythonFunctionsIntro_1.wmv', 'PythonFunctions_2.wmv', 'PythonFilterMapLambda.wmv', 'PythonFunctionsIntro.wmv', 'Crawling_2.wmv', 'PythonIfElse.wmv', 'Crawling_1.wmv', 'Python_IfElse+List.wmv']
>>> import random
>>> songs = os.listdir()
>>> songs
['01-PythonIntroduction.wmv', 'PythonPygame_2.wmv', '.DS_Store', 'PythonPygame_!.wmv', '01-Python.wmv', 'PythonFunctionsIntro_1.wmv', 'PythonFunctions_2.wmv', 'PythonFilterMapLambda.wmv', 'PythonFunctionsIntro.wmv', 'Crawling_2.wmv', 'PythonIfElse.wmv', 'Crawling_1.wmv', 'Python_IfElse+List.wmv']
>>> song = random.choice(songs)
>>> song
'PythonFilterMapLambda.wmv'
>>> song = random.choice(songs)
>>> song
'PythonFunctionsIntro.wmv'
>>> subprocess.call(['open', song])
0
>>> os.chdir('/Users/anmolrajarora/Documents')
>>> os.chdir('python')
>>> os.getcwd()
'/Users/anmolrajarora/Documents/python'
>>> 
>>> 
>>> msg = "run google chrome"
>>> msg.partition(' ')
('run', ' ', 'google chrome')
>>> msg.partition(' ')[-1]
'google chrome'
>>> '''
