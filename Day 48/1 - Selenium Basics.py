from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Paradise-Lost-Penguin-Classics-Milton/dp/0140424393/ref=sr_1_2?crid=1OXM7YTD62HRY&dib=eyJ2IjoiMSJ9.hR5Y7ZG5sysQzNv4NTqK4bO8z7f43On0avknyvfGMxlBDJKbi9hjYviGf1BeBlU_izrdKLWswSOHykUVDV4HYEodzwshyMXcsgny1fTniC_9xmCA4NFzNM4OKpOltvhlBo3qr20n8DpJvSZ7M677FvzwqokXdBAHT0_ZlDfPrW-JlxhvCIabV56JfFk0nC8sKiHhV2L0qvVxm5oAkXsgmSy2eOvlL41grjyteptBRbuTYbBVvSAZaU0D0Ej4EoWUqr6yt8ZZ7fAUgnoqhYL_AoPNF3HlY1FBi3GHL9wP-ls.10IISkXmXDP3cWdEOzEBxfQPbFjF7Zq76JBV2a1fj8w&dib_tag=se&keywords=paradise+lost&qid=1711517263&sprefix=paradise+l%2Caps%2C1060&sr=8-2")



try:
    price = driver.find_element(By.ID, "price")
    print(price.text)
except NoSuchElementException:
    print("Price element not found")


# driver.close() # Close one particular tab.
driver.quit() # Close the browser.