import requests
from bs4 import BeautifulSoup as bs


#Pass it a url, the function will go into that page, then transform that page into parseable html soup 
def goDeeper(pureUrl):
    response = requests.get(pureUrl)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the HTML content from the response
        rss_content = response.text
        # print(rss_content)
        
        # Parse the RSS feed content with BeautifulSoup
        htmlSoup = bs(rss_content, 'html.parser')
        return htmlSoup

    else:
        linkError = "Link " + pureUrl + " was unresponsive"
        return linkError
    exit
#//end goDeeper()



# URL of the website you want to fetch HTML from
baseUrl = "https://www.uah.edu"
url = "https://www.uah.edu/cgi-bin/schedule.pl"

#Open up the first url
semHtmlSoup = goDeeper(url)

# Extract the href attribute from each link element
semHrefAtts = semHtmlSoup.select('a') 

# Ensure 'href' attribute exists before accessing
semesterLinks = [link.get('href') for link in semHrefAtts if link.get('href')]  


#Go through the first three links and pursue them until we get their all their data
# for i in range(min(3, len(semesterLinks))):
i = 0
while i < 1:
    
    #Fetch the list of all the departments and their links
    dptHtmlSoup = goDeeper(semesterLinks[i])

    #print(dptHtmlSoup)

    # Extract the href attribute from each link element
    dptHrefAtts = dptHtmlSoup.select('a') 

    # Ensure 'href' attribute exists before accessing
    dptLinks = [dptLink.get('href') for dptLink in dptHrefAtts if dptLink.get('href')]  

    dptLinks.pop()

    #For each departments linked page within this semester (iteration of the while loop)
    for dptLink in dptLinks:
    
        #The actual html of the course page
        courseHtmlSoup = goDeeper(baseUrl+dptLink)

        #Print the text on this page
        print(courseHtmlSoup,"\n\n\n")

        #-----------------------
        #PARSER TO THE DB GOES HERE
        #-----------------------

        #Iterate to the next dpt page
        i += 1



    #Iterate to the next semester page
    i += 1


#parsedLink1 = web_links[0]



