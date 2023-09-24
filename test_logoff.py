import pytest
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@pytest.mark.sanity
def testLogin():
    # Open the URL
    driver = webdriver.Chrome()

    original_window = driver.current_window_handle
    time.sleep(3)
    print('web3 website launched succesfully')
    driver.get('https://web3.getstan.app/')

    time.sleep(4)
    try:
        playstore_link = driver.find_element(By.XPATH, "/html/body/div[1]/section/section/div[1]/div/a[1]")
        print('Website is redirecting to Google Playstore.....')
        time.sleep(5)
        playstore_link.click()
        driver.switch_to.window(driver.window_handles[3])

        playstore_link = driver.current_url

        print(driver.current_url)

        if playstore_link == "https://play.google.com/store/apps/details?id=com.getstan&inviteCode=STANWEB":
            print('Successfully navigated to the expected URL!................')
        else:
            print(f'Navigation failed. Current URL is {playstore_link}..................')
    except NoSuchElementException:
        print('Google Playstore page  not found....?')

    time.sleep(5)

    print('Page is switched to original window....')
    driver.switch_to.window(original_window)

    time.sleep(5)

    try:
        appstore_link = driver.find_element(By.XPATH, "/html/body/div[1]/section/section/div[1]/div/a[2]")
        print('Website is redirecting to App Store page....')
        time.sleep(4)
        appstore_link.click()
        driver.switch_to.window(driver.window_handles[4])

        appstore_link = driver.current_url

        print(driver.current_url)

        if appstore_link == "https://apps.apple.com/us/app/stan-esports-fan-engagement/id1637869402":
            print('Successfully navigated to the expected URL!................')
        else:
            print(f'Navigation failed. Current URL is {appstore_link}..................')

    except NoSuchElementException:
        print("App Store page not found....?")

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
