import os

def check_div_2():
    if x.isdigit:
        x = int(x)
        if x % 2:
            print(f"{x} it is divisible by 2")
        else:
            print(f"{x} it is not divisible by 2")
    else:
        print("try again")
def clear():
    os.system('cls')

x = input("enter a number to check its divisiblility by 2:-> ")
clear()
check_div_2()
