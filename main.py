import msvcrt
import time
import sys
import os

os.system("color 0A")
os.system("cls" if os.name == "nt" else "clear")

timer = 0

print("<<<<< COUNTDOWN TIMER >>>>>")

while True:
    timer = int(input("How long would you like to set the timer for?: "))
    if timer <= 0:
        print("The time can't be less then or equal to zero!")
    else:
        break

for i in reversed(range(timer)):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)

    # quiting the program mid countdown
    if msvcrt.kbhit():
        if msvcrt.getch() == b'q':
            os.system("color 07")
            sys.exit()
        
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

print("Time's UP!")

os.system("color 07")