import Navigate
import Behaviour
import sys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

sys.path.append('/home/centos/www/Classes/Selenium')
import ErrorHandlerSelenium

class Follow(object):
    def __init__(self,browser,log,loginInsta,xpathFollow):
        self.browser     = browser
        self.driver      = browser.webdriver
        self.log         = log
        self.loginInsta  = loginInsta        
        self.xpathFollow = xpathFollow

    def follow(self,url):
        self.browser.getRetries(url, 3, 10) 

        handler      = "Instagram"
        stage        = "InstagramFollow1"  
        errorHandler = ErrorHandlerSelenium.ErrorHandler(self.browser,self.log)
        ok           = errorHandler.handle(handler, self.loginInsta.username, stage)

        #notice 4 conta privada    nao tem botao de follow
        #notice 5 conta ja seguida nao tem botao de follow
        if ok == True and errorHandler.lastNotice != 4 and errorHandler.lastNotice != 5:
            Behaviour.Wait.randomWait(9,10)  
            self.clickFollow()

            handler = "Instagram"
            stage   = "InstagramFollow2"  
            ok      = errorHandler.handle(handler, self.loginInsta.username, stage)

            if ok == True:
                handler = "Instagram"
                stage   = "InstagramFollow3"  
                ok      = errorHandler.handle(handler, self.loginInsta.username, stage)

        return ok

             
    def clickFollow(self):        
        wait    = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.xpathFollow)))
        Navigate.Move.moveToElement(self.driver, self.xpathFollow)
        form = Navigate.Form(self.driver)
        form.clickButton(self.xpathFollow)      
        Behaviour.Wait.randomWait(12,14)