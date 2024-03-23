from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize a WebDriver (make sure you have the appropriate driver installed and in your PATH)
driver = webdriver.Chrome()  # Change this to the appropriate WebDriver for your browser

# Navigate to the URL
url = "https://catalog.uah.edu/#/courses"
driver.get(url)

# Wait for the dynamically generated content to appear (adjust timeout and conditions as needed)
try:
    # Wait for the element with ID "kuali-catalog" to appear
    catalog_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "style__groups___NnCy6"))
    )

    # Find all list elements
    list_elements = driver.find_elements(By.CLASS_NAME, "style__collapsibleBox___15waq")

    div_element = driver.find_element(By.ID, "kuali-catalog")  # Replace "your_div_id" with the actual ID of the div

    # Find all anchor elements within the div
    link_elements = div_element.find_elements(By.TAG_NAME, "a")

    # Extract the href attribute from each link element
    links = [link.get_attribute("href") for link in link_elements]

    # Print the list of links
    print("List of links:")
    for link in links:
        print(link)

    # Iterate through the list elements
    for element in list_elements:
        # Extract information from each list element
        list_content = element.text
        
        # Do something with the extracted information (print it in this example)
        print(list_content)

    

finally:
    # Remember to close the WebDriver when you're done
    driver.quit()