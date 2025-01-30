import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getMetroData(mfrom="PCMC", mto='Bopadi'):
    # Configure Chrome options for headless mode
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")  
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage")  

    # Set up the WebDriver with ChromeDriverManager
    driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

    try:
        # Open the website
        driver.get(f'https://www.nearbymetro.com/metro/14/farecalculation/From-{mfrom}/To-{mto}')

        # Wait for page to load completely
        time.sleep(3)  # Small delay to allow full data loading

        # Wait for the element to be visible (not just present)
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div[3]/div[1]/div'))
        )

        # Extract and process the text
        data = element.text.split('\n')
        dic = {}

        for i in range(0, len(data), 2):
            t = '_'.join(data[i].split(' '))
            dic[t] = data[i + 1]

    except Exception as e:
        print("Error occurred:", e)
        print("Page Source for Debugging:\n", driver.page_source)

    finally:
        driver.quit()

    return dic