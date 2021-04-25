"""
Hubert Bukowski | x00161897
2nd Year Project | PlantOasis eCommerce store
Add New Review tests
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
        print("RUNNING addNewReview TESTS")

    my_browser.fullscreen_window()

    # Time to allow all web elements to load
    time.sleep(3)

    # Assert Page Title
    assert "Check out our plants and tools! | PlantOasis" in driver.title
    expected_title = "Check out our plants and tools! | PlantOasis"
    if expected_title == driver.title:
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
    
    # Show login confirmation message if user got redirected home
    if expected_title == driver.title:
        print("LOGIN SUCCESS")

    # Navigate to Test product
    my_browser.get(PRODUCT_URL)
    
    # Assert page title
    assert "Testing - Plant Oasis" in driver.title
    # Verify page title
    expected_title = "Testing - Plant Oasis"
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
    
    # Verify that the "Leave Review" button appears
    review_button = driver.find_element_by_link_text("Leave Review")
    if review_button:
        print("Review button verification success!")
    else:
        print("Review button verification failed :(")
    # Click leave review button
    my_browser.fullscreen_window()
    review_button.click()

    # Assert Page Title
    assert "New Testing Review | PlantOasis" in driver.title
    # Verify Page Title
    expected_title = "New Testing Review | PlantOasis"
    actual_title = driver.title
    if expected_title == actual_title:
        print("Page title verification success!")
    else:
        print("Page title verification failed :(")

    # Verify page header
    page_header = driver.find_element_by_tag_name("h1").text
    expected_header = "New Review"
    if page_header:
        print("Page header present verification success!")
        if page_header == expected_header:
            print("Page header verification success!")
    else:
        print("Page header verification failed :(")

    # Verify form elements present
    review_rating_title = driver.find_elements_by_id("div_id_rating")
    review_title_title = driver.find_elements_by_id("div_id_title")
    review_content_title = driver.find_elements_by_id("div_id_content")
    review_image_title = driver.find_elements_by_id("div_id_image")

    if review_rating_title:
        print("Review Rating title verification success!")
    else:
        print("Review Rating title verification failed :(")

    if review_title_title:
        print("Review Title field title verification success!")
    else:
        print("Review Title field title verification failed :(")

    if review_content_title:
        print("Review content field title verification success!")
    else:
        print("Review content field title verification failed :(")

    if review_image_title:
        print("Review image title verification success!")
    else:
        print("Review image title verification failed :(")

    # Select Review Rating
    select = Select(driver.find_element_by_id("id_rating"))
    select.select_by_visible_text("3")

    # Input Review title
    review_title = driver.find_element_by_id("id_title")
    review_title.send_keys("testing")

    # Input Review content
    review_content = driver.find_element_by_id("id_content")
    review_content.send_keys("webDriver testing")

    """
    NOTE: I didn't include uploading images as I had no idea as to how to do it!,
    PlantOasis doesn't require images to be uploaded with each review or product.
    """

    # Verify Submit button present
    submit_button = driver.find_element_by_css_selector("input:nth-child(8)")
    if submit_button:
        print("Submit button verification success!")
    else:
        print("Submit button verification failed :(")
    my_browser.fullscreen_window()
    # Click submit button
    submit_button.click()

    # Verify notification present
    notification = driver.find_element_by_css_selector(".alert")
    if notification:
        print("Review success notification verification success!")
    else:
        print("Review success notification verification failed :(")

    # if this isn't the last browser being tested, close the browser.
    if driver != DRIVER_PATTERNS[-1]:
        print("Closing test")
        driver.close()

print("All tests ran")
time.sleep(3)
driver.close()