from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:

    # Abre o navegador
    navegador = p.chromium.launch(
        headless=False
    )

    # Cria uma nova página
    pagina = navegador.new_page()

    # Acessa o Portal Fake
    pagina.goto(
        "file:///D:/para%20portal%20fake/HO7/portal_fake/index.html"
    )

    # Aguarda a página carregar
    pagina.wait_for_timeout(2000)

    # Localiza o botão pelo ID e clica
    pagina.locator("#btnNovo").click()

    # Aguarda a tela de cadastro abrir
    pagina.wait_for_timeout(3000)

    # Fecha o navegador
    navegador.close()