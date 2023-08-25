#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install requests')


# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import pandas as pd


# In[2]:


get_ipython().run_cell_magic('time', '', "\nlink = 'https://www.h9j.com.br/pt/pacientes-e-visitantes/convenios-e-planos'\nurl = requests.get(link)\n\n# confirma se houve conexão com o site em questão\nif url.status_code == 200:\n    print('Conexão realizada com sucesso!')\n")


# In[4]:


get_ipython().run_cell_magic('time', '', '# Abrindo o navegador\nnavegador = webdriver.Chrome()\nnavegador.get(link)\ntime.sleep(5)\n\n# pega o nome da coluna que desejamos\ncoluna = navegador.find_element(By.XPATH, \n            \'//th[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]\').text\n\n# carrega toda a informação da página\nfor i in range(1, 48):\n    navegador.find_element(By.XPATH, \n        \'//*[@id="DeltaPlaceHolderMain"]/div[1]/section[2]/div/div[2]/div[4]/button\').send_keys("\\n")\n    time.sleep(10)\nprint("Página Carregada com Sucesso!")\n')


# In[17]:


get_ipython().run_cell_magic('time', '', '# intera todos os nomes dos convênios disponíveis.\nconvenios = []\nfor i in range(1, 480):\n    convenios.append(navegador.find_element(By.XPATH, \n    f\'//*[@id="DeltaPlaceHolderMain"]/div[1]/section[2]/div/div[2]/div[3]/table/tbody/tr[{i}]/th\').text)\n\n## confirmamos os valores obtidos e o tamnho da lista\nprint(convenios), len(convenios), type(convenios)\n')


# In[ ]:





# In[ ]:




