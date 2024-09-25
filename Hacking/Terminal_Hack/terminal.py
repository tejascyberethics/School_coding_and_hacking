import os
import pyfiglet
import time

a = 'clear' # in windows, change this into cls



os.system(a)

ascii_banner = pyfiglet.figlet_format("Welcome To Forced Terminal")
print(ascii_banner)

time.sleep(3)

try:
    while True:
            enter_command = input("\n\nEnter a command:-> ")
            os.system(enter_command)
            if enter_command == a:
                ascii_banner = pyfiglet.figlet_format("Welcome To Forced Terminal")
                print(ascii_banner)

except KeyboardInterrupt:
    time.sleep(1)
    os.system(a)
    ascii_banner = pyfiglet.figlet_format("To Quit, Close The Window")
    print(ascii_banner)
    time.sleep(1)
    os.system(a)
