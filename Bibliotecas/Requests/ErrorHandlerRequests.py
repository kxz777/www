import os
import sys

sys.path.append('/home/centos/www/Bibliotecas/')
import Config

def errorHandler(handler, event, value, content, username, stage, log):
    viewport   = ""
    userAgent  = "python request"
    processId  = os.getpid()
    tempPath   = Config.getTempPath()

    if handler  == "Instagram":
        #placeholder
        pass
    elif handler == "Dizu":
        #placeholder
        pass

    log.generateLogDataRequests(tempPath, processId, username, stage, event, value, content, viewport, userAgent)
