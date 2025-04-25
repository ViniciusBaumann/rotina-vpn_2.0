import tkinter as tk


class ContadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador de Execuções")
        self.root.geometry("300x100")
        self.contador = 0

        # Label para exibir o contador
        self.label_contador = tk.Label(
            root, text=f"Contador: {self.contador}", font=("Helvetica", 14)
        )
        self.label_contador.pack(pady=10)

        # Label para exibir a mensagem atual
        self.label_mensagem = tk.Label(
            root, text="Pronto para iniciar...", font=("Helvetica", 10)
        )
        self.label_mensagem.pack(pady=10)

    def atualizar_contador(self, novo_valor=0):
        self.contador = novo_valor
        self.label_contador.config(text=f"Contador: {self.contador}")
        self.root.update()

    # Função para atualizar a mensagem atual
    def atualizar_mensagem(self, mensagem):
        self.label_mensagem.config(text=mensagem)
        self.root.update()


# Função para iniciar a interface
def iniciar_interface():
    root = tk.Tk()
    app = ContadorApp(root)
    return app, root
