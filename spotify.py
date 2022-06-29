from webbrowser import Chrome
from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from playsound import playsound
import recognition

arquivo = open('spotify.txt' , 'r')
usuario = arquivo.readline()
senha = arquivo.readline()

class Spotify:
    def __init__(self):
        self.driver = Chrome()
        self.url = ('https://open.spotify.com/')
        
    def goodmorning(self):
        playsound('audio\GoodMorning.mp3')
        print("Have a Nice Day")
        
    def openspotify(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(2)
    
    def loginspotify(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button:nth-child(2) > div:nth-child(1)').click()
        sleep(3)
    
    def pagelogin(self):
        self.driver.find_element(By.ID,'login-username').send_keys(usuario)
        self.driver.find_element(By.ID,'login-password').send_keys(senha)
        self.driver.find_element(By.CSS_SELECTOR,'.ButtonInner-sc-14ud5tc-0').click()
    
    def selecionar_musica(self):
        sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/nav/div[1]/ul/li[2]/a').click()
        sleep(2)
        ## qual o nome da playlist que gostaria de ouvir hoje senhor?
        selec_music = recognition.Reconhecimento.ouvir_microfone()
        
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[1]/header/div[3]/div/div/form/input').send_keys(selec_music)
        sleep(3)
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[2]/div/div/section[1]/div[2]/div/div/div/div[4]').click()
    
testezinho = Spotify()
testezinho.goodmorning()
testezinho.openspotify()
testezinho.loginspotify()
testezinho.pagelogin()
testezinho.selecionar_musica()