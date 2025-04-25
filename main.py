import pyautogui
import time
import threading
from utils import (
    clicar_na_imagem_2,
    resource_path,
    clicar_na_imagem,
    esperar_por_imagem,
)
from interface import iniciar_interface


def executar_automacao(app):
    contador = 0

    # Obter a resolução da tela
    screen_width, screen_height = pyautogui.size()

    # Definir a região do canto inferior direito (25% da tela)
    region_inferior_direito = (
        screen_width // 2,
        screen_height // 2,
        screen_width // 2,
        screen_height // 2,
    )

    while True:
        try:
            primeira_imagem = resource_path("imgs/vpn-desc.png")
            segunda_imagem = resource_path("imgs/conectar.png")

            app.atualizar_mensagem("Verificando.")
            time.sleep(0.4)
            app.atualizar_mensagem("Verificando..")
            time.sleep(0.4)
            app.atualizar_mensagem("Verificando...")

            resultado_primeira_imagem = esperar_por_imagem(
                primeira_imagem, timeout=15, region=region_inferior_direito
            )

            if resultado_primeira_imagem:
                app.atualizar_mensagem("Resetando.")
                time.sleep(0.2)
                app.atualizar_mensagem("Resetando..")
                time.sleep(0.2)
                app.atualizar_mensagem("Resetando...")
                clicar_na_imagem_2(primeira_imagem, region=region_inferior_direito)

                # Após clicar na primeira imagem, esperar alguns segundos para o programa carregar
                time.sleep(3)

                app.atualizar_mensagem("Procurando botão *Conectar*")
                resultado_segunda_imagem = esperar_por_imagem(
                    segunda_imagem, timeout=15
                )

                if resultado_segunda_imagem:
                    app.atualizar_mensagem("Resetando...")
                    clicar_na_imagem(segunda_imagem)

                    # Incrementar o contador
                    contador += 1
                    app.atualizar_mensagem(
                        f"Script rodou com sucesso {contador} vez(es)."
                    )
                    app.atualizar_contador(contador)

                else:
                    app.atualizar_mensagem("Imagem de conectar não encontrada.")
            else:
                app.atualizar_mensagem("Verificando.")

            # Pequena pausa antes de tentar novamente
            time.sleep(60)

        except Exception as e:
            app.atualizar_mensagem(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    # Iniciar a interface gráfica
    app, root = iniciar_interface()

    # Iniciar a automação em um thread separado
    automacao_thread = threading.Thread(target=executar_automacao, args=(app,))
    automacao_thread.daemon = (
        True  # Define como daemon para terminar junto com a interface
    )
    automacao_thread.start()

    # Manter a interface rodando
    root.mainloop()
