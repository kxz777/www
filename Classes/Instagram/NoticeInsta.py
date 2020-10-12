# encoding: iso-8859-1
import Navigate
import Behaviour

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Notice:
    @staticmethod
    def getNoticeNumber(driver):
        content = driver.page_source
        if "We can save your login info on this browser so you don't need to enter it again" in content:
            notice = 1
        elif "ou curtir e comentar as suas fotos." in content:
            notice = 2
        elif "To secure your account, we'll send you a security code to verify your identity." in content:
            notice = 3
        elif "Esta conta é privada" in content or "This Account is Private" in content:
            notice = 4            
        elif 'aria-label="Following"' in content:
            notice = 5
        else:
            notice = False
        return  notice

    @staticmethod
    def getNoticeValue(noticeNum):
        if noticeNum == 1:
            res = "save login info"
        elif noticeNum == 2:
            res = "activate notification"            
        elif noticeNum == 3:
            res = "token required"        
        elif noticeNum == 4:
            res = "private account"     
        elif noticeNum == 5:
            res = "previous followed"                         
        return res

    @staticmethod
    def getNoticeContent(noticeNum):
        if noticeNum == 1:
            res = "Notice1"
        elif noticeNum == 2:
            res = "Notice2"
        elif noticeNum == 3:
            res = "Notice3"     
        elif noticeNum == 4:
            res = "Notice4"   
        elif noticeNum == 5:
            res = "Notice5"                         
        print ("Insta " + res)                 
        return res

    @staticmethod
    def noticeHandler(driver, noticeNum):
        if noticeNum == 1:
            xpath   = "/html/body/div[1]/section/main/div/div/div/div/button"
            wait    = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            form = Navigate.Form(driver)
            form.clickButton(xpath) #code 400, message Bad HTTP/0.9 request type ('443') #NoneType: None
            Behaviour.Wait.randomWait(3,5)    
        elif noticeNum == 2:
            xpath   = "/html/body/div[4]/div/div/div/div[3]/button[2]"
            wait    = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            form = Navigate.Form(driver)
            form.clickButton(xpath)      
            Behaviour.Wait.randomWait(3,5)     
        elif noticeNum == 3:
            xpath   = "/html/body/div[1]/section/div/div/div[3]/form/span/button"
            wait    = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            form = Navigate.Form(driver)
            form.clickButton(xpath)      
            Behaviour.Wait.randomWait(3,5)                          

            txt     = input("Insert the security code sent to your phone:\n")
            xpath   = "/html/body/div[1]/section/div/div/div[2]/form/div/input"                        
            wait    = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            form    = Navigate.Form(driver)
            form.fillText(txt, xpath)            

            xpath   = "/html/body/div[1]/section/div/div/div[2]/form/span/button"
            wait    = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            form = Navigate.Form(driver)
            form.clickButton(xpath)      
            Behaviour.Wait.randomWait(4,6)  
        elif noticeNum == 4:
            Behaviour.Wait.randomWait(10,10)                                
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])