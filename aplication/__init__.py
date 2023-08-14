from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

from aplication.models.refrigerante_model import refrigerante_model

url = 'https://landing-page-coca-cola-clone.netlify.app/'
refrigerantes_model = []
column_order = ['Descrição', 'Foto']
classes_css = ['baunilha-e-zero', 'coke', 'origins']

driver = webdriver.Chrome()

driver.get(url)

for classe in classes_css:
    refrigerante_obj = driver.find_element(By.CLASS_NAME, classe)
    descricao = refrigerante_obj.find_element(By.TAG_NAME, 'img').get_attribute("src")
    foto = refrigerante_obj.find_element(By.TAG_NAME, 'a').text
    refrigerante = refrigerante_model(descricao, foto)
    refrigerantes_model.append({'Descrição': refrigerante.descricao, 'Foto': refrigerante.foto})  # Organizando em dicionários

driver.quit()

df = pd.DataFrame(refrigerantes_model)
df = df[column_order]
df.to_csv('refrigerantes.csv', index=False)
