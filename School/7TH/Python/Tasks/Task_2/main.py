"""Task_2, WAP to accept distance from a user and convert into km (whatever you want)"""

# import elements

from time import sleep
import os
import string
from customtkinter import *

# system function 

def clear():
    os.system('clear')

def cls_step():
    clear()
    sleep(1)


# functions

def inp_to_km_conv():
    conv = inp_conv / 1000
    print(f"the value {inp_conv} in kilometer's is {conv}")
    sleep(5)
    clear()
    cls_step()

def inp_to_m_conv():
    conv = inp_conv / 100
    print(f"the value {inp_conv} in meters is {conv}")
    sleep(5)
    clear()
    cls_step()

def inp_to_cm_conv():
    conv = inp_conv / 10
    print(f"the value {inp_conv} in centimeters is {conv}")
    sleep(5)
    clear()
    cls_step()


# main code 

cls_step()
inp_conv = input("enter you number to convert\n:-> ")
if inp_conv.isdigit():
    inp_conv = int(inp_conv)
    cls_step()
    print("so you want to convert",inp_conv,"by what? \n1)km \n2)m \n3)cm\n")
    what_conv = input(":-> ")
    what_conv_test = what_conv.isdigit()
    if what_conv_test == True:
        cls_step()

        what_conv = int(what_conv)

        if what_conv == 1:
            inp_to_km_conv()

        elif what_conv == 2:
            inp_to_m_conv()

        elif what_conv == 3:
            inp_to_cm_conv()
            
        else:
            cls_step()
            print("try again, put the write option or try putting the number.")
            sleep(2)
            cls_step()
    else:
        cls_step()
        print("try again, try putting numbers only")
        sleep(2) 
        cls_step()
else:
    cls_step()
    print("try again, please enter a number")
    sleep(2)
    cls_step()
