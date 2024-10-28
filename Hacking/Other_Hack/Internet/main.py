import os
import subprocess
from cryptography.fernet import Fernet

# Generate or use an existing encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)
print(f"Encryption Key (Store safely): {key.decode()}")


# Encrypt Command Outputs for Secure Display and Decrypt for User
def execute_encrypted_command(command):
    # Run the command without root privileges
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Encrypt the output
    encrypted_output = cipher_suite.encrypt(result.stdout.encode())
    print("Encrypted Output:", encrypted_output.decode())

    # Decrypt and display the output
    decrypted_output = cipher_suite.decrypt(encrypted_output).decode()
    print("Decrypted Output:", decrypted_output)


# Main function to run the terminal
def run_user_terminal():
    print("User Terminal is now running. Commands will have encrypted and decrypted output.")
    while True:
        command = input("UserTerminal> ")
        execute_encrypted_command(command)


run_user_terminal()
