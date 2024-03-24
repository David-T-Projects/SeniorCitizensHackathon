from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

#Added DB Support - Caleb
from extensions import db
from models import faculty


def getFaculty(url, driver):
    driver.get(url)

    # Find the div element
    div_elements = driver.find_elements(By.CLASS_NAME, "col-sm-4.card")  # Adjust the class name as needed

    # Iterate over each div element
    for div_element in div_elements:
        # Get the text from the div element
        div_text = div_element.text
        
        # Print the text
        # print("Text inside the div:")
        print(div_text)
        print()  # Print an empty line for clarity

        #Added DB support below - Caleb
        parts = div_text.split("\n")

        potentialName = parts[0]
        position = parts[1]
        email = ""
        phoneNumber = ""
        officeLocation = ""

        #If there's a . that means there is a Mr. Ms. or Ph.D. that we need to get rid of
        if "." in potentialName:
            nameArray = potentialName.split(" ")

            #Add corrected elements to a name list
            cleanedNameArray = []
            for name in nameArray:
                if "." in name:  # Add names without periods
                    continue
                if "," in name:
                    name = name.split(",")[0]  # Remove trailing commas
                cleanedNameArray.append(name)

            fullName = ' '.join(cleanedNameArray).strip()
      
        else:
            fullName = parts[0]  

        def has_numbers(inputString):
            return any(char.isdigit() for char in inputString)
        

        #-------- End of name stuff -------

        #We have to put the rest of the conditional logic inside a try
        try:
            #If it has numbers then you are good to take the first element bc it isn't 2 lines
            if has_numbers(parts[2])==True: 

                if parts[2].isupper()==True:
                    #It is all upper, it must be the room number
                    officeLocation=parts[2]

                    #Moving on to parts[3] & [4]
                    try:
                        if ("@" in parts[3]):
                            #It must be the email, and only the email
                            email = parts[3]
                        else:
                            phoneNumber = parts[3]

                            try:
                                email = parts[4]
                            except:
                                print("User has no email")
                                #user has no email
                    except:
                        print("User has no email")
                

                elif ("@" in parts[2]):
                    #It must be the email
                    email = parts[2]    

                else:
                    #Only option left is the phone number, which means email is the last part
                    phoneNumber = parts[2]
                    try:
                        email = parts[3]
                    except:
                        print("User has no email")
                        #user has no email

            #The third element doesn't have numbers, but it could be an email, check it's case
            elif "@" in parts[2]: 
                #It has an @, it's an email, go ahead and assign it
                email = parts[2]
            
            elif len(parts[2])==3:
                #It must be a building code without a number
                officeLocation = parts[2]

                #Moving on to parts[3] & [4]
                try:
                    if ("@" in parts[3]):
                        #It must be the email, and only the email
                        email = parts[3]
                    else:
                        phoneNumber = parts[3]

                        try:
                            email = parts[4]
                        except:
                            print("User has no email")
                            #user has no email
                except:
                    print("User has no phone number or email")

                

            #It didn't have number and it was all uppercase, it's part of the position
            else:
                position = position + parts[2]
                
                #It was a double position, let's carry on
                try:
                    
                    #It must be the room number if this is true
                    if parts[3].isupper()==True and (has_numbers(parts[3]) or len(parts[3])==3):              
                        officeLocation=parts[3]

                        #Moving on to parts[4] & [5]
                        try:
                            if ("@" in parts[4]):
                                #It must be the email, and only the email
                                email = parts[4]

                            else:

                                phoneNumber = parts[4]
                                try:
                                    email = parts[5]
                                except:
                                    print("User has no email")
        
                        except:
                            print("User has no phone number or email")
                    
                    elif ("@" in parts[3]):
                        #It must be the email
                        email = parts[3]

                    elif has_numbers(parts[3]):
                        #Must be the phone number, which means email is the last part
                        phoneNumber = parts[3]
                        try:
                            email = parts[4]
                        except:
                            print("User has no email")
                            #user has no email
                    
                    else:
                        #We have discovered the fated TRIPLE POSITION
                        position = position + parts[3]
                        try:
                                #We realized it was a triple position, now we have to handle the remaining possibilities
                            
                            if parts[4].isupper()==True and (has_numbers(parts[4]) or len(parts[4])==3):
                                #It must be the room number
                                officeLocation=parts[4]

                                #Moving on to parts[5] & [6]
                                try:
                                    if ("@" in parts[5]):
                                        #It must be the email, and only the email
                                        email = parts[5]

                                    elif has_numbers(parts[5]):
                                        #It's gotta be a phone number
                                        phoneNumber = parts[5]
                                        try:
                                            email = parts[6]
                                        except:
                                            print("User has no email")
                                            #user has no email

                                    else:
                                        #WE HAVE DISCOVERED A QUAD POSITION
                                        position = position + parts[4]

                                except:
                                    print("User has no phone number or email")
                            

                            elif ("@" in parts[4]):
                                #It must be the email
                                email = parts[4]

                            elif has_numbers(parts[4]):
                                #Must be the phone number, which means email is the last part
                                phoneNumber = parts[4]
                                try:
                                    email = parts[4]
                                except:
                                    print("User has no email")
                                    #user has no email

                            else:
                                #WE HAVE DISCOVERED A QUAD POSITION
                                position = position + parts[4]

                                try:

                                    if parts[5].isupper()==True and (has_numbers(parts[5]) or len(parts[5])==3):
                                        #It must be the room number
                                        officeLocation=parts[5]

                                        #Moving on to parts[5] & [6]
                                        try:
                                            if ("@" in parts[6]):
                                                #It must be the email, and only the email
                                                email = parts[6]

                                            elif has_numbers(parts[6]):
                                                #It's gotta be a phone number
                                                phoneNumber = parts[6]
                                                try:
                                                    email = parts[7]
                                                except:
                                                    print("User has no email")
                                                    #user has no email

                                            else:
                                                #WE HAVE DISCOVERED A QUINTUPLE POSITION
                                                position = position + parts[5]

                                        except:
                                            print("User has no phone number or email")
                                

                                    elif ("@" in parts[5]):
                                        #It must be the email
                                        email = parts[5]

                                    elif has_numbers(parts[5]):
                                        #Must be the phone number, which means email is the last part
                                        phoneNumber = parts[5]
                                        try:
                                            email = parts[6]
                                        except:
                                            print("User has no email")
                                            #user has no email
                        
                                    else:
                                        #WE HAVE DISCOVERED A QUINTUPLE POSITION
                                        position = position + parts[5]

                                except:
                                    print("The user has no phone number, office, or email")
                        except:
                            print("The user has no office, phone number, or email")
                    
                    #end of an else for the double position
                            
                #The user had a two line position but not further info
                except:
                    print("The user does not have an office, phone #, or email")
                
        #No third element in the array, the rest is just the position        
        except:
            parts.pop(0)
            position = ''.join(parts)

        #Error checking print statements
        # print("fullName: ", fullName)
        # print("Position: ", position)
        # print("officeLocation: ", officeLocation)
        # print("phoneNumber:", phoneNumber)
        # print("Email:", email)
        # print("\n")

        #missing department = department
        facultyEntry = faculty.Faculty(name = fullName, positions = position, 
                                       officeLocation = officeLocation, phoneNumber = phoneNumber,
                                       emailAddress = email)
        db.session.add(facultyEntry)
        db.session.commit()

def populateFaculty():

    chrome_options = Options()
    chrome_options.add_argument('--headless')

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    with open('_grabbers/faculty_links.txt', 'r') as file:
        links = file.readlines()

    for link in links:
        getFaculty(link, driver)

    # Close the WebDriver
    driver.quit()



