"""
Hubert Bukowski | x00161897
2nd Year Project | PlantOasis eCommerce store
Manage Product tests
NOTE: This test requires the 'addProduct' test to be completed beforehand
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

MODERATOR_USERNAME = "hubo00"
MODERATOR_PASSWORD = "123"

DRIVER_PATTERNS = [
    (webdriver.Chrome("D:\\Selenium\\Drivers\\chromedriver.exe")),
    (webdriver.Edge("D:\\Selenium\\Drivers\\msedgedriver.exe")),
    # (webdriver.firefox("D:\\Selenium\\Drivers\\geckodriver.exe")),
    ]

APP_URL = "http://127.0.0.1:8000/"
PRODUCT_URL = "http://127.0.0.1:8000/shop/product/testingwebdriver/"

for driver in DRIVER_PATTERNS:
    my_browser = driver

    my_browser.get(APP_URL)
    if my_browser.current_url != APP_URL:
        print("Wrong HTML document loaded")
    else:
        print(APP_URL + " Loaded successfully")
        print("RUNNING manageProduct TESTS")

    my_browser.fullscreen_window()

    # Time to allow all web elements to load
    time.sleep(3)

    # Assert Page Title
    assert "Check out our plants and tools! | PlantOasis" in driver.title
    expected_title = "Check out our plants and tools! | PlantOasis"
    if expected_title == driver.title:
        print("Page title verification success!")

    # Log in to be able to leave review
    login_button = driver.find_element_by_link_text("Sign In").click()

    username_field = driver.find_element_by_id("id_username")
    username_field.send_keys(MODERATOR_USERNAME)
    password_field = driver.find_element_by_id("id_password")
    password_field.send_keys(MODERATOR_PASSWORD)

    login_button = driver.find_element_by_css_selector(".btn:nth-child(6)").click()
    my_browser.fullscreen_window()
    print("LOGIN SUCCESS")

    my_browser.get(PRODUCT_URL)

    # Assert Page Title
    assert "Testing - Plant Oasis" in driver.title
    expected_title = "Testing - Plant Oasis"
    if expected_title == driver.title:
        print("Page title verification success!")
    else:
        print("Page title verification failed :(")

    # Verify Edit product button present
    edit_product = driver.find_element_by_link_text("Edit Product")
    if edit_product:
        print("Edit product button verification success!")
    else:
        print("Edit product button verification failed :(")
    # Click edit product button
    edit_product.click()

    # Assert Page Title
    assert "Edit Testing | PlantOasis" in driver.title
    expected_title = "Edit Testing | PlantOasis"
    if expected_title == driver.title:
        print("Page title verification success!")
    else:
        print("Page title verification failed :(")

    # Verify page header
    page_header = driver.find_element_by_css_selector(".mx-auto:nth-child(1)").text
    expected_header = "Manager Options"
    if page_header:
        print("Page header verification success!")
        if page_header == expected_header:
            print("Page header text verification success!")
    else:
        print("Page header verification failed :(")
    
    # Verify form elements present
    form_price_title = driver.find_element_by_css_selector("#div_id_price > .control-label")
    if form_price_title:
        print("Form price title verification success!")
    else:
        print("Form price title verification failed :(")
    
    form_stock_title = driver.find_element_by_css_selector("#div_id_stock > .control-label")
    if form_stock_title:
        print("Form stock title verification success!")
    else:
        print("Form stock title verification failed :(")
    
    # Inputting updated values
    price_form = driver.find_element_by_id("id_price")
    stock_form = driver.find_element_by_id("id_stock")
    price_form.clear()
    price_form.send_keys("24.99")
    stock_form.clear()
    stock_form.send_keys("18")

    # Verify submit button present
    submit_button = driver.find_element_by_css_selector(".btn-plants")
    if submit_button:
        print("Submit button verification success!")
    else:
        print("Submit button verification failed :(")
    # Click submit button
    submit_button.click()

    # Verify confirmation message
    confirmation = driver.find_element_by_css_selector(".text-center > p").text
    if confirmation:
        print("Confirmation verification success!")
        if confirmation == "Product updated successfully":
            print("Confirmation text verification success!")
    else:
        print("Confirmation verification failed :(")
    
    # Verify back to product button present
    button = driver.find_element_by_css_selector(".btn-outline-plants")
    if button:
        print("Back to product button verification success!")
    else:
        print("Back to product button verification failed :(")
    # Click button
    button.click()

    # Assert Page Title
    assert "Testing - Plant Oasis" in driver.title
    expected_title = "Testing - Plant Oasis"
    if expected_title == driver.title:
        print("Page title verification success!")

    # Verify price has changed
    prod_price = driver.find_element_by_css_selector(".prod-price").text
    if prod_price == "€24.99":
        print("Product price change verification success!")
    else:
        print("Product price change verification failed :(")

# if this isn't the last browser being tested, close the browser.
    if driver != DRIVER_PATTERNS[-1]:
        print("Closing test")
        driver.close()

print("All tests ran")
time.sleep(3)
driver.close()