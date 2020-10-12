import requests
import json
import re

def getAccountId(accountName, cookies):
    url      = 'https://dizu.com.br/painel/conectar'
    response = requests.get(url, cookies = cookies)
    subject  = response.text
    pattern  = '<option value=\"([0-9]+)\".*>'+accountName+'<\/option>'
    matches  = re.search(pattern, subject, re.IGNORECASE)
    if(matches == None):
        res = False
    else:
        res = matches.group(1)
    return res

def getTask(accountId, cookies):
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
    return res

def confirmTask(accountId, task, cookies):
    url      = 'https://dizu.com.br/painel/confirmar_pedido'
    body     = {'tarefa_id' : task['taskId'], 'conta_id': accountId, 'realizado' : 1}
    print (body)
    response = requests.post(url, data = body , cookies = cookies)    
    return response.text