import Behaviour
from selenium.webdriver.common.action_chains import ActionChains

class Form(object):

    def __init__(self, driver):
        self.driver = driver

    def fillText(self,string, xpath):
        for char in string:
            element = self.driver.find_element_by_xpath(xpath)
            element.send_keys(char)
            Behaviour.Wait.randomWait(0.1,0.3) #type timing of a person
        Behaviour.Wait.randomWait(0.3,0.5)     #validation timing of typed chars

    def clickButton(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        element.click()          

    def selectOption(self, xpathSelect, value):
        element = self.driver.find_element_by_xpath(xpathSelect)
        for option in element.find_elements_by_tag_name('option'):
            Behaviour.Wait.randomWait(0.1,0.1)
            if option.text == value: #lookup value                
                option.click() 
                break
        Behaviour.Wait.randomWait(0.2,0.3)

class Move:
    @staticmethod
    def moveToElement(driver, xpath):
        element = driver.find_element_by_xpath(xpath)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        Behaviour.Wait.randomWait(0.2,0.3)