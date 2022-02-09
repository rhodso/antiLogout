#Import from standard library
import time
import os

#Import pynput, but if it fails, pip install it and restart script
try:
    from pynput.keyboard import Key, Controller
except:
    os.system("pip install pynput")
    os.system("python antiLogout.py")
    exit(0)

#Startup
print("Started")

print("")
loopFlag = True
for loopCount in range(60, -1, -1):
    status = os.system("taskkill /IM teams.exe /F")
    if(status == 0):
        print("\nKilled teams")
        loopFlag = False
        break
    elif(status == 128):
        print("\nTeams not running, continuing")
        loopFlag = False
        break
    else:
        print("\rTeams could not be killed, trying again " + str(loopCount) + " more times: ", end="")
        time.sleep(1)

if(loopFlag):
    print("\nTried to kill teams 60 times, but teams is still running. Gave up trying to kill teams")

keypresses = 0
keyboard = Controller()
while(True):
    try:
        keypresses += 1
        print("\rPressed " + str(keypresses) + " time(s)", end="")
        keyboard.tap(Key.f14)
        time.sleep(60)
    except:
        break
print("\nStopped")
input("Press enter to continue...")
exit(0)
