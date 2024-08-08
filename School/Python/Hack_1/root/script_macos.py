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
            print("Access granted. You’re in the inner circle.")
            return True
        else:
            attempts -= 1
            print(f"Incorrect password. {attempts} attempts remaining.")
    
    print("Too many incorrect attempts. Deleting script. Oopsie daisy.")
    os.remove(__file__)
    return False

def main():
    get_ip_info()
    print("Hold your horses for 5 seconds...")
    time.sleep(5)
    
    # Shutdown command interface
    os.system('osascript -e \'tell app "System Events" to shut down\'')
    
    # List contents of ip_saves folder
    print("Listing your saved IP info:")
    for filename in os.listdir('ip_saves'):
        print(filename)

if __name__ == "__main__":
    if check_password():
        main()
