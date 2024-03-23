import requests

# The URL of the website containing the XML
url = "https://uah.campuslabs.com/engage/events.rss"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the text content of the response (which is the XML in this case)
    xml_text = response.text
    print(xml_text)
else:
    print("Failed to retrieve the XML. Status code:", response.status_code)

