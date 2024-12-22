import time
"""
time.sleep(seconds to be waited) = this method waits the amount of seconds inputed so the
code after it will run after that many seconds.
 """

while True :
    utime = int(input("Enter the number of seconds to be counted down: "))
    if utime > 0 :
        break
    else :
        print("Invalid input (time must be positve natural number)")
        continue
        

for x in range (utime , -1 , -1):
    seconds = x % 60  # if 65 secs then timers show [65 -60] (remainder) when 59 it show remaider is shown
    minutes = int(x/60) % 60 # same as above but x /60 give the number of minutes
    hours = int(x/ 3600) # to give number of hours
    time.sleep(1) # so the clock will update every second
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
print("TIME IS UP!")