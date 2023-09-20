
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# Open the URL
driver = webdriver.Chrome()

original_window = driver.current_window_handle

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
#
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

# Perform swipe up
print('swipe up')

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(4)

try:
    instagram_link = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div[2]/a[1]')
    print('Website is redirecting to instagram_link.....')
    time.sleep(4)
    instagram_link.click()
    driver.switch_to.window(driver.window_handles[5])

    instagram_link = driver.current_url

    print(driver.current_url)

    if instagram_link == "https://www.instagram.com/getstan.app/":
        print('Successfully navigated to the expected URL!................')
    else:
        print(f'Navigation failed. Current URL is {instagram_link}..................')
    time.sleep(4)  # Wait for 4 seconds after clicking

except NoSuchElementException:
    print("Instagram page not found....?")

time.sleep(4)
print('Page is switched to original window.....!')
driver.switch_to.window(original_window)

time.sleep(4)
try:
    youtube_link = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div[2]/a[2]')
    print('Website is redirecting to youtube_link.....')
    time.sleep(4)
    youtube_link.click()
    driver.switch_to.window(driver.window_handles[6])

    youtube_link = driver.current_url

    print(driver.current_url)

    if youtube_link == "https://www.youtube.com/@Not_Just_a_Fan":
        print('Successfully navigated to the expected URL!................')
    else:
        print(f'Navigation failed. Current URL is {youtube_link}................')
    time.sleep(4)  # Wait for 4 seconds to let the action complete

except NoSuchElementException:
    print("youtube page not found....?")

time.sleep(4)
print('Page is switched to original window....')
driver.switch_to.window(original_window)

time.sleep(4)

try:
    twitter_link = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div[2]/a[3]')
    print('Website is redirecting to twitter_link.....')
    time.sleep(4)
    twitter_link.click()
    driver.switch_to.window(driver.window_handles[7])
    twitter_link = driver.current_url

    print(driver.current_url)

    if twitter_link == "https://twitter.com/getstanapp":
        print('Successfully navigated to the expected URL!................')
    else:
        print(f'Navigation failed. Current URL is {twitter_link}..................')
    time.sleep(4)  # Wait for 4 seconds to let the action complete

except NoSuchElementException:
    print("Twitter page not found")

time.sleep(4)
print('Page is switched to original window....')
driver.switch_to.window(original_window)

time.sleep(4)


try:
    discord_link = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div[2]/a[4]')
    print('Website is redirecting to discord_link.....')
    time.sleep(4)
    discord_link.click()
    driver.switch_to.window(driver.window_handles[8])
    discord_link = driver.current_url

    print(driver.current_url)

    if discord_link == "https://discord.com/invite/AvrWnhMSHg":
        print('Successfully navigated to the expected URL!................')
    else:
        print(f'Navigation failed. Current URL is {discord_link}..................')
    time.sleep(4)  # Wait for 4 seconds to let the action complete

except NoSuchElementException:
    print("Discord page not found....")

time.sleep(4)
print('Page is switched to original window ....')
driver.switch_to.window(original_window)

time.sleep(4)

try:
    terms_and_conditions = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/a[1]')
    print('Website is redirecting to Terms and conditions page ...!')
    time.sleep(4)
    terms_and_conditions.click()
    driver.switch_to.window(driver.window_handles[9])
    terms_and_conditions = driver.current_url

    print(driver.current_url)

    if terms_and_conditions == "https://web3.getstan.app/terms&conditions":
        print('Successfully navigated to the expected URL!................')
    else:
        print(f'Navigation failed. Current URL is {terms_and_conditions}..................')
    time.sleep(4)  # Wait for 4 seconds to let the action complete
except NoSuchElementException:
    print("Terms and conditions page not found....")

time.sleep(4)
print('Page is switched to original window...')
driver.switch_to.window(original_window)

time.sleep(4)

try:
    privacy_policy = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/a[2]')
    print('Website is redirecting to Privacy Policy page ...!')
    time.sleep(4)
    privacy_policy.click()
    driver.switch_to.window(driver.window_handles[10])
    privacy_policy = driver.current_url

    print(driver.current_url)

    if privacy_policy == "https://web3.getstan.app/privacy-policy":
        print('Successfully navigated to the expected URL!................')
    else:
        print(f'Navigation failed. Current URL is {privacy_policy}..................')
    time.sleep(4)  # Wait for 4 seconds to let the action complete
except NoSuchElementException:
    print("Privacy Policy page  not found....!")

time.sleep(4)
print('Page is switched to original window..')
driver.switch_to.window(original_window)

time.sleep(4)

time.sleep(4)
driver.execute_script("window.scrollTo(0, 0);")
print('swipe down..! ')


print('Successfully closed the browser ... !')
driver.quit()

# Perform some clicks and type something (this part will depend on your screen resolution and browser layout)
# pyautogui.click(x=400, y=400)
# pyautogui.typewrite('Hello World!')
#
