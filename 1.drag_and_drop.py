# Drag and drop the item using selenium automation
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://jqueryui.com/resources/demos/droppable/default.html")


source_element = driver.find_element("id", "draggable")
target_element = driver.find_element("id", "droppable")

action_chains = ActionChains(driver)
action_chains.drag_and_drop(source_element, target_element).perform()

driver.quit()
