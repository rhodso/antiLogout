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

#Remvove excess copies of teams and chrome shortcuts that onedrive creates

#   //TODO

"""
Kill teams because it's a complete load of shit and nobody wants it.

Fucking seriously, Microsoft. Not content with ruining the fuck out
of computers everywhere with your bloated, buggy, garbage OS and 
invading the workspace with your fucking garbage release of whatever 
the latest version of office has to offer, now every man and his 
fucking dog has to use teams because isn't teams bloody brilliant.
I don't know of any person who activley enjoys using teams. 
If it were up to me, every acedemic institution would just 
give discord a bunch of fucking money and get them to build a fucking
discord for education or some shit that would be soooo much better
because these people actually know what they're doing
But OH NO I'm just a fucking lowley PhD student. My opinions are not
the concern of the fucking university higer-ups who are quite happy
to bend over and let microsoft fuck them over.

Fuck you microsoft
"""

#Kill teams
print("")
loopFlag = True

#Loop 60 times, counting down
for loopCount in range(60, -1, -1):

    #Kill teams and store the status in status, go figure
    status = os.system("taskkill /IM teams.exe /F")

    if(status == 0): #Teams was killed successfully
        print("\nKilled teams")
        loopFlag = False
        break
    elif(status == 128): #Teams isn't running
        print("\nTeams not running, continuing")
        loopFlag = False
        break
    else: #Other error, try again
        print("\rTeams could not be killed, trying again " + str(loopCount) + " more times: ", end="")
        time.sleep(1)

if(loopFlag): #If we couldn't kill teams after 60 attempts
    print("\nTried to kill teams 60 times, but teams is still running. Gave up trying to kill teams")

#Pressing keys
keypresses = 0
keyboard = Controller()
while(True):
    try:
        #Increment the current key count
        keypresses += 1
        keyboard.tap(Key.f14)
        print("\rPressed " + str(keypresses) + " time(s)", end="")

        #Sleep for a minute
        time.sleep(60)
    except:
        #On any exception just stop (This includes keyboardInterupt)
        break
print("\nStopped")
input("Press enter to continue...")
exit(0)
