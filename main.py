from selenium import webdriver
import os

options = webdriver.ChromeOptions()
path = os.path.abspath("account-data/account_3")
options.add_argument("user-data-dir=" + path)
# other options...
chromedriver = "./webdrivers/chrome"
driver = webdriver.Chrome(executable_path=chromedriver, options=options)

# do stuff...
driver.close()