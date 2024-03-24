from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#Added DB Support - Caleb
from extensions import db
from models import courses


def getFaculty(url):
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

        #If there's a . that means there is a Mr. Ms. or P.H.D. that we need to get rid of
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
                        print("User has no parts[3]")
                

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

            #The second element doesn't have numbers, but it could be an email, check it's case
            elif parts[2].isupper()==False: 
                #It it isn't all upper, it's an email, go ahead and assign it
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

                try:
                    #We realized it was a double position, now we have to handle the remaining possibilities
                    if parts[3].isupper()==True:
                        #It is all upper, it must be the room number
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
                                    #user has no email
                        except:
                            print("User has no phone number or email")
                    
                    elif ("@" in parts[3]):
                        #It must be the email
                        email = parts[3]

                    else:
                        #Only option left is the phone number, which means email is the last part
                        phoneNumber = parts[3]
                        try:
                            email = parts[4]
                        except:
                            print("User has no email")
                            #user has no email
                
                #The user had a two line position but not further info
                except:
                    print("The user does not have an office, phone #, or email")
                
        except:
            parts.pop(0)
            position = ''.join(parts)
            

        
        print("fullName: ", fullName)
        print("Position: ", position)
        print("officeLocation: ", officeLocation)
        print("phoneNumber:", phoneNumber)
        print("Email:", email)
        print("\n")

        

        


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



