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
                print(ascii_banner)

except KeyboardInterrupt:
    os.system('/Users/raviprakashpandey/Desktop/Others/Coding/School_type/School_coding_and_hacking/.venv/bin/python /Users/raviprakashpandey/Desktop/Others/Coding/School_type/School_coding_and_hacking/Hacking/Terminal_Hack/terminal.py;')
