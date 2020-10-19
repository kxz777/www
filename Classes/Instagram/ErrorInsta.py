class Error:
    @staticmethod
    def getErrorNumber(driver):
        content = driver.page_source
        if "We restrict certain activity to protect our community. Tell us if you think we made a mistake." in content:
            error = 1
        elif "Sorry, your password was incorrect. Please double-check your password." in content:
            error = 2
        elif "Sorry, there was a problem. Please try again." in content \
        and "Enter Your Security Code" in content:
            error = 3
        elif "We couldn't connect to Instagram. Make sure you're connected to the internet and try again." in content:
            error = 4
        elif "Please wait a few minutes before you try again." in content:
            error = 5
        elif "The username you entered doesn't belong to an account. Please check your username and try again." in content:
            error = 6
        else:
            error = False
        return  error

    @staticmethod
    def getErrorValue(errorNum):
        if errorNum == 1:
            res = "restricted activity"
        elif errorNum == 2:
            res = "incorrect password"
        elif errorNum == 3:
            res = "code validation invalid"
        elif errorNum == 4:
            res = "could not connect to instagram"
        elif errorNum == 5:
            res = "wait few minutes" 
        elif errorNum == 6:
            res = "account name probably does not exist"                        
        return res

    @staticmethod
    def getErrorContent(errorNum):
        if errorNum == 1:
            res = "Error1"
        elif errorNum == 2:
            res = "Error2"
        elif errorNum == 3:
            res = "Error3"
        elif errorNum == 4:
            res = "Error4"
        elif errorNum == 5:
            res = "Error5"   
        elif errorNum == 6:
            res = "Error6"                    
        print ("Insta " + res)
        return res    