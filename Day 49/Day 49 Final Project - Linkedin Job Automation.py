from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

ACCOUNT_EMAIL = "your email"
ACCOUNT_PASSWORD = "your password"

url = "https://www.linkedin.com/"

def log_in(email, password):
    try :
        driver.implicitly_wait(20)
        email_btn = driver.find_element(By.ID, 'session_key')
        email_btn.send_keys(email)
        password_btn = driver.find_element(By.ID, 'session_password')
        password_btn.send_keys(password)

        send_btn = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
        send_btn.click()

    except NoSuchElementException:
        print("No Such Element")

def find_jobs():
    try:
        driver.implicitly_wait(20)
        jobs_btn = driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a')
        jobs_btn.click()
        driver.implicitly_wait(20)
        
    except NoSuchElementException:
        print("Element not found")


    try:
        driver.implicitly_wait(10)
        input_box = driver.find_element(By.CLASS_NAME, 'jobs-search-box__text-input')
        input_box.send_keys("Equity Research")
        input_box.send_keys( Keys.RETURN)
    except Exception as e:
        print(e)

def save_jobs():
    driver.implicitly_wait(20)
    listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container__link")

    i=0
    for listing in listings:
        print("Opening Listing")
        listing.send_keys(Keys.ENTER)
        time.sleep(2)
        try:
            if i<=5:
                driver.implicitly_wait(10)
                # Click Save Button
                apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button")
                apply_button.click()
                i+=1
                print(f"job {i} saved")
                if i==5:
                    print("Done")
                time.sleep(5)
                

        except Exception as e:
            print(e)
            continue

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

log_in(ACCOUNT_EMAIL, ACCOUNT_PASSWORD)
find_jobs()
save_jobs()