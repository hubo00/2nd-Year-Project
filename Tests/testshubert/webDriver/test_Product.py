"""
Hubert Bukowski | x00161897
2nd Year Project | PlantOasis eCommerce store
Product page tests
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DRIVER_PATTERNS = [
    (webdriver.Chrome("D:\\Selenium\\Drivers\\chromedriver.exe")),
    (webdriver.Edge("D:\\Selenium\\Drivers\\msedgedriver.exe")),
    # (webdriver.firefox("D:\\Selenium\\Drivers\\geckodriver.exe")),
    ]

APP_URL = "http://127.0.0.1:8000/"

for driver in DRIVER_PATTERNS:
    my_browser = driver

    my_browser.get(APP_URL)
    if my_browser.current_url != APP_URL:
        print("Wrong HTML document loaded")
    else:
        print(APP_URL + " Loaded successfully")
        print("RUNNING Product TESTS")

    my_browser.fullscreen_window()

    # Time to allow all web elements to load
    time.sleep(3)

    # Assert Page Title
    assert "Check out our plants and tools! | PlantOasis" in driver.title
    # Verify Page Title
    expected_title = "Check out our plants and tools! | PlantOasis"
    actual_title = driver.title
    if expected_title == actual_title:
        print("Page title verification success!")
    else:
        print("Page title verification failed :(")

    
    # Assert that product list appears
    product_boxes = driver.find_elements_by_class_name("home-images")
    if product_boxes:
        print("Product list verification success!")
    else:
        print("Product list verification failed :(")
    # Assert that Single product is there
    specific_product = driver.find_element_by_css_selector(".col-lg-3:nth-child(1) .home-images")
    if specific_product:
        print("Product assertion success!")
    else:
        print("Product assertion failed :(")
    # Enter Product detail page
    specific_product.click()

    # Assert page title
    assert "Adanson's Monstera - Plant Oasis" in driver.title
    # Verify page title
    expected_title = "Adanson's Monstera - Plant Oasis"
    actual_title = driver.title
    if expected_title == actual_title:
        print("Page title verification success!")
    else:
        print("Page title verification failed :(")


    # Asserting & Verifying page elements
    # Asserting product image
    product_image = driver.find_element_by_class_name("prod-image")
    if product_image:
        print("Product image assertion success!")
    else:
        print("Product image assertion failed :(")
    # Asserting product title
    product_title = driver.find_element_by_class_name("prod-title")
    if product_title:
        print("Product title assertion success!")
    else:
        print("Product title assertion failed :(")
    # Verifying product title
    expected_title = "Adanson's Monstera"
    actual_title = driver.find_element_by_class_name("prod-title").text
    if expected_title == actual_title:
        print("Product title verification success!")
    else:
        print("Product title verification failed :(")
    
    # Asserting product price
    product_price = driver.find_element_by_class_name("prod-price")
    if product_price:
        print("Product price assertion success!")
    else:
        print("Product price assertion failed :(")
    # Verifying product price
    expected_price = "€9.99"
    actual_price = product_price.text
    if expected_price == actual_price:
        print("Product price verification success!")
    else:
        print("Product price verification failed :(")
    
    # Asserting stock indicator
    product_stock = driver.find_element_by_class_name("stock-icon-good")
    if product_stock:
        print("Positive product stock assertion success!")
    else:
        print("Positive product stock assertion failed :(")
    # Verifying stock indicator if product is in Stock
    expected_stock = "In Stock"
    actual_stock = driver.find_element_by_class_name("stock-notif").text
    if expected_stock == actual_stock:
        print("Positive product stock verification success!")
    else:
        print("Positive product stock verification failed :(")

    # Assert add to wishlist button
    wishlist_button = driver.find_element_by_class_name

    # Assert add to cart button
    atc_button = driver.find_element_by_class_name("btn-plants")
    if atc_button:
        print("Add to cart button assertion success!")
    else:
        print("Add to cart button assertion failed :(")
    
    # Assert product description heading
    product_desc_head = driver.find_element_by_tag_name("h5")
    if product_desc_head:
        print("Product description heading assertion success!")
    else:
        print("Product description heading assertion failed :(")
    # Verify product description heading
    expected_heading = "Product Description"
    actual_heading = product_desc_head.text
    if expected_heading == actual_heading:
        print("Product description heading verification success!")
    else:
        print("Product description heading verification failed :(")
    
    # Assert Product description
    product_description = driver.find_element_by_css_selector(".col-10 > p")
    if product_description:
        print("Product description assertion success!")
    else:
        print("Product description assertion failed :(")
    # Verify product description
    expected_desc = "scary plant"
    actual_desc = product_description.text
    if expected_desc == actual_desc:
        print("Product description verification success!")
    else:
        print("Product description verification failed :(")

    # Add product to cart & Verify the user got redirected
    # Click add to cart button
    atc_button.click()
    # Assert page title
    assert "Cart - Plant Oasis" in driver.title
    # Verify page title
    expected_title = "Cart - Plant Oasis"
    actual_title = driver.title
    if expected_title == actual_title:
        print("Page title verification success!")
    else:
        print("Page title verification failed :(")

    # if this isn't the last browser being tested, close the browser.
    if driver != DRIVER_PATTERNS[-1]:
        print("Closing test")
        driver.close()

print("All tests ran")
time.sleep(3)
driver.close()