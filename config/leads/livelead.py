import random
import os, time
import csv 
from tarfile import FIFOTYPE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from fake_useragent import UserAgent
from random import randint, randrange
import warnings
from importrandom import *
warnings.filterwarnings("ignore", category=DeprecationWarning) 


afflinks = [
#"https://www.pinpoint7.net/BitcoinERA/?campaigns=TradeK&api_key=L71VmhSk33rNfbl&landings=BitcoinERA&product=",
#"https://www.pinpoint7.net/BitcoinERA/?campaigns=TradeM&api_key=L71VmhSk33rNfbl&landings=BitcoinERA&product=",
#"https://www.pinpoint7.net/BitcoinERA/?campaigns=TradeO&api_key=L71VmhSk33rNfbl&landings=BitcoinERA&product=",
#"https://www.pinpoint7.net/BitcoinERA/?campaigns=TradeP&api_key=L71VmhSk33rNfbl&landings=BitcoinERA&product=",
#"https://www.pinpoint7.net/BitcoinERA/?campaigns=TradeE&api_key=L71VmhSk33rNfbl&landings=BitcoinERA&product=",
#"https://www.pinpoint7.net/BitcoinERA/?campaigns=TradeV&api_key=L71VmhSk33rNfbl&landings=BitcoinERA&product=",
#"https://www.pinpoint7.net/BitcoinERA/?campaigns=TradeR&api_key=L71VmhSk33rNfbl&landings=BitcoinERA&product=",
#"https://www.pinpoint7.net/BitcoinERA/?campaigns=TradeCT&api_key=L71VmhSk33rNfbl&landings=BitcoinERA&product=",
#"https://www.pinpoint7.net/BitcoinERA/?campaigns=TradeMg&api_key=L71VmhSk33rNfbl&landings=BitcoinERA&product=",
"https://www.pinpoint7.net/BitcoinERA/?campaigns=TradeL&api_key=L71VmhSk33rNfbl&landings=BitcoinERA&product=",
"https://www.pinpoint7.net/BitcoinERA/?campaigns=TradeN&api_key=L71VmhSk33rNfbl&landings=BitcoinERA&product=",
#"https://www.pinpoint7.net/BitcoinERA/?campaigns=TradeI&api_key=L71VmhSk33rNfbl&landings=BitcoinERA&product=",
#"https://www.pinpoint7.net/BitcoinERA/?campaigns=TradeA&api_key=L71VmhSk33rNfbl&landings=BitcoinERA&product=",
#"https://www.pinpoint7.net/BitcoinERA/?campaigns=TradeY&api_key=L71VmhSk33rNfbl&landings=BitcoinERA&product=",
"https://www.pinpoint7.net/BitcoinERA/?campaigns=TradeD&api_key=L71VmhSk33rNfbl&landings=BitcoinERA&product=",
"https://www.pinpoint7.net/BitcoinERA/?campaigns=TradeMZ&api_key=L71VmhSk33rNfbl&landings=BitcoinERA&product=",
#"https://www.pinpoint7.net/BitcoinERA/?campaigns=Trade_La&api_key=L71VmhSk33rNfbl&landings=BitcoinERA&product="
]

def sendlead(line):

    first = '' #get from database
    last = '' #get from database
    email = '' #get from database
    phone = '' #get from database

    #get ccode from database
    #################################################
    #################################################
    with open("/home/abin/Leads/leads/SE7K.csv", 'r') as f:
        mycsv = csv.reader(f)
        mycsv = list(mycsv)
        first = mycsv[line][0]
        last = mycsv[line][1]
        email = mycsv[line][2]
        phone = mycsv[line][3]
        ccode = mycsv[line][4]

    command = ''
    command2 = ''
    
    command = "openvpn --config " + randcountry(ccode) + " --script-security 2 --up /etc/openvpn/update-systemd-resolved --down /etc/openvpn/update-systemd-resolved --dhcp-option 'DOMAIN-ROUTE .' --down-pre --verb 0 --mute-replay-warnings"
    p = os.popen("sudo -S -b %s"%(command), 'w').write(' \n')
    time.sleep(10) #the important wait time

    print(command)
    
    useragent = UserAgent()
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", useragent.random)
    browser = webdriver.Firefox(firefox_profile=profile)

    browser.get(random.choice(afflinks))
    try:
        el = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "form-control"))
        )
        input_fname = browser.find_element_by_name("first_name")
        input_lname = browser.find_element_by_name("last_name")
        input_email = browser.find_element_by_name("email")
        input_num = browser.find_element_by_name("phone")
        input_submit = browser.find_element_by_name("submit")

        input_fname.send_keys(first)
        input_lname.send_keys(last)
        input_email.send_keys(email)
        input_num.send_keys(phone)
        print("form filled")
        time.sleep(2)

        with open('pier.txt', 'a') as f:
            f.write("\n")
            f.write(first + " " + last + " " + email + " " + phone + " " + str(line))
        input_submit.click()

        time.sleep(65)
        with open('links.txt', 'a') as h:
            h.write("\n")
            h.write(browser.current_url)
        browser.close()
        
    except TimeoutException:
        print('didnt work refreshing')
        browser.refresh()
        el = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "form-control"))
        )
        input_fname = browser.find_element_by_name("first_name")
        input_lname = browser.find_element_by_name("last_name")
        input_email = browser.find_element_by_name("email")
        input_num = browser.find_element_by_name("phone")
        input_submit = browser.find_element_by_name("submit")

        input_fname.send_keys(first)
        input_lname.send_keys(last)
        input_email.send_keys(email)
        input_num.send_keys(phone)
        print("form filled")
        time.sleep(2)
        with open('pier.txt', 'a') as f:
            f.write("\n")
            f.write(first + " " + last + " " + email + " " + phone + " " + str(line))
        input_submit.click()

        time.sleep(65)
        with open('links.txt', 'a') as h:
            h.write("\n")
            h.write(browser.current_url)
        browser.close()

    command2 = 'killall openvpn'
    p = os.popen("sudo -S %s"%(command2), 'w').write(' \n')
    time.sleep(randint(270, 900))

for i in range(100):
    sendlead(i+18)
    print(i+18)
