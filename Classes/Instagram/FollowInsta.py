import Navigate
import Behaviour

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Follow(object):
    def __init__(self,driver,xpathFollow):
        self.driver      = driver
        self.xpathFollow = xpathFollow
             
    def clickFollow(self):        
        wait    = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.xpathFollow)))
        Navigate.Move.moveToElement(self.driver, self.xpathFollow)
        form = Navigate.Form(self.driver)
        form.clickButton(self.xpathFollow)      
        Behaviour.Wait.randomWait(12,14)        
