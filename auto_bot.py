from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

'''
------------------------------------------------------------------------------
Before staring the program, create .env file contaning the following variables
-------------------------------------------------------------------------------
UNAME = "username"
PWD = "password"
USR_DATA_DIR = "C:/Users/john/AppData/Local/Google/Chrome/User Data"
PROFILE= "Profile 1"
DRIVER_PATH = "chromedriver.exe is chromedriver path"
'''
load_dotenv()  # This line brings all environment variables from .env into os.environ

#create chromeoptions instance
options = webdriver.ChromeOptions()

# options.add_argument("--headless")
# options.add_argument("--no-sandbox")

#provide location where chrome stores profiles
options.add_argument(r"--user-data-dir="+os.environ['USR_DATA_DIR'])

#provide the profile name with which we want to open browser
options.add_argument(r'--profile-directory='+os.environ["PROFILE"])
driver_service = Service(executable_path=os.environ["DRIVER_PATH"])
#specify where your chrome driver present in your pc
driver = webdriver.Chrome(service=driver_service, options=options)
driver.maximize_window()


# CHROME DRIVER:
#chrome_driver_path = "/Users/puneet/Downloads/chromedriver-mac-arm64/chromedriver"

#chrome_service = Service(chrome_driver_path)
#driver = webdriver.Chrome(service=chrome_service)

# SAFARI DRIVER:
# driver = webdriver.Safari()

driver.get("https://northeastern-csm.symplicity.com/students/?")

#code

sign_in_button = driver.find_element("css selector", 'input[value="Current Students and Alumni"]')
sign_in_button.click()

time.sleep(1)

username_field = driver.find_element("id", "username")
username_field.send_keys(os.environ['UNAME'])

time.sleep(1)

password_field = driver.find_element("id", "password")
password_field.send_keys(os.environ['PWD'])
time.sleep(1)
password_field.send_keys(Keys.RETURN)

time.sleep(15)

#send_push_button = driver.find_element("link text", "Send Me a Push ")
#send_push_button.click()

#time.sleep(4)

job_search_button = driver.find_element("css selector",  "a.tile-layout.ng-star-inserted[href='/students/app/jobs/search'] h2.tile-title")
job_search_button.click()

time.sleep(2)

dropdown = Select(driver.find_element(By.ID, "single-select-filter-ocr"))
dropdown.select_by_value("7: f")

time.sleep(7)

# Find the "Apply" button using its class name
apply_button = driver.find_element_by_class_name("btn_primary")

# Click on the "Apply" button
apply_button.click()

time.sleep(5)  # Adjust sleep duration as needed
    # Click on the element
button.click()
time.sleep(2)  # Adjust sleep duration as needed


#driver.close()
