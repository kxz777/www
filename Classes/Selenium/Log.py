import os.path
import csv
import datetime as DT
import sys

sys.path.append('/home/centos/www/Classes/Selenium')
import Debug

class LogCSV(object):
    def __init__(self, path, fileName, fields):
        self.path       = path
        self.fileName   = fileName
        self.fields     = fields  #['event', 'code', 'time']
        self.fullPath   = self.path + "/" + self.fileName + ".csv"
        self.delimiter  = ','
        self.quotechar  = '"'
        self.quoting    = csv.QUOTE_ALL

        if not os.path.isfile(self.fullPath):
            self.createNewFile()

    #tira print do webdriver, salva html e console JS  
    def generateLogDataSelenium(self, driver, tempPath, processId, username, stage, event, value, content, viewport, userAgent):
        name    = stage + "_" + event + ": " + DT.datetime.now().strftime("%Y_%m_%d %H:%M:%S")        
        date    = DT.datetime.now().strftime("%d/%m/%Y")
        hour    = DT.datetime.now().strftime("%H:%M:%S")        
        png     = Debug.Screenshot(driver,tempPath).save(name)
        html    = Debug.HTML(driver,tempPath).save(name)
        js      = driver.get_log('browser')
        self.insert([processId,username,date,hour,event,stage,value,content,png,html,js,viewport,userAgent])

    #semelhante ao generateLogDataSelenium mas nao tira print e nem salva arquivos
    def generateLogDataRequests(self, tempPath, processId, username, stage, event, value, content, viewport, userAgent):
        name    = stage + "_" + event + ": " + DT.datetime.now().strftime("%Y_%m_%d %H:%M:%S")        
        date    = DT.datetime.now().strftime("%d/%m/%Y")
        hour    = DT.datetime.now().strftime("%H:%M:%S")        
        png     = ''
        html    = ''
        js      = ''
        self.insert([processId,username,date,hour,event,stage,value,content,png,html,js,viewport,userAgent])

    def createNewFile(self):
        with open(self.fullPath, 'a+', newline='') as newFile:
            newFile = csv.writer(newFile, self.quoting)
            newFile.writerow(self.fields)

    def insert(self, values):
        with open(self.fullPath, 'a+', newline='') as oldFile:
            oldFile = csv.writer(oldFile, self.quoting)
            oldFile.writerow(values)