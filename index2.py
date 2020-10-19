import os
import sys
import time

sys.path.append('/home/centos/www/Classes/Selenium')
import Devices
import Driver
import Log

sys.path.append('/home/centos/www/Classes/Instagram')
import LoginInsta
import FollowInsta

sys.path.append('/home/centos/www/Classes/Dizu')
import LoginDizu
import ConectarDizu

sys.path.append('/home/centos/www/Bibliotecas/')

import Config

#Generate random device to change browser viewport and bypass recaptcha
device = Devices.Device('', True)
chrome = Driver.Chrome()
chrome.set_viewport_size(device.width,device.height)

tempPath   = Config.getTempPath()
fileName   = "log"
fields     = ["ID","Account","Date","Time","Event","Stage","Value","Content","png","html","js","ViewPort","User-Agent"]
log        = Log.LogCSV(tempPath, fileName, fields)
log.device = device.name

try:
    ok = chrome.getRetries('https://www.instagram.com', 3, 10)

    if ok == True:
        xpathUser  = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input'
        xpathPass  = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input'
        xpathLogin = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button'
        userInsta  = "spontaneousdrawing4fun"
        passInsta  = "WF4vYL5aMYDu5uy"

        loginInsta = LoginInsta.Login(chrome,log,xpathUser,xpathPass,xpathLogin,userInsta)        
        loginInsta.fillUser(userInsta)
        loginInsta.fillPass(passInsta)
        ok = loginInsta.clickLogin()        

        if ok == True:
            userDizu  = 'vilellagds@gmail.com'
            passDizu  = 'Werq9137di'
            loginDizu = LoginDizu.Login(log, userDizu, passDizu)
            ok = loginDizu.login()

            if ok == True:
                concectarDizu = ConectarDizu.Conectar(log, loginDizu)
                accountId     = concectarDizu.getAccountId(loginInsta.username)
                ok            = accountId
                if ok != False:           
                    for x in range(2):
                        task = concectarDizu.getTask(accountId)
                        if task != False:
                            taskId        = task['taskId']
                            instaLink     = task['instaLink']
                            instaLink     = 'https://www.instagram.com/' + instaLink                                        
                            xpathFollow   = "//*[text()='Follow']"
                            followInsta   = FollowInsta.Follow(chrome,log,loginInsta,xpathFollow)                    

                            ok = followInsta.follow(instaLink)

                            if ok==False:
                                break
                            else:
                                print ("Followed: " + str(x))
finally:
    if(ok==False):
        event   = "error"
        value   = "Failed"
        content = "Process finished over failure."
    else:
        event   = "ok"
        value   = "process completed"
        content = "Success!"

    processId = os.getpid()
    username  = ""
    stage     = "End"
    viewport  = device.name
    userAgent = chrome.userAgent           
    driver    = chrome.webdriver
    time.sleep(4)
    log.generateLogDataSelenium(driver, tempPath, processId, username, stage, event, value, content, viewport, userAgent)

    driver.quit()    