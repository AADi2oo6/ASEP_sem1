from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getMetroData(mfrom="PCMC",mto='Bopadi'):
# Configure Chrome options for headless mode
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    chrome_options.add_argument("--no-sandbox")  # For running in environments like Docker
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues

    # Set up the WebDriver with ChromeDriverManager
    driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

    # Open the website in headless mode
    driver.get(f'https://www.nearbymetro.com/metro/14/farecalculation/From-{mfrom}/To-{mto}')

    # Add an explicit wait
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div[3]/div[1]/div'))
    )

    # Print the extracted text
    data = element.text.split('\n')
    dic = {}
    try :

        for i in range(0,len(data),2):
        
            t = data[i].split(' ')
            t = '_'.join(t)
            dic[t]=data[i+1]
    except:
        pass
        # print(f"{}: {}")

    # Close the driver
    driver.quit()
    return dic
