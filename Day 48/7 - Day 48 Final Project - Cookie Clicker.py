from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")


try:
    driver.implicitly_wait(20)
    language = driver.find_element(By.ID, 'langSelect-EN')
    language.click()

    driver.implicitly_wait(20)
    cookie = driver.find_element(By.ID, "bigCookie")
    start_time = time.time()
    while True:
        cookie.click()
        current_time = time.time() - start_time
        if current_time >= 60 and current_time <= 61:
            product1 = driver.find_element(By.ID, "product1")
            product1.click()
            product2 = driver.find_element(By.ID, "product2")
            product2.click()
        print(current_time)
except NoSuchElementException:
    print("Element not found")

