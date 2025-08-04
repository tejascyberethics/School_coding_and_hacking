import os
import platform
from time import sleep


y = platform.system()


def clear():
    if y == "Windows":
        os.system('cls')
        sleep(1)
    else:
        os.system('clear')
        sleep(1)


x = int(input("enter your age")) 
if x >= 18:
    print(f"you are eligible for voting")