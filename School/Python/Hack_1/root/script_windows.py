import os
import time
import shutil

def get_ip_info():
    # Run 'arp -a' and capture the output
    output = os.popen('arp -a').read()
    
    # Create directory if not exists
    if not os.path.exists('ip_saves'):
        os.makedirs('ip_saves')
    
    # Save output to a file
    with open('ip_saves/ip_info.txt', 'w') as file:
        file.write(output)

def check_password():
    attempts = 3
    password = "tejas_999"  # Set your desired password here
    
    while attempts > 0:
        user_input = input("Enter password: ")
        if user_input == password:
            print("Access granted. Welcome to the elite level.")
            return True
        else:
            attempts -= 1
            print(f"Incorrect password. {attempts} attempts remaining.")
    
    print("Too many incorrect attempts. Deleting script. Better luck next time.")
    os.remove(__file__)
    return False

def main():
    get_ip_info()
    print("Wait for 5 seconds while I do some magic...")
    time.sleep(5)
    
    # Shutdown command interface
    os.system('shutdown -i')
    
    # List contents of ip_saves folder
    print("Here's a list of your precious saved IP info:")
    for filename in os.listdir('ip_saves'):
        print(filename)

if __name__ == "__main__":
    if check_password():
        main()
