"""
Hubert Bukowski | x00161897
2nd Year Project | PlantOasis eCommerce store
Categories page tests
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
        print("RUNNING Category TESTS")

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


    # Assert category buttons
    category_button = driver.find_element_by_link_text("Indoor Plants")
    if category_button:
        print("Indoor Plants button assertion success!")
    else:
        print("Indoor Plants button assertion failed :(")

    category_button = driver.find_element_by_link_text("Outdoor Plants")
    if category_button:
        print("Outdoor Plants button assertion success!")
    else:
        print("Outdoor Plants button assertion failed :(")

    category_button = driver.find_element_by_css_selector(".navbar-nav:nth-child(1) > .nav-item:nth-child(3) > .nav-link")
    if category_button:
        print("Plant Pots button assertion success!")
    else:
        print("Plant Pots button assertion failed :(")

    category_button = driver.find_element_by_link_text("Tools")
    if category_button:
        print("Tools button assertion success!")
    else:
        print("Tools button assertion failed :(")

    # Enter Indoor Plants category
    category_button = driver.find_element_by_link_text("Indoor Plants").click()

    # Assert Page Title
    assert "Indoor Plants | PlantOasis" in driver.title
    # Verify Page Title
    expected_title = "Indoor Plants | PlantOasis"
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
    
    # Enter Outdoor Plants category
    category_button = driver.find_element_by_link_text("Outdoor Plants").click()

    # Assert Page Title
    assert "Outdoor Plants | PlantOasis" in driver.title
    # Verify Page Title
    expected_title = "Outdoor Plants | PlantOasis"
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

    # Enter Plant Pots category
    category_button = driver.find_element_by_css_selector(".navbar-nav:nth-child(1) > .nav-item:nth-child(3) > .nav-link").click()

    # Assert Page Title
    assert "Plant pots | PlantOasis" in driver.title
    # Verify Page Title
    expected_title = "Plant pots | PlantOasis"
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
    
    # Enter Tools category
    category_button = driver.find_element_by_partial_link_text("Tools").click()

    # Assert Page Title
    print(driver.title)
    assert "Tools | PlantOasis" in driver.title
    # Verify Page Title
    expected_title = "Tools | PlantOasis"
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

    # if this isn't the last browser being tested, close the browser.
    if driver != DRIVER_PATTERNS[-1]:
        print("Closing test")
        driver.close()

print("All tests ran")
time.sleep(3)
driver.close()