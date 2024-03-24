from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from extensions import db
from models.Colleges import Colleges

def getPrograms():
    # Initialize a WebDriver (make sure you have the appropriate driver installed and in your PATH)
    driver = webdriver.Chrome()  # Change this to the appropriate WebDriver for your browser

    # Navigate to the URL
    url = "https://catalog.uah.edu/index.php#/programs"
    driver.get(url)


    # Wait for the dynamically generated content to appear (adjust timeout and conditions as needed)
    try:
        # Wait for the element with catalog to appear
        catalog_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "style__collapsibleBox___15waq"))
        )
        catalog_div = driver.find_element(By.CLASS_NAME, "style__topLevelPanelWrapper___1adT-")

        div_elements = driver.find_elements(By.CLASS_NAME, "style__collapsibleBox___15waq")

        # Find all anchor elements within the div
        link_elements = catalog_div.find_elements(By.TAG_NAME, "a")

        # Extract the href attribute from each link element
        links = [link.get_attribute("href") for link in link_elements]

        # Print the list of links
        print("List of links:")
        for link in links:
            print(link)

        list_colleges = []
        college_count = 0
        
        # Iterate through the list elements
        for div in div_elements:
            # Extract information from each list element
            list_content = div.text

            list_content= list_content.split('\n')[0]
            
            list_colleges.append(list_content)

            db.session.add(Colleges(name=list_content))
            db.session.commit()

        print(list_colleges)
        print()

        i = 0
        for link in links:
            # Get the URL of the link
            url = link

            # Visit the link
            driver.get(url)

            catalog_element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "style__topLevelPanel___3yI6z"))
            )

            catalog_div = driver.find_element(By.CLASS_NAME, "style__topLevelPanel___3yI6z")

            # Find all anchor elements within the div
            link_elements = catalog_div.find_elements(By.TAG_NAME, "a")

            # Extract the href attribute from each link element
            links = [link.get_attribute("href") for link in link_elements]
            
            programs_list = []

            for element in link_elements:
                # Extract information from each list element
                content = element.text
                
                programs_list.append(content)
                
            print(programs_list)  
            print()  
                

    finally:
        # Remember to close the WebDriver when you're done
        driver.quit()
