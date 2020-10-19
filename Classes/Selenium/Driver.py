import sys

sys.path.append('/home/centos/www/Bibliotecas/Selenium')
import FakeUserAgent
import ScriptsInjection

from gzip import compress, decompress
#from urllib.parse import urlparse
from lxml import html
from lxml.etree import ParserError
from lxml.html import builder
from seleniumwire import webdriver #do not import drive from selenium, in order to make script injection to work we must import from seleniumwire
from selenium.webdriver.chrome.options import Options

class Chrome(object):
    def __init__(self):
        self.userAgent = FakeUserAgent.getRandomAgent()

        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        #Para ativar aba anonima descomentar abaixo
        #chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--window-size=1280x1696')
        #Para salvar dados de navegação, login, cookies e navegar como usuário do chrome descomentar abaixo
        #chrome_options.add_argument('--user-data-dir=/tmp/user-data')
        chrome_options.add_argument('--hide-scrollbars')
        chrome_options.add_argument('--enable-logging')
        chrome_options.add_argument('--log-level=0')
        chrome_options.add_argument('--v=99')
        chrome_options.add_argument('--single-process')
        chrome_options.add_argument('--data-path=/tmp/data-path')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--homedir=/tmp')
        chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
        #Adicionei a linha abaixo pois estava dando alguns erros de certificado, se voltar a dar erro de SLL rever a solucao
        #chrome_options.add_argument("--disable-web-security") continua dando erro, entao comentei
        chrome_options.add_argument(f'user-agent={self.userAgent}')
        chrome_options.binary_location = "/usr/bin/google-chrome"
        
        #Opcoes para funcionar download
        chrome_options.add_argument('--verbose')
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument('--disable-software-rasterizer')
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": "/tmp/",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
        })
        seleniumwire_options = {
            'custom_response_handler': self.inject
        }
        self.webdriver = webdriver.Chrome(chrome_options=chrome_options,seleniumwire_options=seleniumwire_options)
        self.webdriver.header_overrides = {'Accept-Encoding': 'gzip'} #to enable js script injection ensure we only get gzip encoded responses  
        self.hasInjectedJS = False

    def set_viewport_size(self, width, height):
        window_size = self.webdriver.execute_script("""
            return [window.outerWidth - window.innerWidth + arguments[0],
            window.outerHeight - window.innerHeight + arguments[1]];
            """, width, height)
        self.webdriver.set_window_size(*window_size)        

    def inject(self, req, req_body, res, res_body):
        #print ("subtype")
        #print(res.headers.get_content_subtype() )
        #print ("status")
        #print(res.status)
        #print ("Content-Encoding")
        #print(res.getheader)
        #print("res")
        #print(bytes(self.getFakePlugins(),'utf-8') + decompress(res_body))
        scripts       = ScriptsInjection.getAll()
        subtype       = res.headers.get_content_subtype()
        status        = res.status
        contentEncode = res.getheader('Content-Encoding')

        # various checks to make sure we're only injecting the script on appropriate responses
        # we check that the content type is HTML, that the status code is 200, and that the encoding is gzip
        if subtype == "javascript" and self.hasInjectedJS==False:
            self.hasInjectedJS=True
            return compress(bytes(scripts,'utf-8') + decompress(res_body))
        elif subtype == "html":
            script_elem_to_inject = builder.SCRIPT(scripts)
            if status != 200 or contentEncode != 'gzip':
                return None
            try:
                parsed_html = html.fromstring(decompress(res_body))
            except ParserError:
                return None
            try:
                parsed_html.head.insert(0, script_elem_to_inject)
            except IndexError: # no head element
                return None
            self.hasInjectedJS=True
            return compress(html.tostring(parsed_html))

    def getRetries(self, url, retries, timeout):
        driver = self.webdriver
        driver.set_page_load_timeout(timeout)
        for x in range(retries - 1):
            try:
                ok = True
                driver.get(url)
                break
            except:
                ok = False
                pass    
            self.hasInjectedJS = False
        return ok