from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializa o navegador Chrome
driver = webdriver.Chrome()

# Maximiza a janela (opcional)
driver.maximize_window()

# Acessa o Portal Fake
driver.get("file:///D:/para%20portal%20fake/HO7/portal_fake/index.html")

# Aguarda a página carregar
time.sleep(2)

# Localiza o botão pelo ID e clica
driver.find_element(By.ID, "btnNovo").click()

# Aguarda a tela de cadastro abrir
time.sleep(3)

# Fecha o navegador
driver.quit()