from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")


try:
    f_name = driver.find_element(By.NAME, "fName")
    f_name.send_keys("Tushar")
    f_name = driver.find_element(By.NAME, "lName")
    f_name.send_keys("Dimri")
    email   = driver.find_element(By.NAME, "email")
    email.send_keys("Tushar@gmail.com")
    submit = driver.find_element(By.CLASS_NAME, "btn")
    submit.click()

except NoSuchElementException:
    print("Element not found")

