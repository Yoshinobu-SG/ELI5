import time
Reminder=float(input('Enter the time: ' ))
if Reminder > 0:
    timee="Wake up"
else:
    timee="Don't wake up"
while Reminder > 0:
    time.sleep(1.5)
    print(timee)
if Reminder < 0:
    timee="Don't wake up"
else:
    timee="Wake up"
