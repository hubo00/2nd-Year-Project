"""
Hubert Bukowski | x00161897
2nd Year Project | PlantOasis eCommerce store
subCategories page tests
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
        print("RUNNING subCategory TESTS")

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

    
    # Verify that product list appears
    product_boxes = driver.find_elements_by_class_name("home-images")
    if product_boxes:
        print("Product list verification success!")
    else:
        print("Product list verification failed :(")

    # Verify that Indoor Plants buttons are present
    category_button = driver.find_element_by_link_text("Indoor Plants")
    if category_button:
        print("Indoor Plants button verification success!")
    else:
        print("Indoor Plants button verification failed :(")
    # Enter Indoor Plants
    category_button.click()

    # Assert Page Title
    assert "Indoor Plants | PlantOasis" in driver.title
    # Verify Page Title
    expected_title = "Indoor Plants | PlantOasis"
    actual_title = driver.title
    if expected_title == actual_title:
        print("Page title verification success!")
    else:
        print("Page title verification failed :(")

    # Verify subCategory buttons are present
    sample_button1 = driver.find_element_by_link_text("Calathea")
    sample_button2 = driver.find_element_by_link_text("Dracaenae")
    sample_button3 = driver.find_element_by_link_text("Maranta")

    if sample_button1:
        print("subCategory button 1 verification success!")
    else:
        print("subCategory button 1 verification failed :(")

    if sample_button2:
        print("subCategory button 2 verification success!")
    else:
        print("subCategory button 2 verification failed :(")

    if sample_button3:
        print("subCategory button 3 verification success!")
    else:
        print("subCategory button 3 verification failed :(")
    # Enter first sample subCategory
    sample_button1.click()

    # Assert Page Title
    assert "Calathea | PlantOasis" in driver.title
    # Verify Page Title
    expected_title = "Calathea | PlantOasis"
    actual_title = driver.title
    if expected_title == actual_title:
        print("Page title verification success!")
    else:
        print("Page title verification failed :(")

    # Verify page header reads "Calathea"
    page_header = driver.find_element_by_tag_name("h1").text
    expected_header = "Calathea"
    if page_header == expected_header:
        print("Page header verification success!")
    else:
        print("Page header verfication failed :(")

    # Verify that product list appears
    product_boxes = driver.find_elements_by_class_name("home-images")
    if product_boxes:
        print("Product list verification success!")
    else:
        print("Product list verification failed :(")

    # Return to Indoor Plants category
    category_button = driver.find_element_by_link_text("Indoor Plants")
    category_button.click()

    # Enter second sample subCategory
    sample_button2 = driver.find_element_by_link_text("Dracaenae")
    sample_button2.click()

    # Assert Page Title
    assert "Dracaenae | PlantOasis" in driver.title
    # Verify Page Title
    expected_title = "Dracaenae | PlantOasis"
    actual_title = driver.title
    if expected_title == actual_title:
        print("Page title verification success!")
    else:
        print("Page title verification failed :(")

    # Verify page header reads "Dracaenae"
    page_header = driver.find_element_by_tag_name("h1").text
    expected_header = "Dracaenae"
    if page_header == expected_header:
        print("Page header verification success!")
    else:
        print("Page header verfication failed :(")

    # Verify that product list appears
    product_boxes = driver.find_elements_by_class_name("home-images")
    if product_boxes:
        print("Product list verification success!")
    else:
        print("Product list verification failed :(")

    # Return to Indoor Plants category
    category_button = driver.find_element_by_link_text("Indoor Plants")
    category_button.click()

    # Enter third sample subCategory
    sample_button3 = driver.find_element_by_link_text("Maranta")
    sample_button3.click()

    # Assert Page Title
    assert "Maranta | PlantOasis" in driver.title
    # Verify Page Title
    expected_title = "Maranta | PlantOasis"
    actual_title = driver.title
    if expected_title == actual_title:
        print("Page title verification success!")
    else:
        print("Page title verification failed :(")

    # Verify page header reads "Maranta"
    page_header = driver.find_element_by_tag_name("h1").text
    expected_header = "Maranta"
    if page_header == expected_header:
        print("Page header verification success!")
    else:
        print("Page header verfication failed :(")

    # Verify that product list appears
    product_boxes = driver.find_elements_by_class_name("home-images")
    if product_boxes:
        print("Product list verification success!")
    else:
        print("Product list verification failed :(")

# if this isn't the last browser being tested, close the browser.
    if driver != DRIVER_PATTERNS[-1]:
        print("Closing test")
        driver.close()

print("All tests ran")
time.sleep(3)
driver.close()