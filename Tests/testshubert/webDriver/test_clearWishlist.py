"""
Hubert Bukowski | x00161897
2nd Year Project | PlantOasis eCommerce store
Edit Review tests
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

for driver in DRIVER_PATTERNS:
    my_browser = driver

    my_browser.get(APP_URL)
    if my_browser.current_url != APP_URL:
        print("Wrong HTML document loaded")
    else:
        print(APP_URL + " Loaded successfully")
        print("RUNNING editReview TESTS")

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

    # Log in to be able to edit review
    login_button = driver.find_element_by_link_text("Sign In").click()

    username_field = driver.find_element_by_id("id_username")
    username_field.send_keys(MODERATOR_USERNAME)
    password_field = driver.find_element_by_id("id_password")
    password_field.send_keys(MODERATOR_PASSWORD)

    login_button = driver.find_element_by_css_selector(".btn:nth-child(6)").click()
    my_browser.fullscreen_window()
    print("LOGIN SUCCESS")

    # Visit 3 different products and add them to cart
    prod_one = "http://127.0.0.1:8000/shop/product/dragon-treedracaena-marginata/"
    prod_two = "http://127.0.0.1:8000/shop/product/plastic-pot28cmd-x-12cmh/"
    prod_three = "http://127.0.0.1:8000/shop/product/madonna-lilylilium-candidum/"

    # Visit product #1
    my_browser.get(prod_one)
    # Verify wishlist button present
    wishlist_button = driver.find_element_by_css_selector("a > .far")
    if wishlist_button:
        print("Icon for empty heart verification success!")
    else:
        print("Icon for empty heart verification failed :(")
    # Click Button
    wishlist_button.click()

    # Verify notification present
    notification = driver.find_element_by_xpath("//ul/div/div")
    if notification:
        print("Edit success notification verification success!")
    else:
        print("Edit success notification verification failed :(")
    
    # Visit product #2
    my_browser.get(prod_two)
    # Verify wishlist button present
    wishlist_button = driver.find_element_by_css_selector("a > .far")
    if wishlist_button:
        print("Icon for empty heart verification success!")
    else:
        print("Icon for empty heart verification failed :(")
    # Click Button
    wishlist_button.click()

    # Verify notification present
    notification = driver.find_element_by_xpath("//ul/div/div")
    if notification:
        print("Edit success notification verification success!")
    else:
        print("Edit success notification verification failed :(")
    
    # Visit product #3
    my_browser.get(prod_three)
    # Verify wishlist button present
    wishlist_button = driver.find_element_by_css_selector("a > .far")
    if wishlist_button:
        print("Icon for empty heart verification success!")
    else:
        print("Icon for empty heart verification failed :(")
    # Click Button
    wishlist_button.click()

    # Verify notification present
    notification = driver.find_element_by_xpath("//ul/div/div")
    if notification:
        print("Edit success notification verification success!")
    else:
        print("Edit success notification verification failed :(")
    
    # Verifying 3 products appear in wishlist
    prod_one = driver.find_element_by_css_selector(".col-9 tr:nth-child(1) > td > h3")
    prod_two = driver.find_element_by_css_selector("tr:nth-child(2) > td > h3")
    prod_three = driver.find_element_by_css_selector("tr:nth-child(3) > td > h3")

    if prod_one:
        print("Product one verification success!")
    else:
        print("Product one verification failed :(")
    
    if prod_two:
        print("Product two verification success!")
    else:
        print("Product two verification failed :(")

    if prod_three:
        print("Product three verification success!")
    else:
        print("Product three verification failed :(")
    
    # Verify Clear wishlist button present
    button = driver.find_element_by_css_selector(".btn-danger")
    if button:
        print("Clear wishlist button verification success!")
    else:
        print("Clear wishlist button verification failed :(")
    
    my_browser.fullscreen_window()
    button.click()
    alert = driver.switch_to.alert
    alert.accept()

    # if this isn't the last browser being tested, close the browser.
    if driver != DRIVER_PATTERNS[-1]:
        print("Closing test")
        driver.close()

print("All tests ran")
time.sleep(3)
driver.close()   
    