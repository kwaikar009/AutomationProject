import configparser

conf = configparser.RawConfigParser()
conf.read(".\\configurations\\config.ini")

class readConfig:
    @staticmethod
    def getAppUrl():
        appUrl= conf.get('common info','baseUrl')
        return appUrl


    @staticmethod
    def getUserName():
        userName= conf.get('common info','userName')
        return userName

    @staticmethod
    def getPassword():
        password= conf.get('common info','password')
        return password