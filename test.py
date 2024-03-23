
from bs4 import BeautifulSoup
import requests


# URL of the website you want to fetch HTML from
url = "https://uah.campuslabs.com/engage/events.rss"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the HTML content from the response
    rss_content = response.text
    print(rss_content)
    
    # Parse the RSS feed content with BeautifulSoup
    soup = BeautifulSoup(rss_content, 'xml')

    # Find the description element
    description = soup.find('description')

    # Extract the CDATA content from the description element
    cdata_content = description.string.strip()

    # Parse the CDATA content as XML
    item_soup = BeautifulSoup(cdata_content, 'xml')

    # Find the div with class "p-name summary"
    div_with_class = item_soup.find('div', class_='p-name summary')

    # Check if the div with class is found
    if div_with_class:
        print("Found the div with class 'p-name summary':")
        print(div_with_class.text)
    else:
        print("No div with class 'p-name summary' was found.")





