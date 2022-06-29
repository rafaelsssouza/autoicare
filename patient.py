from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import  By
import modules

nome_do_paciente = '[eqmagnt] - Testes'
#input('Digite o nome do paciente: ')
nome_do_paciente = nome_do_paciente.capitalize()

olhinho = 1
lapis = 2
tomada = 3
integracaogm = 4
qrcode = 5
prontuario = 6

class Patient:
    def __init__(self):
        self.driver = webdriver.Chrome
        modules.Filiais.__init__(self)
        modules.Filiais.patient(self)
    
    def search_patient(self):
        sleep(4)    
        self.driver.find_element(By.TAG_NAME, 'input').send_keys(nome_do_paciente) ## Nome do paciente 
        self.driver.find_element(By.CSS_SELECTOR, '.filters > .buttons > :nth-child(2) > .btn').click() ## CONSULTAR
        sleep(2)
    
    def actions(self):
        self.driver.find_element(By.CSS_SELECTOR, ':nth-child(1) > td:nth-child(12) > section:nth-child(1) > fa-icon:nth-child({})'.format(prontuario)).click() #selecionar uma variavel
        sleep(2)
    
    def init_captation(self):
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '.support-title').click()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,'button.btn:nth-child(2)').click()
        sleep(3)