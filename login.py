from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import  By

chaves = open("userpass.txt", "r")
user = chaves.readline()
senha = chaves.readline()

class login:
    def __init__(self):
        self.site_link = 'https://icarehml.homedoctor.com.br:8090/'
        self.site_map = {
            "campos":{
                "username":{
                    "id":"username"
                },
                "password":{
                    "id":"pass"
                }
            },
            "button":{
                "eye":{
                    "xpath":"/html/body/app-root/app-login-page/div/div/div[2]/div[2]/fa-icon[2]"
                },
                "arrow":{
                    "xpath":"/html/body/app-root/app-login-page/div/div/div[2]/button/fa-icon"
                }
            }
        }
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
    def abrir_site(self):
        sleep(2)
        self.driver.get(self.site_link)
        sleep(2)

    def usuario(self): #usuario
        self.driver.find_element(By.ID, self.site_map["campos"]["username"]["id"]).send_keys(user)
        
    def senha(self): #senha
        self.driver.find_element(By.ID, self.site_map["campos"]["password"]["id"]).send_keys(senha)
        
    def olhinho(self):
        self.driver.find_element(By.XPATH, self.site_map["button"]["eye"]["xpath"]).click()   
        
    def botaoiniciar(self):
        self.driver.find_element(By.XPATH, self.site_map["button"]["arrow"]["xpath"]).click()
        
    def selecionar_filial(self):
        sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ':nth-child(3) > .item > span').click()

class pagelogin():
    url = login()
    url.abrir_site()
    url.usuario()
    url.senha()
    url.botaoiniciar()
    url.selecionar_filial()

