
#Importar a biblioteca
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

chrome = webdriver.Chrome()
chrome.implicitly_wait(2)
chrome.get('https://webscraper.io/test-sites/tables')
titule_page = chrome.title


#Encontra elementos pela nome da tag td
table_dados = chrome.find_elements(By.TAG_NAME, 'td')# td = tabledatda

linhas = []
celulas = []
colunas = 4
contador_coluna = 0
for dados in table_dados:
    contador_coluna = contador_coluna +1
    celulas.append(dados.text)
    if contador_coluna == colunas:
        linhas.append(celulas)
        celulas = []
        contador_coluna = 0


df = pd.DataFrame(linhas, columns=['#','First Name','Last Name','User Name'])
print(df)
df.to_csv('Alunos Senai 2 WEBSCRAPER.csv')