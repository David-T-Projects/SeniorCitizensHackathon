from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize a WebDriver (make sure you have the appropriate driver installed and in your PATH)
driver = webdriver.Chrome()  # Change this to the appropriate WebDriver for your browser

# Navigate to the URL
url = "https://catalog.uah.edu/#/courses?isPrint=true"
driver.get(url)

# Wait for the dynamically generated content to appear (adjust timeout and conditions as needed)
try:
    # Wait for the element with ID "kuali-catalog" to appear
    catalog_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "kuali-catalog"))
    )
    
    # Once the element is found, you can extract its content
    catalog_content = catalog_element.text
    print("Catalog content:")
    print(catalog_content)

finally:
    # Remember to close the WebDriver when you're done
    driver.quit()