from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import pandas as pd


link = 'https://www.h9j.com.br/pt/pacientes-e-visitantes/convenios-e-planos'
url = requests.get(link)

# confirma se houve conexão com o site em questão
if url.status_code == 200:
    print('Conexão realizada com sucesso!')


%%time
# Abrindo o navegador
navegador = webdriver.Chrome()
navegador.get(link)
time.sleep(5)

# pega o nome da coluna que desejamos
coluna = navegador.find_element(By.XPATH, 
            '//th[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]').text

# carrega toda a informação da página
for i in range(1, 48):
    navegador.find_element(By.XPATH, 
        '//*[@id="DeltaPlaceHolderMain"]/div[1]/section[2]/div/div[2]/div[4]/button').send_keys("\n")
    time.sleep(10)
print("Página Carregada com Sucesso!")


%%time
# intera todos os nomes dos convênios disponíveis.
convenios = []
for i in range(1, 480):
    convenios.append(navegador.find_element(By.XPATH, 
    f'//*[@id="DeltaPlaceHolderMain"]/div[1]/section[2]/div/div[2]/div[3]/table/tbody/tr[{i}]/th').text)

## confirmamos os valores obtidos e o tamnho da lista
print(convenios), len(convenios), type(convenios)
