# Rotina VPN 2.0

Este é um script de automação em Python para gerenciar conexões VPN. O script monitora e gerencia automaticamente o status da conexão VPN, realizando reconexões quando necessário.

## Funcionalidades

- Monitoramento automático do status da VPN
- Interface gráfica para acompanhamento
- Reconexão automática quando necessário
- Contador de reconexões realizadas

## Requisitos

- Python 3.x
- PyAutoGUI
- Tkinter (geralmente vem com Python)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/ViniciusBaumann/rotina-vpn_2.0.git
cd rotina-vpn_2.0
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como usar

Execute o script principal:
```bash
python main.py
```

O programa iniciará com uma interface gráfica mostrando o status atual da automação.

## Estrutura do Projeto

- `main.py`: Script principal com a lógica de automação
- `interface.py`: Implementação da interface gráfica
- `utils.py`: Funções utilitárias
- `imgs/`: Diretório contendo as imagens necessárias para a automação

## Contribuição

Sinta-se à vontade para contribuir com o projeto através de Pull Requests ou reportando issues.
