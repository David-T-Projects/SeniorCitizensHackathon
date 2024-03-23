

# URL of the website you want to fetch HTML from
url = "https://www.uah.edu/cgi-bin/schedule.pl"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the HTML content from the response
    rss_content = response.text
    print(rss_content)
    
    # Parse the RSS feed content with BeautifulSoup
    soup = BeautifulSoup(rss_content, 'xml')


    # Extract the href attribute from each link element
    web_links = soup.select('a') 

    actual_web_links = [link['href'] for link in web_links] 

    # Print the list of links
    print("List of links:")
    for link in web_links:
        print(link)


