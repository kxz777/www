class HTML(object):
    def __init__(self, driver, path):
        self.driver   = driver
        self.path = path

    def save(self, name):
        res = self.driver.page_source    
        full_path = self.path + "/" + name + ".html"
        f= open(full_path,"w+")
        f.write(res)
        f.close() 
        return full_path

class Screenshot(object):
    def __init__(self, driver, path):
        self.driver   = driver
        self.path = path

    def save(self, name):
        full_path = self.path + "/" + name  + ".png"
        self.driver.save_screenshot(full_path)
        return full_path