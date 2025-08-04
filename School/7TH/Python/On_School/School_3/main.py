import os
from time import sleep


#error, fix it on home

def clear():
    os.system('cls')



def calculate_step1():
    sleep(1)
    clear()
    sleep(1)
    print("please wait...")
    sleep(2)


    if bill_respected >= 25000 :
        Disk = 20
        print(f"\n\n\n{name}, you got a discount of {bill_respected}")
        Disk_total = bill_respected * ( Disk / 100 )
        print(Disk_total)
        
    elif bill_respected >= 20000 and bill_respected < 25000:
        Disk = 15
        print(f"\n\n\n{name}, you got a discount of {bill_respected}")
        Disk_total = bill_respected * ( Disk / 100 )
        print(Disk_total)
        
    elif bill_respected >= 10000 and bill_respected < 20000:
        Disk = 10
        print(f"\n\n\n{name}, you got a discount of {bill_respected}")
        Disk_total = bill_respected * ( Disk / 100 )
        print(Disk_total)
    
    elif bill_respected >= 5000 and bill_respected < 10000:
        Disk = 5
        print(f"\n\n\n{name}, you got a discount of {bill_respected}")
        Disk_total = bill_respected * ( Disk / 100 )
        print(Disk_total)
    
    else:
        Disk = 0
        print(f"\n\n\n{name}, you got a discount of {bill_respected}")
        Disk_total = bill_respected * ( Disk / 100 )
        print(Disk_total)

    

    



name = input("\n\n enter your name:-> ")
sleep(1)
bill_respected = int(input(" \n \nenter your bill amount:-> "))
sleep(2)
clear()
calculate_step1()
