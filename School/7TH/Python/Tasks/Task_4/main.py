from time import sleep
from os import system
from customtkinter import *


os.system('cls')
app = CTk('dark green')
app.geometry('400x400')
set_appearance_mode('dark')

def calculate():
    x = input_1.get()
    y = input_2.get()
    z = input_3.get()
    if x.isdigit and y.isdigit and z.isdigit:
        x = int(x)
        y = int(y)
        z = int(z)
        triangle_perimeter = x+y+z
        label_ans.configure(text=f"ANS = {triangle_perimeter}")
    else:
        print("try again...")

label = CTkLabel(master=app, text="Triangle perimeter calculator", font=("sans serif", 20))
label_ans = CTkLabel(master=app, text="ANS = 0")
input_1 = CTkEntry(master=app, placeholder_text="enter you 1st side", bg_color="transparent")
input_2 = CTkEntry(master=app, placeholder_text="enter you 2nd side", bg_color="transparent")
input_3 = CTkEntry(master=app, placeholder_text="enter you 3rd side", bg_color="transparent")
submit = CTkButton(master=app, text="calculate the perimeter", hover_color="green", bg_color="transparent", text_color="white", command=calculate)


label.pack(anchor="s", expand=False, pady=20)
label_ans.pack(anchor="n", expand=False, pady=20)
input_1.pack(anchor="n", expand=False, pady=10)
input_2.pack(anchor="n", expand=False, pady=10)
input_3.pack(anchor="n", expand=False, pady=10)
submit.pack(anchor="s", expand = True, pady=20)

app.mainloop()