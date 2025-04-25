import pygetwindow as gw
import pyautogui
import time
import threading
import os
import sys


# Funções utilitárias
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def clicar_na_imagem(imagem_caminho, offset_y=0, region=None):
    try:
        localizacao_imagem = pyautogui.locateOnScreen(
            imagem_caminho, confidence=0.9, region=region
        )
        if localizacao_imagem:
            x, y = pyautogui.center(localizacao_imagem)
            pyautogui.click(x, y + offset_y)
            print(f"Cliquei na imagem: {imagem_caminho}")
        else:
            print(f"Imagem não encontrada: {imagem_caminho}")
    except pyautogui.PyAutoGUIException:
        print(f"Erro ao tentar clicar na imagem: {imagem_caminho}")


def clicar_na_imagem_2(imagem_caminho, offset_y=0, region=None):
    try:
        localizacao_imagem = pyautogui.locateOnScreen(
            imagem_caminho, confidence=0.9, region=region
        )
        if localizacao_imagem:
            x, y = pyautogui.center(localizacao_imagem)
            pyautogui.click(x, y + offset_y, button="right")
            print(f"Cliquei na imagem: {imagem_caminho}")
        else:
            print(f"Imagem não encontrada: {imagem_caminho}")
    except pyautogui.PyAutoGUIException:
        print(f"Erro ao tentar clicar na imagem: {imagem_caminho}")


def esperar_por_imagem(imagem_caminho, timeout=10, confidence=0.9, region=None):
    start_time = time.time()
    while True:
        try:
            localizacao_imagem = pyautogui.locateOnScreen(
                imagem_caminho, confidence=confidence, region=region, grayscale=True
            )
            if localizacao_imagem:
                return localizacao_imagem
        except Exception:
            pass

        if time.time() - start_time > timeout:
            return None

        time.sleep(0.5)


# Função que verifica se a imagem aparece na tela
def verificar_imagem_loop(imagem_caminho, region=None, intervalo=5):
    while True:
        try:
            print(f"Verificando se {imagem_caminho} está na tela...")
            resultado = esperar_por_imagem(
                imagem_caminho, confidence=0.5, region=region
            )
            if resultado:
                print(f"Imagem encontrada: {imagem_caminho}")
                clicar_na_imagem(imagem_caminho, region=region)
            else:
                print(f"Imagem não encontrada: {imagem_caminho}")
            time.sleep(intervalo)  # Aguarda um tempo antes de verificar novamente
        except Exception as e:
            print(f"Erro no loop de verificação de imagem: {e}")
