from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\chromedriver.exe")
# Maximize window
driver.maximize_window()
driver.minimize_window()
driver.maximize_window()
# open Linkedin login page
driver.get("https://www.linkedin.com/home")
time.sleep(3)
# reading login credentials
f = open("cred.txt", "r")
user = f.readlines()
user = [i.rstrip() for i in user]
Email = user[0]
Password = user[1]
f.close()
# login
driver.find_element(By.XPATH, "//input[@id='session_key']").send_keys(Email)
driver.find_element(By.XPATH, "//input[@id='session_password']").send_keys(Password)
driver.find_element(By.XPATH, "//button[@class='sign-in-form__submit-button']").click()
# navigating to jobs page
jobs = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//a[@class='app-aware-link global-nav__primary-link']")))
jobs[1].click()
time.sleep(2)
# searching in jobs
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3299847161&distance=25&geoId=102713980&keywords=data%20scientist")
div = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, "jobs-search-results-list")))
l1 = []
try:
    for f in range(2, 10):
        time.sleep(5)
        div_in = div.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")
        for j in div_in:
            j.click()
            misc = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='jobs-unified-top-card__content--two-pane']/a[@class='ember-view']")))
            if misc.get_attribute("href") not in l1:
                l1.append(misc.get_attribute("href"))
        driver.find_element(By.XPATH, "//button[@aria-label='Page {}']".format(f)).click()
except:
    pass
# Getting Data from urls
Job_Title = []
Company_Name = []
Company_Location = []
Job_Description = []
Work_Method = []
Post_Date = []
for l in l1:
    try:
        driver.get(l)
        time.sleep(2)
        drive = driver.find_element(By.XPATH, "//div[@class='p5']")
        Job_Title.append(drive.find_element(By.TAG_NAME, "h1").text)
        Company_Name.append(drive.find_element(By.CLASS_NAME, "jobs-unified-top-card__company-name").text)
        Company_Location.append(drive.find_element(By.CLASS_NAME, "jobs-unified-top-card__bullet").text)
        try:
            Work_Method.append(drive.find_element(By.CLASS_NAME, "jobs-unified-top-card__workplace-type").text)
        except:
            Work_Method.append(None)
        try:
            Post_Date.append(drive.find_element(By.CLASS_NAME, "jobs-unified-top-card__posted-date").text)
        except:
            Post_Date.append(None)

        try:
            driver.find_element(By.XPATH, "//footer[@class='artdeco-card__actions']/button[@id='ember35']").click()
            Job_Description.append(driver.find_element(By.XPATH, "//div[@id='job-details']").text)
        except:
            pass
    except:
        pass
# creating DataFrame
df = pd.DataFrame(list(zip(Job_Title, Company_Name, Company_Location, Work_Method, Post_Date)),
                  columns=["Job_Title", "Company_Name", "Company_Location", "Work_Method", "Post_Date"])
df.to_csv("linkedin.csv", index=False)
# creating Job_description file
job_desc = open("Job_desc.txt", "w+")
for data in Job_Description:
    job_desc.writelines(data)
job_desc.close()
#closing driver
driver.close()
