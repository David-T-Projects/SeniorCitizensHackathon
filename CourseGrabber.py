import requests
from bs4 import BeautifulSoup as bs
from extensions import db
from models.courseListings import CourseListings

def populateDBCall(passed_str, department, id_num):

    assignList = []
    temp = ''
    index = 0
    while index < len(passed_str):
        if passed_str[index] != ' ':
            temp += passed_str[index]
        else:
            # If the next character is also a space, append the temp value to assignList
            # and move index to the next non-whitespace character
            if index + 1 < len(passed_str) and passed_str[index + 1] == ' ':
                assignList.append(temp)
                temp = ''

                while index + 1 < len(passed_str) and passed_str[index + 1] == ' ':
                    index += 1
            # If the next character is not a space, append the temp value to assignList
            # and reset temp for the next word
            elif index + 1 < len(passed_str) and passed_str[index + 1] != ' ':
                assignList.append(temp)
                temp = ''
        index += 1

    sectionType = str(assignList.pop(0))
    CRN = int(assignList.pop(0))
    course = str(assignList.pop(0) + "-" + assignList.pop(0))
    lname = assignList.pop()

    if(lname != "Du"):

        if(lname == "STAFF"):
            instructor = str(lname)
        else:
            instructor = str(assignList.pop() + ' ' + lname)
        room = str(assignList.pop())
        building = str(assignList.pop())

        if(assignList[-1] == "TBA"):
            end = "TBA"
            start = str(assignList.pop())
        else:
            end = str(assignList.pop())
            start = str(assignList.pop())
        days = str(assignList.pop())
        
        try:
            temp = int(assignList.pop())
            wait_list = int(temp)
        
        except:
            instructor+=room
            room = building
            building = end
            end = start
            start = days
            days = temp
            wait_list= int(assignList.pop())

        availability= str(assignList.pop())
        enrollment = int(assignList.pop())
        max_enrollment= int(assignList.pop())
        credit= float(assignList.pop())
    
    else:
        name_three = str(assignList.pop())
        name_two = str(assignList.pop())
        instructor = str(assignList.pop() + name_two +' '+ name_three + ' ' + lname)
        room = str(assignList.pop())
        building = str(assignList.pop())

        if(assignList[-1] == "TBA"):
            end = "TBA"
            start = str(assignList.pop())
        else:
            end = str(assignList.pop())
            start = str(assignList.pop())
        days = str(assignList.pop())
        
        try:
            temp = int(assignList.pop())
            wait_list = int(temp)
        
        except:
            instructor+=room
            room = building
            building = end
            end = start
            start = days
            days = temp

        availability= str(assignList.pop())
        enrollment = int(assignList.pop())
        max_enrollment= int(assignList.pop())
        credit= float(assignList.pop())


    title = ' '.join(assignList)
    title_str = str(title)

    course_entry = CourseListings(id = id_num, sectionType = sectionType, CRN = CRN, department = department, course=course, title=title_str, 
                                  credit=credit, max_enrollment=max_enrollment, enrollment=enrollment, availability=availability, 
                                  wait_list=wait_list, days=days, start=start, end=end, building=building, room=room, instructor=instructor)

    db.session.add(course_entry)
    db.session.commit()




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

def scrape_schedule_information():

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
    k = 0
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
            datacopy = str(courseHtmlSoup)
            repair = "&amp;"
            repaired_data_part = datacopy.replace(repair, "&")
            repaired_data = repaired_data_part.replace(" C", "  C")

            data_arr = repaired_data.split("\n")
            
            department_str = data_arr[6].replace("<h2>", "")
            department = department_str.split("/")
            j = 11

            while(data_arr[j][0] != "<"):
                populateDBCall(data_arr[j], department[0], k)
                j+=1
                k+=1
                
            i += 1



        #Iterate to the next semester page
        i += 1


    #parsedLink1 = web_links[0]



