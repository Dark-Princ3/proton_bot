import os
import time

from colorama import init
from colorama import Fore
from pack.functions import (calculate_move, find_xpath, human_move, switch_frame)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

init(convert = True)

def verification(driver, randuser, randpwd):
    x_i, y_i = calculate_move()
    
    print(Fore.CYAN+"Verifying Account.......\n\n", Fore.WHITE)

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    '''- . -.-. .... - .- -. .. -.-.'''
    print(Fore.CYAN+"Waiting for verification E-mail\n\n", Fore.WHITE)
    
    wait_email = True

    while wait_email == True:
        try:
            WebDriverWait(driver,10).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/div/main/section[1]/div/div/div[1]/div/table/tbody/tr/td[1]/a')))
            wait_email = False
        except:    
            driver.refresh()

    find_xpath(driver, '//*[@id="__layout"]/div/div/main/section[1]/div/div/div[1]/div/table/tbody/tr/td[1]/a').click()
    
    switch_frame(driver, '//*[@id="the_message_iframe"]')

    code = driver.find_element_by_tag_name("code").text

    print(Fore.CYAN+"Please wait\n\n", Fore.WHITE)

    time.sleep(.2)

    driver.switch_to.window(driver.window_handles[1])

    code_input = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type = "text"]')))
    for i in code:
        code_input.send_keys(i)
        time.sleep(.1)

    human_move(driver, '//*[@id = "verification-panel"]/p[3]/button', x_i, y_i)
    time.sleep(1)
    human_move(driver, '//*[@id = "confirmModalBtn"]',x_i,y_i)
    time.sleep(1)
    
    print(Fore.GREEN+"\nYour account details.\n", Fore.WHITE)
    try:
        print("Username:\t", randuser, "\n")
        print("Password:\t", randpwd, "\n")
    except BaseException as E:
        print(E)
        input("\nBroken\n")

    ''''- . -.-. .... - .- -. .. -.-.'''
    print(Fore.WHITE+"")
    driver.close()  
    os.system("exit")
