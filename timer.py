import time
setTime = int(input("Set your timer in seconds:"))
n = 1
 
while n:
    setTime = setTime - 1
    print(setTime)
    time.sleep(1)
    if setTime <= 0:
        print('Time\'s up.')
