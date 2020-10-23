import os
import sys

sys.path.append('/home/centos/www/Bibliotecas/')
import Config

sys.path.append('/home/centos/www/Classes/Instagram')
import ErrorInsta
import NoticeInsta

sys.path.append('/home/centos/www/Classes/Dizu')
import ErrorDizu
import NoticeDizu

class ErrorHandler(object):
    def __init__(self,browser,log):
        self.browser     = browser
        self.driver      = browser.webdriver
        self.log         = log        
        self.lastError   = False
        self.lastNotice  = False
        self.ignoreListNotice  = []
        self.ignoreListError   = []
            
    def handle(self, handler, username, stage):
        viewport   = self.log.device
        userAgent  = self.browser.userAgent
        driver     = self.driver

        processId  = os.getpid()
        tempPath   = Config.getTempPath()

        if handler  == "Instagram":
            error      = ErrorInsta.Error
            notice     = NoticeInsta.Notice
        elif handler == "Dizu":
            error      = ErrorDizu.Error
            notice     = NoticeDizu.Notice

        errorNum   = error.getErrorNumber(driver)
        noticeNum  = notice.getNoticeNumber(driver)
        if(errorNum!=False and errorNum not in self.ignoreListError):
            self.lastError = errorNum
            event   = "error"    
            value   = error.getErrorValue(errorNum)
            content = error.getErrorContent(errorNum)
            self.log.generateLogDataSelenium(driver, tempPath, processId, username, stage, event, value, content, viewport, userAgent)
            ok      = False
        else:
            while(noticeNum!=False and noticeNum not in self.ignoreListNotice):
                self.lastNotice = noticeNum
                event   = "notice"                        
                value   = notice.getNoticeValue(noticeNum)
                content = notice.getNoticeContent(noticeNum)
                self.log.generateLogDataSelenium(driver, tempPath, processId, username, stage, event, value, content, viewport, userAgent)
                notice.noticeHandler(driver, noticeNum)
                self.browser.hasInjectedJS = False
                noticeNum  = notice.getNoticeNumber(driver)

            ok = True

        return ok
