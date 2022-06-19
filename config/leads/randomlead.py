import random
import psutil
import logging, os, time
import subprocess
import sys
from waiting import wait
from subprocess import call
from tarfile import FIFOTYPE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from fake_useragent import UserAgent
from faker import Faker
from faker.providers import *
from random import randint, randrange
import warnings
from importrandom import *
warnings.filterwarnings("ignore", category=DeprecationWarning) 

fake = Faker()
domain = [
"outlook.com",
"hotmail.com",
"yahoo.com",
"gmail.com",
"live.com",
]

linkdict = {
"N": "https://www.pinpoint7.net/BitcoinERA/?campaigns=TradeN&api_key=ROxUP76L7CNfJ8K&landings=BitcoinERA&product=",
"CT": "https://www.pinpoint7.net/BitcoinERA/?campaigns=TradeCT&api_key=ROxUP76L7CNfJ8K&landings=BitcoinERA&product=",
"B": "https://www.pinpoint7.net/BitcoinERA/?campaigns=TradeB&api_key=ROxUP76L7CNfJ8K&landings=BitcoinERA&product="
}

countries = ['NL', 'FI', 'SE', 'AU']

NL = "06" + str(randint(100000000, 999999999))
FI = "09" + str(randint(100000000, 999999999))
SE = "07" + str(randint(100000000, 999999999))
AU = "04" + str(randint(100000000, 999999999))

phone = [NL,FI,SE,AU]

ccode = ''
command = ''
command2 = ''
pnumber = ''

def sendlead(ccode):
    
    command = "openvpn --config " + randcountry(ccode) + " --script-security 2 --up /etc/openvpn/update-systemd-resolved --down /etc/openvpn/update-systemd-resolved --dhcp-option 'DOMAIN-ROUTE .' --down-pre --verb 0 --mute-replay-warnings"
    p = os.popen("sudo -S -b %s"%(command), 'w').write(' \n')
    time.sleep(10) #the important wait time

    if ccode == 'NL':
        pnumber = NL
    elif ccode == 'FI':
        pnumber = FI
    elif ccode == 'SE':
        pnumber = SE
    elif ccode == 'AU':
        pnumber = AU

    print(command)


    first = fake.first_name_male()
    last = fake.last_name()

    usr =[
    first+ last + (str(random.randint(0, 9)) + str(random.randint(0, 9))),
    (str(random.randint(0, 9)) + str(random.randint(0, 9))) + first+ last,
    (str(random.randint(0, 9)) + str(random.randint(0, 9))) + last+ first,
    (str(random.randint(0, 9)) + str(random.randint(0, 9))) + first[0]+ last,
    (str(random.randint(0, 9)) + str(random.randint(0, 9))) + last[0]+ first,
    first[0] + last + str(random.randint(0, 9)),
    last[0] + first + str(random.randint(0, 9)),
    last + first[0] + str(random.randint(0, 9)),
    first + last[0] + str(random.randint(0, 9)),
    first[0] + first[0] + last,
    last[0] + last[0] + first,
    first + last + str(random.randint(0, 9)),
    last + first + str(random.randint(0, 9)),
    last + first + (str(random.randint(0, 9)) + str(random.randint(0, 9))) 
    ]

    email = random.choice(usr) + "@" + random.choice(domain)
    useragent = UserAgent()
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", useragent.random)
    browser = webdriver.Firefox(firefox_profile=profile)

    browser.get(random.choice(list(linkdict.values())))
    try:
        el = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "form-control"))
        )
        input_fname = browser.find_element_by_name("first_name")
        input_lname = browser.find_element_by_name("last_name")
        input_email = browser.find_element_by_name("email")
        input_num = browser.find_element_by_name("phone")
        #input_submit = browser.find_element_by_name("submit")

        input_fname.send_keys(first)
        input_lname.send_keys(last)
        input_email.send_keys(email)
        input_num.send_keys(pnumber)
        print("form filled")
        time.sleep(2)
        #input_submit.click()

        #time.sleep(randint(1, 3))
        browser.close()
    except TimeoutException:
        browser.refresh()
        el = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "form-control"))
        )
        input_fname = browser.find_element_by_name("first_name")
        input_lname = browser.find_element_by_name("last_name")
        input_email = browser.find_element_by_name("email")
        input_num = browser.find_element_by_name("phone")
        #input_submit = browser.find_element_by_name("submit")

        input_fname.send_keys(first)
        input_lname.send_keys(last)
        input_email.send_keys(email)
        input_num.send_keys(pnumber)
        print("form filled")
        time.sleep(2)
        print('didnt work refreshed')
        
    command2 = 'killall openvpn'
    p = os.popen("sudo -S %s"%(command2), 'w').write(' \n')
    time.sleep(6)

for i in range(50):
    sendlead(random.choice(countries))
    print(i)
    print(i)
    print(i)
    print(i)

