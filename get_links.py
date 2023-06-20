from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import json
import os
import time


url = 'https://www.amazon.ae/s?rh=n%3A11995892031&fs=true&ref=lp_11995892031_sar'
os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)


links = []
driver.get(url)
for i in range(50):
    product_page_link = driver.find_elements(By.CSS_SELECTOR, '.s-line-clamp-2 [href]')
    product_link = [i.get_attribute('href') for i in product_page_link]

    for link in product_link:
        links.append(link)

    
    next_page = driver.find_element(By.CLASS_NAME, 's-pagination-strip').find_element(By.LINK_TEXT, "Next")
    next_page.click()
    time.sleep(2)

df = pd.DataFrame(links,index=None, columns=['links'])
df.to_csv("products_links1.csv",index=False)
