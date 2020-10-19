import os
import platform

import Drivers as uc
uc.install()

from colorama import init
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from create_acc import create_account
from functions import calculate_move
from temp_gen import temp_mail
from verify import verification

init(convert = True)

driver_path = "default"


os_name = platform.system()
if os_name == "Linux":
    driver_path = 'Drivers/chromedriver_linux'
    clear_cmd = 'clear'

if os_name == "Windows":
    driver_path = 'Drivers/chromedriver.exe'
    clear_cmd = 'cls'
    
if os_name == "Darwin":
    driver_path = 'Drivers/chromedriver_mac'
    clear_cmd = 'clear'
    

def clear():
    return os.system(clear_cmd)

clear()

options = Options()
options.headless = True
options.add_argument('--log-level=3')
driver = webdriver.Chrome(options = options, executable_path = driver_path)
print("- . -.-. .... - .- -. .. -.-.")


x_i, y_i = calculate_move()
email = temp_mail(driver)
randuser, randpwd = create_account(driver, email, x_i, y_i)
verification(driver, randuser, randpwd)
