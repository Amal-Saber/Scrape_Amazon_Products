from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import json
import os
import time


os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)


def get_title(driver):
    # Get Product Title
    Product_Title = driver.find_element(By.ID, 'productTitle').get_attribute('innerHTML').strip()

    return Product_Title




def get_price(driver):
    #  Get Product Current Price
    current_price = driver.find_element(By.CLASS_NAME, 'a-offscreen').get_attribute('innerHTML').strip()


    # Get Discount Percentage
    try:
        discount_percentage = driver.find_element(By.CLASS_NAME, "savingsPercentage").get_attribute('innerHTML')
    except:
        discount_percentage = 'No discount'


    # Get Price befor the discount 
    try:
        typical_price = driver.find_element(By.CLASS_NAME, "a-offscreen").get_attribute('innerHTML')
    except:
           typical_price = "No discount" 

    return    current_price,  discount_percentage,  typical_price  
    



def get_rating(driver):

    # Get stars number
    try:
        stars = driver.find_element(By.CSS_SELECTOR, 'span[data-hook="rating-out-of-text"]').get_attribute('innerHTML')    
    except:
        stars = "No reviewer"


    # Get Reviewer Count
    try:
        reviewer_count_tag = driver.find_element(By.CSS_SELECTOR, 'div[ data-hook="total-review-count"]')
        reviewer_count = reviewer_count_tag.find_element(By.TAG_NAME, 'span').get_attribute('innerHTML').split(">",2)[1].strip()
    except:
        reviewer_count = "No reviewer"

    return   stars, reviewer_count      




def get_product_info(driver):
    # Get product discription
    try:
        product_discription_tags = driver.find_element(By.ID, "feature-bullets" ).find_elements(By.CLASS_NAME, "a-list-item")
        product_discription = [i.text for i in product_discription_tags]
    except:
        product_discription = 'No product discription'


    # get Product Details
    try:
        keys_tags = driver.find_elements(By.CSS_SELECTOR, 'td[class="a-span3"]')
        keys = [key_tag.text for key_tag in keys_tags]

        values_tag = driver.find_elements(By.CSS_SELECTOR, 'td[class="a-span9"]')
        values = [val.text for val in values_tag]

        product_info = {}
        for i in range(0,len(keys)):
            product_info[keys[i]] = values[i]

    except:
        product_info = "No product info"

    return product_discription, product_info



def  get_image(driver):
    # Get image's urls
    links = []
    url_tags = driver.find_elements(By.CLASS_NAME, "a-button-text")
    for i in url_tags:
        try:
            img = i.find_element(By.TAG_NAME, "img").get_attribute('src')
            links.append(img)
        except:
            continue

    return links



def save_csv(data_list, csv_file_name):
    df = pd.DataFrame(data_list)
    df.to_csv(csv_file_name)



def save_json(data_list, json_file_name):
    with open(json_file_name, "w") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4) 


#-------------------------------------------------------------------------------------------------------------------------------
product_details_data = []
ratings_data = []
images_data = []
prices_data = []


urls = pd.read_csv("products_links.csv", header=0)
for i, url in enumerate(urls['links']):
    start_time = time.time()
    driver.get(url)
    
    title = get_title(driver)
    current_price,  discount_percentage,  typical_price = get_price(driver)
    stars, reviewer_count = get_rating(driver)
    product_discription, product_info = get_product_info(driver)
    links = get_image(driver)


    product_details = {}
    product_details['Link Product Page'] = url
    product_details['title'] = title
    product_details['ID'] = i
    product_details['Product Discription'] = product_discription
    product_details['Product Info'] = product_info
    product_details_data.append(product_details)


    product_rate = {}
    product_rate['Link Product Page'] = url
    product_rate['title'] = title
    product_rate['ID'] = i
    product_rate['Stars'] = stars
    product_rate['Reviewer Count'] = reviewer_count
    ratings_data.append(product_rate)


    product_images = {}
    product_images['Link Product Page'] = url
    product_images['title'] = title
    product_images['ID'] = i
    product_images['Images'] = links
    images_data.append(product_images)


    product_price = {}
    product_price['Link Product Page'] = url
    product_price['title'] = title
    product_price['ID'] = i
    product_price['Current Price'] = current_price
    product_price['Discount Percentage'] = discount_percentage 
    product_price['Price Before Discount'] = typical_price
    prices_data.append(product_price)
    
    print(time.time() - start_time)
    



product_details_datacsv = save_csv(product_details_data, 'product_details_data.csv')

ratings_datacsv = save_csv(ratings_data, 'ratings_data.csv')

images_datacsv = save_csv(images_data, 'images_data.csv')

prices_datacsv= save_csv(prices_data, 'prices_data.csv')
