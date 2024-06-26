from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")


try:
    number = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
    print(number.text)
except NoSuchElementException:
    print("Element not found")


driver.quit()