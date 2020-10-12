import Navigate
import Behaviour
import requests
import re
import json 

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Login(object):
    def __init__(self,driver,xpathUser,xpathPass,xpathLogin,username,password):
        self.driver     = driver
        self.xpathUser  = xpathUser
        self.xpathPass  = xpathPass
        self.xpathLogin = xpathLogin
        self.username   = username
        self.password   = password
        Behaviour.Wait.randomWait(2,3)
             
    def fillUser(self):
        wait    = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.xpathUser)))
        form    = Navigate.Form(self.driver)
        form.fillText(self.username, self.xpathUser)

    def fillPass(self):
        wait    = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.xpathPass)))        
        form = Navigate.Form(self.driver)
        form.fillText(self.password, self.xpathPass)

    def clickLogin(self):
        Behaviour.Wait.randomWait(4,5)
        wait    = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.xpathLogin)))
        form = Navigate.Form(self.driver)
        form.clickButton(self.xpathLogin)      
        Behaviour.Wait.randomWait(4,5)

    #para pular o recaptcha faco o login via post
    #para tanto uso apenas os seguintes cookies:
    #__cfduid e crsftoken
    #__cfduid vem do cookies da requisicao
    #crsftoken vem do texto de resposta da requisicao no campo id
    # def postLogin(self):
    #     url  = 'https://dizu.com.br/painel/login'
    #     body = {'login' : self.username, 'senha': self.password}
    #     x = requests.post(url, data = body)
    #     content = x.text
    #     content = json.loads(content)
    #     cookies = x.cookies
    #     key = cookies.__dict__['_cookies']['.dizu.com.br']['/']['__cfduid'].__dict__['name']
    #     val = cookies.__dict__['_cookies']['.dizu.com.br']['/']['__cfduid'].__dict__['value']
    #     self.driver.get('https://dizu.com.br')        
    #     self.driver.add_cookie({'name' : key, 'value' : val})
    #     self.driver.add_cookie({'name' : 'crsftoken', 'value' : content["id"]})
    #     Behaviour.Wait.randomWait(4,5)