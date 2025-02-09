from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the main survey page
base_url = "https://surveymyopinion.researchnow.com/screening"
driver.get(base_url)

# Wait for page to load
wait = WebDriverWait(driver, 10)

try:
    # Find survey links dynamically
    survey_links = driver.find_elements(By.TAG_NAME, "a")
    for link in survey_links:
        href = link.get_attribute("href")
        if href and "screening?id=" in href:  # Detect dynamic survey links
            print("Navigating to:", href)
            driver.get(href)
            break  # Stop after finding the first survey link

    # Wait for survey questions to load
    time.sleep(5)

    # Sample: Select a radio button (Modify based on actual survey questions)
    radio_buttons = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
    if radio_buttons:
        radio_buttons[0].click()  # Selects the first radio button
        print("Selected a radio button")

    # Sample: Check a checkbox (Modify based on actual survey questions)
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    if checkboxes:
        checkboxes[0].click()  # Selects the first checkbox
        print("Checked a checkbox")

    # Sample: Fill out a text input (Modify based on actual survey questions)
    text_inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    if text_inputs:
        text_inputs[0].send_keys("Sample Answer")  # Enters text
        print("Entered text input")

    # Submit form if there's a submit button
    submit_buttons = driver.find_elements(By.CSS_SELECTOR, "input[type='submit'], button[type='submit']")
    if submit_buttons:
        submit_buttons[0].click()
        print("Submitted the survey")

    # Wait for a few seconds before closing
    time.sleep(5)

except Exception as e:
    print("Error:", e)

# Close browser
driver.quit()