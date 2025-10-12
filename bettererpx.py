from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

userName="TCS22077"

options = Options()
options.add_argument("--headless")  # no browser UI
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
driver.get("https://erpx.gpgit.com/erp/academic/users/login")

driver.find_element(By.ID, "username").send_keys(userName)
driver.find_element(By.ID, "UserPassword").send_keys(userName)

checkbox = driver.find_element(By.ID, "checkbox_2")
if not checkbox.is_selected():
    checkbox.click()
try:
    driver.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(2)
    checkbox=driver.find_element(By.CLASS_NAME,"btn")
    checkbox.click()
except Exception as e:
    print(e)

# if driver.page_source:
#     print(driver.page_source)
driver.quit()
