import requests
import re
import sys

sys.path.append('/home/centos/www/Bibliotecas/Requests')
import ErrorHandlerRequests

class Conectar(object):

    def __init__(self, log, login):
        self.log   = log
        self.login = login

    def getAccountId(self, accountName):
        cookies  = self.login.cookies
        url      = 'https://dizu.com.br/painel/conectar'
        response = requests.get(url, cookies = cookies)

        subject  = response.text
        pattern  = '<option value=\"([0-9]+)\".*>'+accountName+'<\/option>'
        matches  = re.search(pattern, subject, re.IGNORECASE)

        if(matches == None):
            handler = "Dizu"
            event   = "error"
            value   = ""
            content = ""
            stage   = "DizuConectarGetAccId"              
            ErrorHandlerRequests.errorHandler(handler, event, value, content, accountName, stage, self.log)

            res = False
        else:
            res = matches.group(1)

        return res

    def getTask(self, accountId):
        cookies  = self.login.cookies
        url      = "https://dizu.com.br/painel/listar_pedido/?conta_id="+accountId+"&twitter_id=Twitter&tarefa10=0&curtida05=0&estado=SP"
        response = requests.get(url, cookies = cookies)

        subject  = response.text
        pattern  = "data-tarefa_id=[\"']([0-9].+)[\"']\s"
        matches  = re.search(pattern, subject, re.IGNORECASE)

        if(matches == None):
            res = False
        else:
            taskId   = matches.group(1)

            subject  = response.text
            pattern  = "href=[\"']https://instagram.com/(.+)[\"']\sid"
            matches  = re.search(pattern, subject, re.IGNORECASE)
            if(matches == None):
                res = False
            else:      
                instaLink = matches.group(1)  
                res       = {'taskId' : taskId, 'instaLink' : instaLink}

        if res == False:
            handler = "Dizu"
            event   = "notice"
            value   = ""
            content = ""
            stage   = "DizuConectarGetTask"              
            ErrorHandlerRequests.errorHandler(handler, event, value, content, accountId, stage, self.log)

        return res

    def confirmTask(self, accountId, task):
        cookies  = self.login.cookies
        url      = 'https://dizu.com.br/painel/confirmar_pedido'
        body     = {'tarefa_id' : task['taskId'], 'conta_id': accountId, 'realizado' : 1}

        try:
            response = requests.post(url, data = body , cookies = cookies)    
            response = response.text
        except:
            response = False

        return response