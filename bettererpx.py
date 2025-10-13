from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

userName="TCS22135"

options = Options()
options.add_argument("--headless")  # no browser UI
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
driver.get("https://erpx.gpgit.com/erp/academic/users/login")

driver.find_element(By.ID, "username").send_keys(userName)
driver.find_element(By.ID, "UserPassword").send_keys(userName)

checkbox = driver.find_element(By.ID, "checkbox_2")

print(checkbox.is_selected())
if not checkbox.is_selected():
    checkbox.click()

print(driver.find_element(By.CLASS_NAME,"btn"))
driver.find_element(By.CLASS_NAME, "btn").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME,"btn").click()
soup=BeautifulSoup(driver.page_source,"html.parser")
print(soup)


# try:
#     time.sleep(2)
#     checkbox=driver.find_element(By.CLASS_NAME,"btn")
#     checkbox.click()
#     soup = BeautifulSoup(driver.page_source, "html.parser") 
#     userName = soup.find("h2", class_="page-title").text
#     print(userName)
# except Exception as e:
#     print(67,e)

# if driver.page_source:
#     print(driver.page_source)
driver.quit()
