from turtle import end_fill
import speech_recognition as sr

class Reconhecimento:
#Função para ouvir e reconhecer a fala
    def ouvir_microfone():
        #Habilita o microfone do usuário
        microfone = sr.Recognizer()
        #usando o microfone
        with sr.Microphone() as source:
            
            #Chama um algoritmo de reducao de ruidos no som
            microfone.adjust_for_ambient_noise(source)
            
            #Frase para o usuario dizer algo
            print("Fale um cantor, música ou playlist: ")
            
            #Armazena o que foi dito numa variavel
            audio = microfone.listen(source)
            
        try:
            #Passa a variável para o algoritmo reconhecedor de padroes
            frase = microfone.recognize_google(audio,language='pt-BR')
            
            #Retorna a frase pronunciada
            print("Você disse: " + frase)
            
        #Se nao reconheceu o padrao de fala, exibe a mensagem
        except sr.UnknownValueError:
            print("Não entendi")
            
        return frase
