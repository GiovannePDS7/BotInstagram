from playwright.sync_api import sync_playwright
import pyautogui
import time

with sync_playwright() as p:
    # Abre o Instagram no navegador
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.instagram.com/')
    page.locator('//*[@id="loginForm"]/div/div[1]/div/label/input').click()
    page.keyboard.type("SEU USUARIO") #seu login
    page.keyboard.press("Tab")
    page.keyboard.type("SUA SENHA") #sua senha
    page.keyboard.press("Enter")
    time.sleep(5)
    page.goto('https://www.instagram.com/p/Cq_jIQLss7-/')
    time.sleep(2)
# Interage com as postagens

    page.get_by_role("img", name='Curtir').click()

    i = 1
    while i <= 5: # loop de comentarios
        page.get_by_placeholder("Adicione um comentário...").click()
        page.keyboard.type(f"comentário: {i}") # comentario desejado
        page.keyboard.press("Enter")
        i = i + 1

    time.sleep(20000)

# Fecha o navegador
