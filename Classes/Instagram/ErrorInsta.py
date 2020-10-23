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
        elif "It looks like you may have shared your username and password with an app offering followers or likes" in content:
            error = 7   
        elif "Please update your password to help us keep your account safe" in content:
            error = 8
        elif "Your Account Was Compromised" in content:
            error = 9            
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
        elif errorNum == 7:
            res = "automation detected1"      
        elif errorNum == 8:
            res = "automation detected2"      
        elif errorNum == 9:
            res = "automation detected3"                              
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
        elif errorNum == 7:
            res = "Error7"      
        elif errorNum == 8:
            res = "Error8"     
        elif errorNum == 9:
            res = "Error9"                                                
        print ("Insta " + res)
        return res    