from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_ID=os.environ["EMAIL_ID"]
PASSWORD=os.environ["PASSWORD"]

def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4006200033&f_AL=true&keywords=Python%20Developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")


time.sleep(2)
sign_in_button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
sign_in_button.click()

time.sleep(2)
email_input=driver.find_element(By.XPATH,value='//*[@id="username"]')
email_input.send_keys(EMAIL_ID)

time.sleep(2)
password_input=driver.find_element(By.XPATH,value='//*[@id="password"]')
password_input.send_keys(PASSWORD)

time.sleep(2)
signin=driver.find_element(By.XPATH,value='//*[@id="organic-div"]/form/div[3]/button')
signin.click()

time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys("1234567891")

        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
