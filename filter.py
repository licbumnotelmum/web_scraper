from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import sqlDatabase as sql
import time

options = Options()
options.add_argument("--headless")  # no browser UI
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
#TBT3   JAN
#TCS22135

start=116
entries=200
field = "TCS22"


limit = start+entries
for i in range(start , limit):               #using 12 as other return an error
 
    roll="00"+str(i)
    roll=roll[-3:]      #000 001 002 003

    userID = field + roll       #TCS22000 TCS22001 TCS22002 TCS22003
    print(userID)

    driver.get("https://erpx.gpgit.com/erp/academic/users/login")

    driver.find_element(By.ID, "username").send_keys(userID)                    #login creds
    driver.find_element(By.ID, "UserPassword").send_keys(userID)

    checkbox = driver.find_element(By.ID, "checkbox_2")                         #checkbox for keep me loged in
    if not checkbox.is_selected():
        checkbox.click()

    try:
        driver.find_element(By.CLASS_NAME, "btn").click()                       #clicks login button
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, "html.parser")                                 #inserts username and id into mysql database
        userName = soup.find("h2", class_="page-title").text
        sql.insertUserName(userID , userName)                          

        completeDetails=driver.find_element(By.CLASS_NAME,"btn")                 #finds button for complete details
        completeDetails.click()

        soup = BeautifulSoup(driver.page_source, "html.parser")                  #captures all information in complete details

        buildName = soup.find(id="p_building_name")["value"]                                    #address details
        plotNo = soup.find(id="p_plot_no")["value"]
        street = soup.find(id="p_street")["value"]
        landmark = soup.find(id="p_landmark")["value"]
        area = soup.find(id="p_area")["value"]
        village = soup.find(id="p_village")["value"]
        pincode  = soup.find(id="p_pin_code")["value"]
        sql.insertAddress(userID,buildName,plotNo,street,landmark,area,village,pincode)
        print("add")

        table = soup.find('tbody')                                                              #sibling details
        row = table.find("tr")
        data = row.find_all("td")
        relation = data[0].get_text(strip=True)
        name = data[1].get_text(strip=True)
        dob = data[2].get_text(strip=True)
        phNo = data[3].get_text(strip=True)
        email = data[4].get_text(strip=True)
        edu = data[5].get_text(strip=True)
        occ = data[6].get_text(strip=True)
        sql.insertSiblings(userID,relation,name,dob,phNo,email,edu,occ)
        print("sib")



        enrollNo = soup.find(id="enroll_no")["value"]                                           #student details
        dob = soup.find(id="dob")["value"]
        aadhar = soup.find(id="aadhar")["value"]
        pan = soup.find(id="StudentDetailsPanCard")["value"]    
        PhNo = soup.find(id="stud_mob")["value"]
        email = soup.find(id="email")["value"]
        sql.insertStudent(userID, enrollNo, dob, aadhar, pan, PhNo, email)

        fatherName = soup.find_all(id="father_name")                                            #father details
        fatherName =f'{fatherName[0]["value"]} {fatherName[1]["value"]} {fatherName[2]["value"]}'
        PhNo = soup.find_all(id="father_alternate_mob")
        alterNo =PhNo[1]["value"]
        PhNo = PhNo[0]["value"]
        dob = soup.find(id="father_dob")["value"]
        occ = soup.find(id="father_occupation")["value"]
        sql.insertFather(userID,fatherName,PhNo,alterNo,dob,occ)

        mother = soup.find_all(id="mother_name")                                                #motherdetails
        mother =f'{mother[0]["value"]} {mother[1]["value"]} {mother[2]["value"]}'
        PhNo = soup.find_all(id="mother_mob")
        alterNo =PhNo[1]["value"]
        PhNo = PhNo[0]["value"]
        dob = soup.find(id="mother_dob")["value"]
        occ = soup.find(id="mother_occupation")["value"]
        sql.insertMother(userID,mother,PhNo,alterNo,dob,occ)


    except Exception as e:
        continue

driver.quit()