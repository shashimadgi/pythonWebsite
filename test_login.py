import pytest
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



@pytest.mark.regression
def testLogin():
    # Open the URL
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    original_window = driver.current_window_handle
    time.sleep(3)
    print('web3 website launched succesfully')
    driver.get('https://web3.getstan.app/')

    time.sleep(4)

    try:
        blogs = driver.find_element(By.XPATH, "/html/body/section/div/a[1]")
        print('Blogs page opened successfully.....')
        blogs.click()
        time.sleep(4)

        driver.switch_to.window(driver.window_handles[1])

        blogs = driver.current_url

        print(driver.current_url)

        if blogs == "https://medium.com/stan-app":
            print('Successfully navigated to the expected URL!................')
        else:
            print(f'Navigation failed. Current URL is {blogs}..................')

    except NoSuchElementException:
        print("Blogs page not found.....?")

    time.sleep(4)

    print('Page is switched to original window....')
    driver.switch_to.window(original_window)
    # Wait for the browser to open
    time.sleep(5)

    try:
        careers = driver.find_element(By.XPATH, "/html/body/section/div/a[2]")
        print('Careers page opened successfully.....')
        careers.click()
        driver.switch_to.window(driver.window_handles[2])

        careers = driver.current_url

        print(driver.current_url)

        if careers == "https://getstanapp.notion.site/Join-us-in-building-the-next-gen-Fan-engagement-platform-Stan" \
                      "-8dbf1aa241904fcb9bb30915ce468279":
            print('Successfully navigated to the expected URL!................')
        else:
            print(f'Navigation failed. Current URL is {careers}..................')



    except NoSuchElementException:
        print("Careers page not found....?")

    time.sleep(4)

    print('Page is switched to original window....')
    driver.switch_to.window(original_window)

    time.sleep(4)
    print('Login successful')


def testLogoff():
    print('Login unsuccessful')


def testCalaculation():
    print('Login notsuccessful')
    assert 2 + 2 == 4
