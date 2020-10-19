import requests
import json 
import sys

sys.path.append('/home/centos/www/Bibliotecas/Requests')
import ErrorHandlerRequests

class Login(object):
    def __init__(self,log,username,password):
        self.log      = log
        self.username = username
        self.password = password
        self.cookies  = False
             
    def login (self):
        url      = 'https://dizu.com.br/painel/login'
        body     = {'login' : self.username, 'senha': self.password}

        try:
            response = requests.post(url, data = body)

            content   = response.text
            content   = json.loads(content)
            cookies   = response.cookies

            cfduid    = cookies.__dict__['_cookies']['.dizu.com.br']['/']['__cfduid'].__dict__['value']
            crsftoken = content["id"]

            self.cookies  = {'cfduid': cfduid , 'crsftoken' : crsftoken}
            ok = True
        except:
            self.cookies  = False
            handler = "Dizu"
            event   = "error"
            value   = ""
            content = ""
            stage   = "DizuLogin"              
            ErrorHandlerRequests.errorHandler(handler, event, value, content, self.username, stage, self.log)
            ok = False

        return ok
