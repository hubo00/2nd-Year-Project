"""
Hubert Bukowski | x00161897
2nd Year Project | PlantOasis eCommerce store
Wishlist Navigation tests
NOTE: This test requires the 'addNewProduct' test to be completed beforehand
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
        print("RUNNING wishlistNavigation TESTS")

    my_browser.fullscreen_window()

    # Time to allow all web elements to load
    time.sleep(3)

    # Assert Page Title
    assert "Check out our plants and tools! | PlantOasis" in driver.title
    # Verify Page Title
    expected_title = "Check out our plants and tools! | PlantOasis"
    if expected_title == driver.title:
        print("Page title verification success!")
    else:
        print("Page title verification failed :(")

    # Log in as manager to be able to add new product
    login_button = driver.find_element_by_link_text("Sign In").click()

    username_field = driver.find_element_by_id("id_username")
    username_field.send_keys(MODERATOR_USERNAME)
    password_field = driver.find_element_by_id("id_password")
    password_field.send_keys(MODERATOR_PASSWORD)

    login_button = driver.find_element_by_css_selector(".btn:nth-child(6)").click()
    my_browser.fullscreen_window()
    print("LOGIN SUCCESS")

    # Verify wishlist button present in navbar
    wishlist_button = driver.find_element_by_css_selector(".fa-heart")
    if wishlist_button:
        print("Navbar wishlist icon verification success!")
    else:
        print("Navbar wishlist icon verification failed :(")
    # click wishlist icon
    wishlist_button = driver.find_element_by_css_selector(".fa-heart").click()

    # Asserting Page title
    assert "hubo00's_wishlist - Plant Oasis" in driver.title
    expected_title = "hubo00's_wishlist - Plant Oasis"
    if expected_title == driver.title:
        print("Page title verification success!")
    else:
        print("Page title verification failed :(")
    
    # Verifying page header
    page_header = driver.find_element_by_css_selector("h1").text
    if page_header:
        print("Page header verification success!")
        if page_header == "Your Wishlist":
            print("Page header text verification success!")
        else:
            print("Page header text verification failed :(")
    else:
        print("Page header verification failed :(")
    
    # Verifying that empty wishlist message appears
    empty_message = driver.find_element_by_css_selector(".row > p").text
    if empty_message:
        print("Empty wishlist message verification success!")
        if empty_message == "You have no items in your wishlist":
            print("Message contents verification success!")
        else:
            print("Message contents verification failed :(")
    else:
        print("Empty wishlist message verification failed :(")

    # Go to Test Product
    my_browser.get(PRODUCT_URL)
    my_browser.fullscreen_window()
    
    # Asserting Page title
    assert "Testing - Plant Oasis" in driver.title
    expected_title = "Testing - Plant Oasis"
    if expected_title == driver.title:
        print("Page title verification success!")
    else:
        print("Page title verification failed :(")

    # Verify wishlist button present ( and shows that item not in wishlist )
    wishlist_button = driver.find_element_by_css_selector("a > .far")
    if wishlist_button:
        print("Icon for empty heart verification success!")
    else:
        print("Icon for empty heart verification failed :(")
    # Click Button
    wishlist_button.click()

    # Asserting Page title
    assert "hubo00's_wishlist - Plant Oasis" in driver.title
    expected_title = "hubo00's_wishlist - Plant Oasis"
    if expected_title == driver.title:
        print("Page title verification success!")
    else:
        print("Page title verification failed :(")

    # Verify notification present
    notification = driver.find_element_by_xpath("//ul/div/div")
    if notification:
        print("Edit success notification verification success!")
    else:
        print("Edit success notification verification failed :(")

    # Verify Product elements appear in wishlist
    product_title = driver.find_element_by_css_selector(".col-9 td > h3")
    product_altName = driver.find_element_by_css_selector(".col-9 h4")
    product_category = driver.find_element_by_css_selector("h5")
    product_price = driver.find_element_by_css_selector("h3:nth-child(2)")
    product_inStock = driver.find_element_by_css_selector(".fa-check-circle")
    date_added = driver.find_element_by_css_selector("p:nth-child(4)")
    if product_title:
        print("Product title verification success!")
    else:
        print("Product title verification failed :(")
    if product_altName:
        print("Product alt name verification success!")
    else:
        print("Product alt name verification failed :(")
    if product_category:
        print("Product category verification success!")
    else:
        print("Product category verification failed :(")
    if product_price:
        print("Product price verification success!")
    else:
        print("Product price verification failed :(")
    if product_inStock:
        print("Product stock notification verification success!")
    else:
        print("Product stock notification verification failed :(")
    if date_added:
        print("Date added verification success!")
    else:
        print("Date added verification failed :(")

    # Go to Product Out of Stock
    my_browser.get("http://127.0.0.1:8000/shop/product/electric-hedge-trimmerhonda/")

    # Verify wishlist button present
    wishlist_button = driver.find_element_by_css_selector("a > .far")
    if wishlist_button:
        print("Icon for empty heart verification success!")
    else:
        print("Icon for empty heart verification failed :(")
    # Click Button
    wishlist_button.click()

    # Verify notification present
    notification = driver.find_element_by_css_selector(".alert")
    if notification:
        print("Edit success notification verification success!")
    else:
        print("Edit success notification verification failed :(")

    # Verify Out of Stock product notification
    product_outStock = driver.find_element_by_css_selector(".fa-times-circle")
    if product_outStock:
        print("Product Stock notification verification success!")
    else:
        print("Product stock notification verification failed :(")
    
    # Verify In stock Add to cart buttons present
    add_to_cart = driver.find_element_by_css_selector("tr:nth-child(1) .cart-button > .fas")
    if add_to_cart:
        print("Add to cart button verification success!")
    else:
        print("Add to cart button verification failed :(")
    
    # Verify Remove buttons present
    remove_one = driver.find_element_by_css_selector("tr:nth-child(1) .cart-trash > .fas")
    remove_two = driver.find_element_by_css_selector("tr:nth-child(2) .cart-trash > .fas")
    if remove_one:
        print("Product one remove button verification success!")
    else:
        print("Product one remove button verification failed :(")
    if remove_two:
        print("Product two remove button verification success!")
    else:
        print("Product Two remove button verification failed :(")
    
    # Remove out of stock product from wishlist
    remove_two.click()

    # Verify notification present
    notification = driver.find_element_by_css_selector(".alert")
    if notification:
        print("Edit success notification verification success!")
    else:
        print("Edit success notification verification failed :(")
    
    # Add Last Product to Cart
    add_to_cart = driver.find_element_by_css_selector("tr:nth-child(1) .cart-button > .fas").click()

    # Asserting Page title
    assert "Cart - Plant Oasis" in driver.title
    expected_title = "Cart - Plant Oasis"
    if expected_title == driver.title:
        print("Page title verification success!")
    else:
        print("Page title verification failed :(")
    
    # Verify product name in cart is "Testing"
    product_title = driver.find_element_by_css_selector("h3").text
    if product_title:
        print("Product title verification success!")
        if product_title == "Testing":
            print("Product title contents verification success!")
        else:
            print("Product title content verification failed :(")
    else:
        print("Product title verification failed :(")
    
    # if this isn't the last browser being tested, close the browser.
    if driver != DRIVER_PATTERNS[-1]:
        print("Closing test")
        driver.close()

print("All tests ran")
time.sleep(3)
driver.close()   
    