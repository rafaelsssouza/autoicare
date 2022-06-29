from operator import contains
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import  By

chaves = open("chaves.txt", "r")
user = chaves.readline()
senha = chaves.readline()


class Login:
    def __init__(self):
        print("Iniciando o login...")
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
            },
            "filiais":{
                "participações":":nth-child(3) > .item > span",
                
                "sp":":nth-child(23) > span:nth-child(2)"
            }
        }

    def abrir_site(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window() 
        sleep(2)
        self.driver.get(self.site_link)
        sleep(2)

    def usuario(self): #usuario
        self.driver.find_element(By.ID, self.site_map["campos"]["username"]["id"]).send_keys(user)
        
    def senha(self): #senha
        self.driver.find_element(By.ID, self.site_map["campos"]["password"]["id"]).send_keys(senha)
        
    def olhinho(self): #olhinho
        self.driver.find_element(By.XPATH, self.site_map["button"]["eye"]["xpath"]).click()   
        
    def botaoiniciar(self): #button login
        self.driver.find_element(By.XPATH, self.site_map["button"]["arrow"]["xpath"]).click()
        print("Login realizado.....")
        
    def selecionar_filial(self): #filial
        sleep(4)
        self.driver.find_element(By.CSS_SELECTOR, self.site_map["filiais"]["participações"]).click()
