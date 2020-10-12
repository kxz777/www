import random

class Device(object):
    def __init__(self, name, randomly):

        if randomly == True:
            name = random.choice(self.getDevicesList())
        self.name   = name
        self.width  = self.getWidth(name)
        self.height = self.getHeight(name)

    def getDevicesList(self):
        lis = [
            'Moto G4',
            'Galaxy S5',
            'Pixel2',
            'Pixel2 XL',
            'iPhone5',
            'iPhoneSE',
            'iPhone6',
            'iPhone7',
            'iPhone8',
            'iPhone6 Plus',
            'iPhone7 Plus',
            'iPhone8 Plus',
            'iPhoneX',
            'iPad',
            'iPad Pro',
            'Surface Duo',
            'Galaxy Duo'            
        ]

        return lis

    def getWidth(self, name):
        dic = {
            'Moto G4'     : 360,
            'Galaxy S5'   : 360,
            'Pixel2'      : 411,
            'Pixel2 XL'   : 411,
            'iPhone5'     : 320,
            'iPhoneSE'    : 320,
            'iPhone6'     : 375,
            'iPhone7'     : 375,
            'iPhone8'     : 375,
            'iPhone6 Plus': 414,
            'iPhone7 Plus': 414,
            'iPhone8 Plus': 414,
            'iPhoneX'     : 375,
            'iPad'        : 768,
            'iPad Pro'    : 1024,
            'Surface Duo' : 540,
            'Galaxy Duo'  : 280
        }

        return dic[name]

    def getHeight(self, name):
        dic = {
            'Moto G4'     :640,
            'Galaxy S5'   :640,
            'Pixel2'      :731,
            'Pixel2 XL'   :823,
            'iPhone5'     :568,
            'iPhoneSE'    :568,
            'iPhone6'     :667,
            'iPhone7'     :667,
            'iPhone8'     :667,
            'iPhone6 Plus':736,
            'iPhone7 Plus':736,
            'iPhone8 Plus':736,
            'iPhoneX'     :812,
            'iPad'        :1024,
            'iPad Pro'    :1366,
            'Surface Duo' :720,
            'Galaxy Duo'  :653
        }        

        return dic[name]