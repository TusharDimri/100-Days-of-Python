from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")


try:
    event_time = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
    for time in event_time:
        print(time.text)
    event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
    for event_name in event_names:
        print(event_name.text)

    events = {}
    for n in range(len(event_names)):
        events[n] = {
            "time": event_time[n].text,
            "name": event_names[n].text,
        }
    print(events)
except NoSuchElementException:
    print("Element not found")


driver.quit()