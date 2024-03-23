from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def getFaculty(url):
    driver.get(url)

    # Find the div element
    div_elements = driver.find_elements(By.CLASS_NAME, "col-sm-4.card")  # Adjust the class name as needed

    # Iterate over each div element
    for div_element in div_elements:
        # Get the text from the div element
        div_text = div_element.text
        
        # Print the text
        print("Text inside the div:")
        print(div_text)
        print()  # Print an empty line for clarity


chrome_options = Options()
chrome_options.add_argument('--headless')

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

with open('faculty_links.txt', 'r') as file:
    links = file.readlines()

for link in links:
    getFaculty(link)

# Close the WebDriver
driver.quit()



