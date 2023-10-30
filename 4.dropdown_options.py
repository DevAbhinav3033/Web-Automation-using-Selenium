# Get the list of all the options present in the dropdown using selenium automation
from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()

driver.get("https://www.amazon.com")  # using amazon website

dropdown = Select(driver.find_element("xpath",
                                      "//select[@id='searchDropdownBox']"))
options = dropdown.options

for index, option in enumerate(options):
    print(option.text)

driver.quit()
