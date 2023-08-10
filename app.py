
import time
from rede import redeem_codes
from selenium.webdriver.common.by import By

from selenium import webdriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

url = "https://play.google.com/store/games?code"
driver.get(url)

temp = redeem_codes[0]
for i in redeem_codes:

    driver.find_element(By.CLASS_NAME,'whsOnd.zHQkBf').send_keys(i)
    elements = driver.find_elements(By.TAG_NAME, "button")
    elements[-1].click()
    time.sleep(5)
    driver.find_element(By.CLASS_NAME,'whsOnd.zHQkBf').clear()



