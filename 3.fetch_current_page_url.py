# Fetch the url of the current website using selenium
from selenium import webdriver

driver = webdriver.Chrome()


# the address whose url needs to be fetched
driver.get("https://mail.google.com/mail/u/0/#inbox")

current_url = driver.current_url
print("Current URL: " + current_url)

driver.quit()
