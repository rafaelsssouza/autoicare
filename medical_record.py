from random import random
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import  By
import patient
import random

class Prontuario:
    def __init__(self):
        self.driver = webdriver.Chrome
        patient.Patient.__init__(self)
        patient.Patient.search_patient(self)
        patient.Patient.actions(self)
        
    def dados_patient(self):
        self.driver.find_element(By.CSS_SELECTOR, ':nth-child(1) > div:nth-child(1) > p:nth-child(3)').click()

    def dados_patient_form_operational_core(self):
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, 'div.accordion-border:nth-child(1) > app-accordion-tab:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)').click()
        #print('2 = A , 3 = B , 4 = C , 5 = D , 6 = E , 1 = Equipe ')
        equipe = random.randrange(2,5)  #int(input('Selecione a Equipe: '))
        self.driver.find_element(By.XPATH, '//app-operational-core/div/div[2]/app-form-input/div/span/select/option[{}]'.format(equipe)).click() #Equipe
        #print('Digite 1 para ID 2 para AD')
        program_type = random.randrange(1,2)  #input('Selecione um valor: '))
        self.driver.find_element(By.XPATH, '//div/app-operational-core/div/div[3]/app-form-input/div/span/select/option[{}]'.format(program_type)).click()

    def quit(self):
        sleep(10)
        self.driver.close()

teste = Prontuario()
teste.dados_patient()
teste.dados_patient_form_operational_core()
teste.quit()