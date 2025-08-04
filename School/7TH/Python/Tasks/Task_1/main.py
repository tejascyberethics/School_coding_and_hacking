"""Task_1, WAP of a user taking and input and rusult in perrimeter or area"""

# import elements that i have imported

import time
import os
from customtkinter import *

# main system clear screen on terminal function

def clear():
    os.system('clear')


# calculation of area and its perimeter function

def area():
    area = l*b
    print(f"the area of the rectangle height {l} and breath {b} is:-> {area}\n\n\n")

def perimeter():
    perimeter = 2*(l+b)
    print(f"the perimeter of the rectangle height {l} and breath {b} is:-> {perimeter}\n\n\n")


# main code

clear()
l = input("enter your length of rectangle\n:-> ")
b = input("enter your breath of rectangle\n:-> ")

clear()

check_l, check_b = l.isdigit(), b.isdigit()

if (check_l == True) and (check_b == True):
    clear()
    l = int(l)
    b = int(b)
    time.sleep(1)
    clear()
    condition = int(input("what do you want to do for the rectangle?\n1)find its peremeter\n2)find its area\n\n:-> "))
    if condition == 2:
        clear()
        area()
        time.sleep(5)
        clear()
    elif condition == 1:
        clear()
        perimeter()
        time.sleep(5)
        clear()
    else:
        clear()
        time.sleep(1)
        print("wrong input, try again (try putting the number only)")
        time.sleep(2)
        clear()
else:
    clear()
    time.sleep(1)
    print("please enter a number")
    time.sleep(1)
    clear()