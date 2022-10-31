from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

#Primeiro setamos o driver e passamos como parametro nosso chrome driver
#Que nesse caso se instala automaticamente
driver = webdriver.Chrome(ChromeDriverManager().install())

#Depois entramos no link desejado
driver.get("https://www.climatempo.com.br/")

#É importante dar um sleep de alguns segundos para o navegador carregar o conteúdo
time.sleep(5)

#Pegamos o tempo
tempo = driver.find_element(By.ID, "current-weather-temperature")

print(f"Hoje o tempo é de {tempo.text} graus")