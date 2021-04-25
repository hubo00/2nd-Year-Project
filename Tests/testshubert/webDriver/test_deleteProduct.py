"""
Hubert Bukowski | x00161897
2nd Year Project | PlantOasis eCommerce store
Delete Product tests
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
        print("RUNNING deleteProduct TESTS")

    my_browser.fullscreen_window()

    # Time to allow all web elements to load
    time.sleep(3)

    # Assert Page Title
    assert "Check out our plants and tools! | PlantOasis" in driver.title
    expected_title = "Check out our plants and tools! | PlantOasis"
    if expected_title == driver.title:
        print("Page title verification success!")

    # Log in as manager to be able to delete product
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

    # Verify Delete product button present
    delete_product = driver.find_element_by_link_text("Delete Product")
    if delete_product:
        print("Delete product button verification success!")
    else:
        print("Delete product button verification failed :(")
    # Click delete product button
    delete_product.click()

    # Assert Page Title
    assert "Delete Testing | PlantOasis" in driver.title
    expected_title = "Delete Testing | PlantOasis"
    if expected_title == driver.title:
        print("Page title verification success!")
    else:
        print("Page title verification failed :(")

    # Verify page header
    page_header = driver.find_element_by_css_selector(".text-center").text
    if page_header:
        print("Page header verification success!")
        if page_header == "Delete Testing":
            print("Page header text verification success!")
    else:
        print("Page header verification failed :(")

    # Verify Confirmation & Cancel buttons
    confirm_button = driver.find_element_by_css_selector(".btn-danger")
    cancel_button = driver.find_element_by_link_text("Cancel")
    if confirm_button:
        print("Delete confirmation button verification success!")
    else:
        print("Delete confirmation button verification failed :(")
    
    if cancel_button:
        print("Delete cancel button verification success!")
    else:
        print("Delete cancel button verification failed :(")
    
    # Cancel Deletion
    cancel_button = driver.find_element_by_link_text("Cancel").click()

    # Assert Page to make sure product still exists
    assert "Testing - Plant Oasis" in driver.title
    expected_title = "Testing - Plant Oasis"
    if expected_title == driver.title:
        print("Page title verification success!")
    else:
        print("Page title verification failed :(")

    # Click Delete product button
    delete_product = driver.find_element_by_link_text("Delete Product").click()

    # Click delete confirmation button
    confirm_button = driver.find_element_by_css_selector(".btn-danger").click()

    # Assert user got redirected to the home-page
    assert "Check out our plants and tools! | PlantOasis" in driver.title
    expected_title = "Check out our plants and tools! | PlantOasis"
    if expected_title in driver.title:
        print("Page title Assertion success!")

    # Verify notification appears
    notification = driver.find_element_by_css_selector(".alert")
    if notification:
        print("Delete success notification verification success!")
    else:
        print("Delete success notification verification failed :(")

    # if this isn't the last browser being tested, close the browser.
    if driver != DRIVER_PATTERNS[-1]:
        print("Closing test")
        driver.close()

print("All tests ran")
time.sleep(3)
driver.close()