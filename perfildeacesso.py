from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import  By
from login import pagelogin


class selectpage:
    def __init__(self):
        self.site_link = 'https://icarehml.homedoctor.com.br:8090/select-profile'
        self.driver = webdriver.Chrome()
        
        
    def abrirpage(self):
        time.sleep(5)
        self.driver.get(self.site_link)

url2 = selectpage
url2.abrirpage
url2.close()
