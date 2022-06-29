from certifi import where
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import  By
import login
from random import randrange

inicio = False
fim = False

numero = randrange(0,100)

class repeticao1():
    def repeticao(self):
        self.driver = webdriver.Chrome
        login.Login.__init__(self)
        login.Login.abrir_site(self)
        login.Login.usuario(self)
        login.Login.senha(self)
        login.Login.botaoiniciar(self)
        login.Login.selecionar_filial(self)

    def url_new(self):
        self.driver.get('https://icarehml.homedoctor.com.br:8090/captation/patient/{}'.format(numero))
        
teste1 = repeticao1()
teste1.repeticao()
teste1.url_new()