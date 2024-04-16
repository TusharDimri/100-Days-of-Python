from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")


try:
    search = driver.find_element(By.XPATH, '//*[@id="p-search"]/a')
    search.send_keys("Paradise Lost", Keys.ENTER)

except NoSuchElementException:
    print("Element not found")

