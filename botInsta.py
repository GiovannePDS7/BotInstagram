from playwright.sync_api import sync_playwright
import pyautogui
import time

with sync_playwright() as p:
    # Abre o Instagram no navegador
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.instagram.com/')
    page.locator('//*[@id="loginForm"]/div/div[1]/div/label/input').click()
    page.keyboard.type("*SEU LOGIN*")  # Seu login
    page.keyboard.press("Tab")
    page.keyboard.type("*SUA SENHA*")  # Sua senha
    page.keyboard.press("Enter")
    time.sleep(5)
    
    page.goto("*URL DA PUB*") # link da pub em que o programa ira rodar
    time.sleep(3)
# Interage com as postagens

    page.get_by_role("img", name='Curtir').first.click()

    i = 1
    while i <= 5:  # Loop de comentarios Ex. aqui ele ira comentar 5 vezes
        page.get_by_placeholder("Adicione um comentário...").click()
        page.keyboard.type("*COMENTARIO*")  # comentario desejado
        page.keyboard.press("Enter")
        i = i + 1
    time.sleep(20000) # Mantem o programa aberto até 20000 segundos

# Fecha o navegador
browser.close()
