import Navigate
import Behaviour

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Login(object):
    def __init__(self,driver,xpathUser,xpathPass,xpathLogin,username):
        self.driver     = driver
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
        Behaviour.Wait.randomWait(3,5)