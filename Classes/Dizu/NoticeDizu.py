class Notice:
    @staticmethod
    def getNoticeNumber(driver):
        content = driver.page_source
        if "place holderUm ou mais erros ocorrem. Verifique os dados informados" in content:
            notice = 1
        else:
            notice = False
        return  notice

    @staticmethod
    def getNoticeValue(noticeNum):
        if noticeNum == 1:
            res = "login error"  
        else:
            res = False        
        return res

    @staticmethod
    def getNoticeContent(noticeNum):
        if noticeNum == 1:
            res = "Notice1"
        else:
            res = False
        print ("Dizu " + res)
        return res

    @staticmethod
    def noticeHandler(driver, noticeNum, loginDizu):
        if noticeNum == 1:
            print ("placeholder")
