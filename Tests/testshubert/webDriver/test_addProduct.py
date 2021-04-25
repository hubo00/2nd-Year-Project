"""
Hubert Bukowski | x00161897
2nd Year Project | PlantOasis eCommerce store
Add Product tests
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
        print("RUNNING addProduct TESTS")

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

    # Log in as manager to be able to add new product
    login_button = driver.find_element_by_link_text("Sign In").click()

    username_field = driver.find_element_by_id("id_username")
    username_field.send_keys(MODERATOR_USERNAME)
    password_field = driver.find_element_by_id("id_password")
    password_field.send_keys(MODERATOR_PASSWORD)

    login_button = driver.find_element_by_css_selector(".btn:nth-child(6)").click()
    my_browser.fullscreen_window()
    print("LOGIN SUCCESS")

    # Verify Manage button present in navbar
    manage_button = driver.find_element_by_id("navbardrop")
    if manage_button:
        print("Manage button verification success!")
    else:
        print("Manage button verification failed :(")
    # Click Manage button
    manage_button = driver.find_element_by_css_selector(".fa-users-cog").click()

    # Verify Add product button present in dropdown
    addProduct_button = driver.find_element_by_link_text("Add Product")
    if addProduct_button:
        print("Add product button verification success!")
    else:
        print("Add product button verification failed :(")
    # Click Add product button
    addProduct_button.click()

    # Assert Page Title
    assert "New Product | PlantOasis" in driver.title
    expected_title = "New Product | PlantOasis"
    if expected_title == driver.title:
        print("Page title assertion success!")

    # Verify page header
    page_header = driver.find_element_by_css_selector(".text-center").text
    expected_header = "New Product"
    if page_header:
        print("Page header verification success!")
        if page_header == expected_header:
            print("Pager header text verification success!")
    else:
        print("Page header verification failed :(")
    
    # Verify form elements present
    # Verifying form field titles
    FORM_TITLES = [
        "Name*",
        "Name alt",
        "Category*",
        "Description",
        "Price*",
        "Image",
        "Stock*"]
    form_titles = driver.find_elements_by_css_selector(".control-label")
    form_titles_text = []
    for title in form_titles:
        form_titles_text.append(title.text)
    if form_titles_text:
        print("Form title verification success!")
    else:
        print("Form title verification failed :(")
    for index, title in enumerate(form_titles_text):
        if title == FORM_TITLES[index]:
            print("Form title text verification success!")
        else:
            print("Form title text verification failed :(")

    # Verifying & Entering form fields
    name_field = driver.find_element_by_id("id_name")
    nameAlt_field = driver.find_element_by_id("id_name_alt")
    category_field = Select(driver.find_element_by_id("id_category"))
    description_field = driver.find_element_by_id("id_description")
    price_field = driver.find_element_by_id("id_price")
    image_field = driver.find_element_by_id("id_image")
    stock_field = driver.find_element_by_id("id_stock")

    if name_field:
        print("Name field verification success!")
        name_field.send_keys("Testing")
    else:
        print("Name field verification failed :(")

    if nameAlt_field:
        print("Alt name field verification success!")
        nameAlt_field.send_keys("webDriver")
    else:
        print("Alt name field verification failed :(")

    if category_field:
        print("Category field verification success!")
        category_field.select_by_visible_text("Shears") # For testing only
    else:
        print("Category field verification failed :(")
    
    if description_field:
        print("Description field verification success!")
        description_field.send_keys("Testing add Product in webDriver")
    else:
        print("Description field verification failed :(")

    if price_field:
        print("Price field verification success!")
        price_field.send_keys("42.99")
    else:
        print("Price field verification failed :(")
    
    if image_field:
        print("Image upload button verification success!")
    else:
        print("Image upload button verification failed :(")
    
    if stock_field:
        print("Stock field verification success!")
        stock_field.send_keys("14")
    else:
        print("Stock field verification failed :(")
    
    # Verify submit button present
    submit_button = driver.find_element_by_xpath("//input[@value='Submit']")
    if submit_button:
        print("Submit button verification success!")
    else:
        print("Submit button verification failed :(")
    # Click submit button
    submit_button.click()

    # Verify notification present
    notification = driver.find_element_by_css_selector(".alert")
    if notification:
        print("Review success notification verification success!")
    else:
        print("Review success notification verification failed :(")


    # Verify new product has been created
    my_browser.get(PRODUCT_URL)
    # Assert Page Title
    assert "Testing - Plant Oasis" in driver.title
    expected_title = "Testing - Plant Oasis"
    if expected_title == driver.title:
        print("Page title assertion success!")
        print("PRODUCT CREATED SUCCESSFULLY")

    # if this isn't the last browser being tested, close the browser.
    if driver != DRIVER_PATTERNS[-1]:
        print("Closing test")
        driver.close()

print("All tests ran")
time.sleep(3)
driver.close()