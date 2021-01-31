import pyautogui as pt
from time import sleep
import pyperclip as srtct
from process import process_message

sleep(2)
positionGlobal = pt.locateOnScreen("Whatsapp/smiley.png", confidence=.6)
position = pt.position()
x = position[0]
y = position[1]

def get_message():
    global x,y
    position = pt.locateOnScreen("Whatsapp/smiley.png", confidence=.6)
    pt.moveTo(position,duration=.5)
    position = pt.position()
    x = position[0]
    y = position[1]
    pt.moveTo(x + 70,y - 70,duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(15,15)
    pt.click()
    wp_msg = srtct.paste()
    return wp_msg

def post_message(message):
    global x, y
    position = pt.position()
    x = position[0]
    y = position[1]
    pt.moveTo(x, y + 55, duration=.5)
    pt.click()
    pt.hotkey('ctrl', 'v')
    pt.typewrite('', interval=.5)
    pt.typewrite("\n", interval=.1)

def check_new_message():
    global x,y
    while True:
        if pt.locateOnScreen("Whatsapp/wp_open.png",confidence=.7) != None:
            try:
                position = pt.locateOnScreen("Whatsapp/new_message.png",confidence=.7)
                if position is not None:
                    pt.moveTo(position,duration=.5)
                    position = pt.position()
                    x = position[0]
                    y = position[1]
                    pt.moveTo(x - 100,y,duration=.5)
                    pt.click()
                    sleep(.5)
            except(Exception):
                print("no new message")

            try:
                x = 593
                y = 811

                if pt.pixelMatchesColor(x, y, (255 ,255 ,255), tolerance=10):
                    message = get_message()
                    post_message(process_message(message))
                else:
                    print("no new message")
                sleep(5)
            except Exception as e:
                print(e)
        else:
            if pt.locateOnScreen("Whatsapp/wp.png",confidence=.7) is not None:
                position = pt.locateOnScreen("Whatsapp/wp.png", confidence=.7)
                pt.moveTo(position, duration=.5)
                pt.click()
            sleep(5)

check_new_message()