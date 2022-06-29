from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import  By
import login

class Filiais:
    def __init__(self):
        self.driver = webdriver.Chrome
        login.Login.__init__(self)
        login.Login.abrir_site(self)
        login.Login.usuario(self)
        login.Login.senha(self)
        login.Login.botaoiniciar(self)
        login.Login.selecionar_filial(self)

    def patient(self):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '.module-item:nth-child(3) .title').click() #modulo pacientes
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, 'div.page:nth-child(2) > div:nth-child(1)').click() #side bar