import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def test_title_name():
    driver_chrome = Chrome('/usr/lib/chromium-browser/chromedriver')
    driver_chrome.maximize_window()
    driver_chrome.get('https://uk.wikipedia.org/wiki/Python')
    actual_title = driver_chrome.title
    expected_title = 'Python — Вікіпедія'
    assert actual_title == expected_title
    driver_chrome.quit()


def test_login_open_login_page():
    driver_chrome = Chrome('/usr/lib/chromium-browser/chromedriver')
    driver_chrome.maximize_window()
    driver_chrome.get('https://uk.wikipedia.org/wiki/Python')
    login_button_locator = '//li[@id="pt-login"]/a'
    login_button_element = driver_chrome.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    time.sleep(1)
    text_in_page_locator = '//div/h1[@id="firstHeading"]'
    actual_text_in_page = driver_chrome.find_element(By.XPATH, text_in_page_locator).text
    expected_text_in_page = 'Вхід до системи'
    assert actual_text_in_page == expected_text_in_page
    driver_chrome.quit()


def test_login():
    url = 'https://uk.wikipedia.org/w/index.php?title=%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0:%D0%92%D1%85%D1%96%D0%B4&returnto=Python'
    login = '1iriver1'
    password = '1iriver11234567890'
    driver_chrome = Chrome('/usr/lib/chromium-browser/chromedriver')
    driver_chrome.maximize_window()
    driver_chrome.get(url)
    time.sleep(1)

    # Enter Login
    login_locator = '//input[@name="wpName"]'
    login_element = driver_chrome.find_element(By.XPATH, login_locator)
    login_element.clear()
    login_element.send_keys(login)

    # Enter Password
    password_locator = '//input[@name="wpPassword"]'
    password_element = driver_chrome.find_element(By.XPATH, password_locator)
    password_element.clear()
    password_element.send_keys(password)
    time.sleep(1)

    # Login
    login_button_element_by_xpath = '//div/button'
    login_button_element_by_xpath = driver_chrome.find_element(By.XPATH, login_button_element_by_xpath)
    login_button_element_by_xpath.click()

    # registration check
    check_user_locator = '//li[@id="pt-userpage"]//span'
    actual_user = driver_chrome.find_element(By.XPATH, check_user_locator).text
    expected_user = login
    assert actual_user == expected_user
    driver_chrome.quit()
