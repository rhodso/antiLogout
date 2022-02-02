import time
import os

def anyKey():
    input("Press enter to continue...")
    exit(0)

try:
    from pynput.keyboard import Key, Controller
except:
    os.system("pip install pynput")
    os.system("python antiLogout.py")
    anyKey()

#Startup
print("Started")

#Wait some seconds
time.sleep(10)
os.system("taskkill /IM teams.exe /F")
print("Killed teams lol")

keyboard = Controller()
while(True):
    try:
        print("Pressed")
        keyboard.tap(Key.f14)
        time.sleep(300)
    except:
        break
print("Stopped")
anyKey()
