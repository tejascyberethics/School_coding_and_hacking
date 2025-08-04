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


clear()
x = input("enter a number to check if it is positive: ")

if x.isdigit:
    print("approved, lets continue")
    x = int(x)
    clear()

    if x < 0:
        print(f"the number {x} is negitive.")
        sleep(4)
        clear()
    elif x == 0:
        print(f"the number {x} is an whole number.")
        sleep(4)
        clear()
    else:
        print(f"the number {x} is positive.")
        sleep(4)
        clear()

