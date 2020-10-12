import requests
import json

def login (username, password):
    url      = 'https://dizu.com.br/painel/login'
    body     = {'login' : username, 'senha': password}
    response = requests.post(url, data = body)

    content   = response.text
    content   = json.loads(content)
    cookies   = response.cookies

    cfduid    = cookies.__dict__['_cookies']['.dizu.com.br']['/']['__cfduid'].__dict__['value']
    crsftoken = content["id"]

    return {'cfduid': cfduid , 'crsftoken' : crsftoken}