"""
Hubert Bukowski | x00161897
2nd Year Project | PlantOasis eCommerce store
Review browsing tests
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
PRODUCT_URL = "http://127.0.0.1:8000/shop/product/adansons-monsteramonstera-adansonii/"

for driver in DRIVER_PATTERNS:
    my_browser = driver

    my_browser.get(APP_URL)
    if my_browser.current_url != APP_URL:
        print("Wrong HTML document loaded")
    else:
        print(APP_URL + " Loaded successfully")
        print("RUNNING reviewBrowsing TESTS")

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

    # Log in to be able to leave review
    login_button = driver.find_element_by_link_text("Sign In").click()

    username_field = driver.find_element_by_id("id_username")
    username_field.send_keys(MODERATOR_USERNAME)
    password_field = driver.find_element_by_id("id_password")
    password_field.send_keys(MODERATOR_PASSWORD)

    login_button = driver.find_element_by_css_selector(".btn:nth-child(6)").click()
    my_browser.fullscreen_window()
    print("LOGIN SUCCESS")

    # Verify that product list appears
    product_boxes = driver.find_elements_by_class_name("home-images")
    if product_boxes:
        print("Product list verification success!")
    else:
        print("Product list verification failed :(")
    # Verify that Single product is there
    specific_product = driver.find_element_by_css_selector(".col-lg-3:nth-child(1) .home-images")
    if specific_product:
        print("Product assertion success!")
    else:
        print("Product assertion failed :(")
    # Enter Product detail page
    my_browser.get(PRODUCT_URL)

    # Assert page title
    assert "Adanson's Monstera - Plant Oasis" in driver.title
    # Verify page title
    expected_title = "Adanson's Monstera - Plant Oasis"
    actual_title = driver.title
    if expected_title == actual_title:
        print("Page title verification success!")
    else:
        print("Page title verification failed :(")

    # Verify that the Review header appears
    review_header = driver.find_element_by_tag_name("h4")
    if review_header:
        print("Review header verification success!")
    else:
        print("Review header verification failed :(")

    # Verify sample Review 1 Elements present
    review_owner = driver.find_element_by_css_selector(".col:nth-child(1) h3")
    review_rating = driver.find_element_by_css_selector(".col:nth-child(1) .fas:nth-child(2)")
    review_title = driver.find_element_by_css_selector(".col:nth-child(1) h4")
    review_content = driver.find_element_by_css_selector(".col:nth-child(1) .row > p")
    review_date = driver.find_element_by_css_selector(".col:nth-child(1) .row:nth-child(4)")
    # No image only
    review_imageNotFound = driver.find_element_by_css_selector(".row:nth-child(1) > .col-6 > p")
    # Review creators, Moderators & Admins only
    review_delete_button = driver.find_element_by_link_text("Delete")
    # Review creators only
    review_edit_button = driver.find_element_by_link_text("Edit")
    # Image present only
    review_image = driver.find_element_by_css_selector(".review-image")
    # Verified purchase only
    review_verifier = driver.find_element_by_id("purchase-verifier")

    if review_owner:
        print("Review owner verification success!")
    else:
        print("Review owner verification failed :(")

    if review_rating:
        print("Review rating verification success!")
    else:
        print("Review rating verification failed :(")

    if review_title:
        print("Review title verification success!")
    else:
        print("Review title verification failed :(")

    if review_content:
        print("Review content verification success!")
    else:
        print("Review content verification failed :(")

    if review_date:
        print("Review date verification success!")
    else:
        print("Review date verification failed :(")

    if review_imageNotFound:
        print("Review imageNotFound verification success!")
    else:
        print("Review imageNotFound verification failed :(")

    if review_delete_button:
        print("Review delete button verification success!")
    else:
        print("Review delete button verification failed!")
    
    if review_edit_button:
        print("Review edit button verification success!")
    else:
        print("Review edit button verification failed :(")
    
    if review_image:
        print("Review image verification success!")
    else:
        print("Review image verification failed :(")

    if review_verifier:
        print("Review verifier verification success!")
    else:
        print("Review verifier verification failed :(")

    # if this isn't the last browser being tested, close the browser.
    if driver != DRIVER_PATTERNS[-1]:
        print("Closing test")
        driver.close()

print("All tests ran")
time.sleep(3)
driver.close()