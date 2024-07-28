"""take 3 user input and enter their sum & product"""


# a = input("enter your 1st digit\n:-> ")
# sleep(1)
# b = input("\n\nenter your 2nd digit\n:-> ")
# sleep(1)
# c = input("\n\nenter your 3rd digit\n:-> ")


# import elements

from time import sleep
import os
from customtkinter import *

# installation for important modules

os.system('clear')
os.system('pip install customtkinter')
os.system('pip install customtkinter --upgrade')
sleep(2)
os.system('clear')
sleep(1)
os.system('pip install pillow')
os.system('pip install pillow --upgrade')
sleep(2)
os.system('clear')
sleep(1)


# ui setup for code

app = CTk()
app.geometry('400x400')
set_appearance_mode('dark')

# command functions for the widget's

def calculate_clicked():
    os.system('clear')
    print(f"entered input of: \n1){input_1.get()} \n2){input_2.get()} \n3){input_3.get()}")
    x = input_1.get()
    y = input_2.get()
    z = input_3.get()
    if (x.isdigit) and (y.isdigit) and (z.isdigit):
        x = int(x)
        y = int(y)
        z = int(z)
        calculated_sum =  x + y + z
        calculated_product = x * y * z
        print("\ncalculating\n\n")
        print(f"the sum of all three of these are {x+y+z}\nthe product of all three of there are {x*y*z}")
        label_ans_sum.configure(text = f"ANS_ADD = {calculated_sum}")
        label_ans_product.configure(text = f"ANS_MUL = {calculated_product}")
    else:
        os.system('clear')
        print("try again, put numbers only")

# main widgets 
label = CTkLabel(master=app, text = "Sum and Product finder", font = ("Sans Serif",25))
label_ans_sum = CTkLabel(master=app, text = "ANS_ADD = 0", font = ("Sans Serif",15))
label_ans_product = CTkLabel(master=app, text = "ANS_MUL = 0", font = ("Sans Serif",15))
input_1 = CTkEntry(master=app, placeholder_text = "enter you 1st number", width = 300, height = 30, placeholder_text_color = "red")
input_2 = CTkEntry(master=app, placeholder_text = "enter you 2nd number", width = 300, height = 30, placeholder_text_color = "red")
input_3 = CTkEntry(master=app, placeholder_text = "enter you 3rd number", width = 300, height = 30, placeholder_text_color = "red")
button = CTkButton(master=app, text = "click to calculate", bg_color = "transparent", hover_color = "red", command = calculate_clicked)

label.pack(anchor = "s", expand = False, pady = 20)
label_ans_sum.pack(anchor = "s", expand = False, pady = 10)
label_ans_product.pack(anchor = "s", expand = False, pady = 10)
input_1.pack(anchor = "s", expand = True, pady = 10)
input_2.pack(anchor = "n", expand = False, pady = 10)
input_3.pack(anchor = "n", expand = False, pady = 10)
button.pack(anchor = "n", expand = True, pady = 20)



app.mainloop()