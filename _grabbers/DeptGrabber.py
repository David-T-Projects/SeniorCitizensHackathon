from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from extensions import db
from models.courses import Course
from models.department import Department
from selenium.webdriver.chrome.options import Options

def getCourses():

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # Initialize a WebDriver (make sure you have the appropriate driver installed and in your PATH)
    driver = webdriver.Chrome()  # Change this to the appropriate WebDriver for your browser

    # Navigate to the URL
    url = "https://catalog.uah.edu/#/courses"
    driver.get(url)

    # Wait for the dynamically generated content to appear (adjust timeout and conditions as needed)
    try:
        # Wait for the element with catalog to appear
        catalog_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "style__groups___NnCy6"))
        )
        
        # Get the catalog element
        div_element = driver.find_element(By.CLASS_NAME, "style__groups___NnCy6") 

        # Find all list elements
        list_elements = driver.find_elements(By.CLASS_NAME, "style__collapsibleBox___15waq")

        # Find all anchor elements within the div
        link_elements = div_element.find_elements(By.TAG_NAME, "a")

        # Extract the href attribute from each link element
        links = [link.get_attribute("href") for link in link_elements]

        # Print the list of links
        print("List of links:")
        for link in links:
            print(link)

        list_dept = []

        # Iterate through the list elements
        for element in list_elements:
            # Extract information from each list element
            list_content = element.text

            list_content= list_content.split('\n')[0]
            
            list_dept.append(list_content)
            
            db.session.add(Department(name=list_content))

        print(list_dept)

        i = 0
        for link in links:
            # Get the URL of the link
            url = link

            # Visit the link
            driver.get(url)

            catalog_element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "style__collapsibleBox___15waq"))
            )

            # Get the catalog element
            div_element = driver.find_element(By.CLASS_NAME, "style__collapsibleBox___15waq") 

            # Find all anchor elements within the div
            link_elements = div_element.find_elements(By.TAG_NAME, "a")

            # These are the course links, these links will have course descriptions and credit hours
            dept_links = [link.get_attribute("href") for link in link_elements]
            
            for link in link_elements:
                course_name = link.text
                parts = course_name.split("-")
                courseID = parts[0].strip(' ')
                name = parts[1].strip(' ')
                department = list_dept[i]
                course_entry = Course(courseID = courseID, name = name, department_name = department, description = None, credits = None)
                db.session.add(course_entry)
                db.session.commit()
            i+=1

    finally:
        # Remember to close the WebDriver when you're done
        driver.quit()

