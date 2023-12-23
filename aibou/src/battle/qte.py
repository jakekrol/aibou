#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# external
import rich
import keyboard
from rich.padding import Padding
from rich.align import Align
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# std
from time import sleep
import random 
import string
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
random.seed=0

class Event():
    def __init__(self):
        # default values are for failure
        self.result = 0
        self.feedback = 'X'
        # updated by success()

def randomcharacter():
    ''' Returns a random a-z or 0-9 character. '''
    return random.choice(string.ascii_lowercase + string.digits)

def success(char):
    print(f'success {char} was pressed')
    keyboard.remove_hotkey(char) # prevent new success calls
    event.result += 1
    event.feedback = u'\u2713'

def fail(char):
    print('fail')
    checkcharacter(char, callback=False)

def addhotkey(char):
    keyboard.add_hotkey(char, success, args=[char])

def removehotkey(char):
    keyboard.remove_hotkey(char)

def checkcharacter(char, time):
    global event
    event = Event()
    addhotkey(char)
    sleep(time)
    # handle removing key only when success() wasn't called (failed qte)
    try:
        removehotkey(char)
    except KeyError: 
        pass
    return event.result, event.feedback

def runevent(char, time):
    result, feedback = checkcharacter(char, time)
    return result, feedback

    

