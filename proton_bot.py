import os
import platform
import threading   #WIP

#import Drivers as uc        #WIP
#uc.install()                #WIP

from colorama import init
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pack.create_acc import create_account
from pack.functions import calculate_move
from pack.temp_gen import temp_mail
from pack.verify import verification

init(convert = True)

driver_path = "default"


os_name = platform.system()
if os_name == "Linux":
    driver_path = 'Drivers/chromedriver'
    clear_cmd = 'clear'

if os_name == "Windows":
    driver_path = 'Drivers/chromedriver.exe'
    clear_cmd = 'cls'
    
if os_name == "Darwin":
    driver_path = 'Drivers/chromedriver'
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
randuser, randpwd = create_account(driver, temp_mail(driver), x_i, y_i)
verification(driver, randuser, randpwd)
