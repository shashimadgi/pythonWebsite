
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager



driver=webdriver.Chrome("C:\\Users\\user\\Downloads\\chromedriver.exe")
driver.maximize.window()
driver.get("https://stan-profile-git-stage-get-stan.vercel.app/login")
print("application title is ",driver.title)
print("application url is ",driver.current_url)
driver.quit()