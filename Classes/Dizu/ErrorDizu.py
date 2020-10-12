class Error:
    @staticmethod
    def getErrorNumber(driver):
        content = driver.page_source
        if 'lido","param":"recaptcha_token' in content:
            error = 1
        elif 'veis no momento. Tente com outro perfil, ou volte mais tarde. Dica: Vo' in content:
            error = 2   
        elif 'Um ou mais erros ocorrem. Verifique os dados informados' in content:
            error = 3
        elif 'The web server reported a bad gateway error.' in content:
            error = 4           
        elif "has banned your access based on your browser's signature" in content:
            error = 5       
        elif "Invalid domain for site key" in content:                        
            error = 6
        else:
            error = False
        return  error

    @staticmethod
    def getErrorValue(errorNum):
        if errorNum == 1:
            res = "blocked by recaptcha"
        elif errorNum == 2:
            res = "no tasks available now"
        elif errorNum == 3:
            res = "login error"
        elif errorNum == 4:
            res = "server is down"    
        elif errorNum == 5:
            res = "banned by signature browser"        
        elif errorNum == 6:
            res = "failed on recaptcha score"                          
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
        print ("Dizu " + res)
        return res    