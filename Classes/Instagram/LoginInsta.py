import Navigate
import Behaviour
import sys

sys.path.append('/home/centos/www/Classes/Selenium')
import ErrorHandlerSelenium

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Login(object):
    def __init__(self,browser,log,xpathUser,xpathPass,xpathLogin,username):
        self.browser    = browser
        self.driver     = browser.webdriver
        self.log        = log        
        self.xpathUser  = xpathUser
        self.xpathPass  = xpathPass
        self.xpathLogin = xpathLogin
        self.username   = username
        Behaviour.Wait.randomWait(1,3)
             
    def fillUser(self, username):
        wait    = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.xpathUser)))
        form    = Navigate.Form(self.driver)
        form.fillText(username, self.xpathUser)

    def fillPass(self, password):
        wait    = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.xpathPass)))        
        form = Navigate.Form(self.driver)
        form.fillText(password, self.xpathPass)

    def clickLogin(self):
        wait    = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.xpathLogin)))
        form = Navigate.Form(self.driver)
        form.clickButton(self.xpathLogin)
        self.browser.hasInjectedJS = False
        Behaviour.Wait.randomWait(3,5)

        handler      = "Instagram"
        stage        = "InstagramLogin"  
        errorHandler = ErrorHandlerSelenium.ErrorHandler(self.browser,self.log)
        ok           = errorHandler.handle(handler, self.username, stage)
        return ok