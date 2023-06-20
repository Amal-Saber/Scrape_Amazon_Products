
# Scrape Amazon Products

This project involves collecting data on products and storing them in files

**The required data is :**
- Product Page Link
- Product Title
- Product ID
- Current Price
- Discount Percentage
- Price Before Discount
- Stars
- Reviewer count
- Product Info
- Product Description
- Product images


## Project Steps
  1. Create a code that collects product links, navigates to different pages, collects links from them, and exports them in a CSV file.

  2. wright code to collect product data and save them in CSV files. 
 There are four files each related data is stored in a file.  Each file contains a primary key, which links each file to the others.

        * product_details_data.csv
            - ID 
            - title  
            - Product Info    
            - Link Product Page
            - Product Discription
            
        * prices_data.csv
            - ID
            - title
            - Current Price
            - Link Product Page
            - Discount Percentage
            - Price Before Discount  

        * images_data.csv
            - ID
            - title
            - Current Price
            - image 1 : image 40 

        * ratings_data.csv
            - ID
            - title
            - Current Price
            - Stars out of 5
            - Reviewer Count
        
3. the last step is cleaning the data
    - file format
    - delete duplicate values
    - Change the data types of some columns such as currency, numbers, etc.
    - Delete unwanted text that came with some column values
    - split column values into columns 
    - ...     


## Tools Used    
   > - Excel 
   > - Python 
   > - Selenium
   > - Visual Studio Code 
    
       