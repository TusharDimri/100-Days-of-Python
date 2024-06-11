from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

def fill_form(prices_data, links_data, addresses_data, num):
    for i in range(0, num):
        url = 'https://forms.gle/K6C5N5heV1KhixPn9'
        driver.get(url)
        driver.implicitly_wait(10)

        address_btn = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
        address_btn.send_keys(addresses_data[i])
        
        price_btn = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_btn.send_keys(prices_data[i])

        links_btn =  driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
        links_btn.send_keys(links_data[i])
        
        submit_btn = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        submit_btn.click()
        time.sleep(5)

def get_listings():
    url = 'https://appbrewery.github.io/Zillow-Clone/'
    response=requests.get(url)
    page = response.text

    soup = BeautifulSoup(page, 'html.parser')

    prices_data = []
    links_data = []
    addresses_data = []

    prices = soup.find_all(name = 'div', class_='PropertyCardWrapper')
    for price in prices:
        prices_data.append(price.text.strip().split("+")[0].split("/")[0])
    links = soup.find_all(name='a', class_='property-card-link')
    for link in links:
        links_data.append(link.get('href'))

    addresses = soup.find_all(name='address')
    for address in addresses:
        addresses_data.append(address.text.strip())

    fill_form(prices_data, links_data, addresses_data, len(prices_data))

get_listings()