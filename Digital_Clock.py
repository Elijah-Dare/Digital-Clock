"""Digital Clock by Ai sweigart modified by Agbolade Elijah
Displays a digital clock of the current time with a seven-segment display. Press ctrl + c to stop.
Requires sevseg.py to be in the same folder

Tags: tiny, artistic"""

import sys, time
import sevseg # imports our sevseg.py program

try:
    while True: # Main program loop
        # clear the screen by printing several newlines:
        print('\n' * 60)
        
        # Get the current time from the computer's clock:
        currentTime = time.localtime()
        # % 12 so we use a 12 hour clock, not 24:
        hours = str(currentTime.tm_hour %  12)
        if hours == '0':
            hours = '12' # 12 - hour clock show 12:00, not 00:00
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)
        
        # Get the digit strings fromm the sevseg module:
        # 1 - For Hours
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()
        
        # 2 - For Minutes
        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()
        
        # 3 - For Seconds
        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()
        
        # Display the digits
        print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow) 
        print()
        print('Press Ctrl-C to quit')
        
        # keep looping until the second changes:
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break
except KeyboardInterrupt:
    print('Digital clock, by Ai sweigart moodified by Agbolade Elijah')
    sys.exit() # when Ctrl-C is pressed, end the program.