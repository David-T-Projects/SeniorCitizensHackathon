from bs4 import BeautifulSoup
import requests

# URL of the website you want to fetch HTML from
url = "https://catalog.uah.edu/#/courses?isPrint=true"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the HTML content from the response
    html_content = response.text
    #print(html_content)
    
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all <div> tags with a specific class
    divs_with_class = soup.find_all('div', _id='UAH-kuali-section')
    
    # Check if any <div> tags with the specified class were found
    if divs_with_class:
        # Extract data or perform operations on the found <div> tags
        for div in divs_with_class:
            # Example: Print the text content of each <div> tag
            print(div.text)
    else:
        print("No <div> tags with the specified class were found.")
else:
    print("Failed to fetch HTML. Status code:", response.status_code)



