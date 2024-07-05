from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException, TimeoutException

def setup_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Optional: Run in headless mode
    service = Service('/home/user/Downloads/chromedriver')  # Update this path
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def test_payloads(url, file_path):
    driver = setup_browser()
    try:
        with open(file_path, 'r') as file:
            payloads = file.readlines()

        for payload in payloads:
            payload = payload.strip()
            test_url = url.replace("PAYLOAD", payload)
            print(f"Testing URL: {test_url}")
            driver.get(test_url)

            try:
                # Wait for up to 10 seconds for the alert to be present
                WebDriverWait(driver, 10).until(EC.alert_is_present())
                alert = driver.switch_to.alert
                alert_text = alert.text
                print(f"Alert found with text: '{alert_text}'")
                alert.accept()  # Close the alert
                print(f"Payload executed: {payload}")
            except TimeoutException:
                print(f"Timeout while waiting for alert with payload: {payload}")
            except NoAlertPresentException:
                print(f"No alert present with payload: {payload}")
            except UnexpectedAlertPresentException:
                print("Unexpected alert encountered during execution.")

    finally:
        driver.quit()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Test XSS payloads.')
    parser.add_argument('--url', required=True, help='URL to test with PAYLOAD placeholder')
    parser.add_argument('--file', required=True, help='Path to the payload file')
    args = parser.parse_args()
    test_payloads(args.url, args.file)

