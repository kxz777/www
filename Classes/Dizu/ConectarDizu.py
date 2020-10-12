import Navigate
import Behaviour

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Conectar(object):
    def __init__(self,driver,xpathInstaAcc,xpathIniciar,xpathVerLink,xpathConfirmar,xpathPularTarefa):
        self.driver          = driver
        self.xpathInstaAcc   = xpathInstaAcc
        self.xpathIniciar    = xpathIniciar
        self.xpathVerLink    = xpathVerLink
        self.xpathConfirmar  = xpathConfirmar
        self.xpathPularTarefa= xpathPularTarefa        
        Behaviour.Wait.randomWait(1,3)
             
    def fillinstaAcc(self, instaAcc):        
        wait    = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.xpathInstaAcc)))
        Navigate.Move.moveToElement(self.driver, self.xpathInstaAcc)
        form    = Navigate.Form(self.driver)
        form.selectOption(self.xpathInstaAcc, instaAcc)

    def clickIniciar(self):
        Navigate.Move.moveToElement(self.driver, self.xpathIniciar)
        wait    = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.xpathIniciar)))
        form = Navigate.Form(self.driver)
        form.clickButton(self.xpathIniciar)      
        Behaviour.Wait.randomWait(6,8)        

    def clickVerLink(self):
        wait    = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.xpathVerLink)))
        Navigate.Move.moveToElement(self.driver, self.xpathVerLink)
        form = Navigate.Form(self.driver)
        form.clickButton(self.xpathVerLink)
        Behaviour.Wait.randomWait(7,9)

    def clickConfirmar(self):
        wait    = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.xpathConfirmar)))
        Navigate.Move.moveToElement(self.driver, self.xpathConfirmar)
        form = Navigate.Form(self.driver)
        form.clickButton(self.xpathConfirmar)
        Behaviour.Wait.randomWait(4,8)       

    def clickPularTarefa(self):
        wait    = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.xpathPularTarefa)))
        Navigate.Move.moveToElement(self.driver, self.xpathPularTarefa)
        form = Navigate.Form(self.driver)
        form.clickButton(self.xpathPularTarefa)
        Behaviour.Wait.randomWait(2,4)

    def verificarDisponibilidadeTarefas(self,log,tempPath,processId,username,viewport,userAgent):
        content = self.driver.page_source
        while "1. Acesse o link com o perfil selecionado acima" not in content:
            stage   = "DizuWaitingTaks"
            event   = "notice"                        
            value   = "wating"
            content = ""
            log.generateLogData(self.driver, tempPath, processId, username, stage, event, value, content, viewport, userAgent)
            Behaviour.Wait.randomWait(30,30)
            self.clickIniciar()
            Behaviour.Wait.randomWait(2,3)
            content = self.driver.page_source