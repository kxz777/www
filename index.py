import os
import glob
import json
import sys
import time
import datetime as DT

sys.path.append('/home/centos/www/Classes/Selenium')
import Debug
import Devices
import Driver
import Log

sys.path.append('/home/centos/www/Classes/Instagram')
import LoginInsta
import FollowInsta
import ErrorInsta
import NoticeInsta

sys.path.append('/home/centos/www/Classes/Dizu')
import LoginDizu
import ConectarDizu
import ErrorDizu
import NoticeDizu

processId = os.getpid()

#Generate random device
random = True
device = Devices.Device('', random)

#Chnage viewport to bypass recaptcha
chrome = Driver.Chrome()
chrome.set_viewport_size(device.width,device.height)
driver = chrome.webdriver

tempPath = "/home/centos/www/temp"
fileName = "log"
fields   = ["ID","Account","Date","Time","Event","Stage","Value","Content","png","html","js","ViewPort","User-Agent"]
log      = Log.LogCSV(tempPath, fileName, fields)

try:
    chrome.getRestries('https://www.instagram.com', 3, 10)
    xpathUser  = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input'
    xpathPass  = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input'
    xpathLogin = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button'
    username   = "spontaneousdrawing4fun"
    password   = "WF4vYL5aMYDu5uy"
    # username   = "ery_1aa"
    # password   = "tuna12"

    loginInsta = LoginInsta.Login(driver,xpathUser,xpathPass,xpathLogin,username)        
    loginInsta.fillUser(username)
    loginInsta.fillPass(password)
    loginInsta.clickLogin()
    chrome.hasInjectedJS = False

    stage      = "InstagramLogin"
    viewport   = device.name
    userAgent  = chrome.userAgent    
    errorNum   = ErrorInsta.Error.getErrorNumber(driver)
    noticeNum  = NoticeInsta.Notice.getNoticeNumber(driver)
    if(errorNum!=False):        
        event   = "error"            
        value   = ErrorInsta.Error.getErrorValue(errorNum)
        content = ErrorInsta.Error.getErrorContent(errorNum)
        log.generateLogData(driver, tempPath, processId, username, stage, event, value, content, viewport, userAgent)
    else:
        while(noticeNum!=False):
            event   = "notice"                        
            value   = NoticeInsta.Notice.getNoticeValue(noticeNum)
            content = NoticeInsta.Notice.getNoticeContent(noticeNum)
            log.generateLogData(driver, tempPath, processId, username, stage, event, value, content, viewport, userAgent)
            NoticeInsta.Notice.noticeHandler(driver, noticeNum)
            chrome.hasInjectedJS = False
            noticeNum  = NoticeInsta.Notice.getNoticeNumber(driver)

        event   = "ok"                        
        value   = "login success"
        content = ""
        log.generateLogData(driver, tempPath, processId, username, stage, event, value, content, viewport, userAgent)
        chrome.getRestries('https://dizu.com.br/login?error=session_expired', 3, 10)

        xpathUser  = '//*[@id="login"]'
        xpathPass  = '//*[@id="senha"]'
        xpathLogin = '/html/body/div[1]/section/form/div[5]/button'
        username   = "vilellagds@gmail.com"
        password   = "Werq9137di"
        # username   = "ericashima@yahoo.com.br"
        # password   = "thbvbbmth"

        loginDizu  = LoginDizu.Login(driver,xpathUser,xpathPass,xpathLogin,username,password)
        loginDizu.fillUser()
        loginDizu.fillPass()
        loginDizu.clickLogin()
        chrome.hasInjectedJS = False

        stage      = "DizuLogin" 
        viewport   = device.name
        userAgent  = chrome.userAgent
        errorNum   = ErrorDizu.Error.getErrorNumber(driver)
        noticeNum  = NoticeDizu.Notice.getNoticeNumber(driver)
        if(errorNum!=False):                       
            event   = "error"                        
            value   = ErrorDizu.Error.getErrorValue(errorNum)
            content = ErrorDizu.Error.getErrorContent(errorNum)                
            log.generateLogData(driver, tempPath, processId, username, stage, event, value, content, viewport, userAgent)
        else:
            while(noticeNum!=False):
                event   = "notice"                                
                value   = NoticeDizu.Notice.getNoticeValue(noticeNum)
                content = NoticeDizu.Notice.getNoticeContent(noticeNum)
                log.generateLogData(driver, tempPath, processId, username, stage, event, value, content, viewport, userAgent)
                NoticeDizu.Notice.noticeHandler(driver, noticeNum, loginDizu)
                chrome.hasInjectedJS = False
                noticeNum  = NoticeDizu.Notice.getNoticeNumber(driver)

            event   = "ok"                        
            value   = "login success"
            content = ""
            log.generateLogData(driver, tempPath, processId, username, stage, event, value, content, viewport, userAgent)
            chrome.getRestries('https://dizu.com.br/painel/conectar', 3, 10)

            xpathInstaAcc    = '//*[@id="instagram_id"]'
            xpathIniciar     = '//*[@id="iniciarTarefas"]'
            xpathVerLink     = '//*[text()[contains(., "Ver link")]]' 
            xpathConfirmar   = '//*[text()[contains(., "confirmar")]]'
            xpathPularTarefa = '//*[text()[contains(., "Pular Tarefa")]]'

            contectarDizu = ConectarDizu.Conectar(driver,xpathInstaAcc,xpathIniciar,xpathVerLink,xpathConfirmar,xpathPularTarefa)
            contectarDizu.fillinstaAcc(loginInsta.username)
            contectarDizu.clickIniciar()

            stage   = "DizuConectar"
            event   = "ok"                        
            value   = "connected successfully"
            content = ""
            log.generateLogData(driver, tempPath, processId, username, stage, event, value, content, viewport, userAgent)            

            for x in range(15):
                contectarDizu.verificarDisponibilidadeTarefas(log,tempPath,processId,username,viewport,userAgent)
                contectarDizu.clickVerLink()
                chrome.hasInjectedJS = False
                
                #Go to insta tab
                driver.switch_to.window(driver.window_handles[-1])
                noticeNum     = NoticeInsta.Notice.getNoticeNumber(driver)
                errorNum      = ErrorInsta.Error.getErrorNumber(driver)
                if errorNum!= False:
                    time.sleep(10)
                    stage   = "InstaFollow"
                    event   = "error"                        
                    value   = ErrorInsta.Error.getErrorValue(errorNum)
                    content = ErrorInsta.Error.getErrorContent(errorNum)
                    log.generateLogData(driver, tempPath, processId, username, stage, event, value, content, viewport, userAgent)                                                
                elif noticeNum == 4 or noticeNum == 5:#perfil privado ou que ja foi seguindo anteriormente
                    time.sleep(10)
                    stage   = "InstaFollow"
                    event   = "notice"                        
                    value   = NoticeInsta.Notice.getNoticeValue(noticeNum)
                    content = NoticeInsta.Notice.getNoticeContent(noticeNum)
                    log.generateLogData(driver, tempPath, processId, username, stage, event, value, content, viewport, userAgent)                                
                    #close insta tab
                    driver.close()
                    #go back to dizu tab
                    driver.switch_to.window(driver.window_handles[-1])                    
                    time.sleep(6)

                    stage   = "Pre pular tarefa"
                    event   = "notice"                        
                    value   = NoticeInsta.Notice.getNoticeValue(noticeNum)
                    content = NoticeInsta.Notice.getNoticeContent(noticeNum)
                    log.generateLogData(driver, tempPath, processId, username, stage, event, value, content, viewport, userAgent)                                

                    #Por enquanto confirmo que segui o seguidor privado no futuro pular tarefa
                    #contectarDizu.clickPularTarefa()
                    contectarDizu.clickConfirmar()

                    time.sleep(12)
                    stage   = "Pos pular tarefa"
                    event   = "notice"                        
                    value   = NoticeInsta.Notice.getNoticeValue(noticeNum)
                    content = NoticeInsta.Notice.getNoticeContent(noticeNum)
                    log.generateLogData(driver, tempPath, processId, username, stage, event, value, content, viewport, userAgent)                                
                    time.sleep(6)

                else:
                    time.sleep(10)
                    xpathFollow   = "//*[text()='Follow']"
                    followInsta   = FollowInsta.Follow(driver,xpathFollow)                    
                    followInsta.clickFollow()

                    stage   = "InstaFollow"
                    event   = "ok"                        
                    value   = "Followed successfully"
                    content = ""
                    log.generateLogData(driver, tempPath, processId, username, stage, event, value, content, viewport, userAgent)  

                    print("Followed:" + str(x))              
                    driver.close()
                    driver.switch_to.window(driver.window_handles[-1])
                    time.sleep(4)
                    contectarDizu.clickConfirmar()
                    stage   = "DizuConfirmar"
                    event   = "ok"                        
                    value   = "Confirmed successfully"
                    content = ""
                    log.generateLogData(driver, tempPath, processId, username, stage, event, value, content, viewport, userAgent)
finally:
    if(errorNum!=False):
        event   = "error"
        value   = "Failed"
        content = "Process finished over failure."
    else:
        event   = "end"
        value   = "process completed"
        content = ""

    username  = ""
    stage     = "End"
    viewport  = device.name
    userAgent = chrome.userAgent           
    log.generateLogData(driver, tempPath, processId, username, stage, event, value, content, viewport, userAgent)
    #for handle in driver.window_handles:
        #print (handle)

    #driver.close()
    driver.quit()