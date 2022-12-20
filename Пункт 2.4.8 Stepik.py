from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)
    button = browser.find_element(By.TAG_NAME,'button')
    price = WebDriverWait(browser,15).until(EC.text_to_be_present_in_element((By.ID,'price'), '$100'))
    button.click()
    num = browser.find_element(By.ID, 'input_value')
    c = calc(int(num.text))
    pol = browser.find_element(By.ID, 'answer')
    but = browser.find_element(By.ID, 'solve')
    pol.send_keys(c)
    but.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(150)
    # закрываем браузер после всех манипуляций
    browser.quit()
