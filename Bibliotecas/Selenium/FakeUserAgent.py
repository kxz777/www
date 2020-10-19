from fake_useragent import UserAgent

def getRandomAgent():
    ua = UserAgent()
    try:
        userAgent = ua.random
    except:
        userAgent = 'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'        
    return userAgent