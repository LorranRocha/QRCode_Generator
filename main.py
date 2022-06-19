#   Python Version 3.10.5
#   Author: Lorran Rocha https://www.lorranrocha.com/

# pip install qrcode
# pip install pillow

import qrcode
import os

def criarQr():
    try:
        os.system('clear')
    finally:
        os.system('cls')
        
    # Link para website
    dados = str(input("Digite o link para o seu website: "))

    # Cria o qrcode
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
        )

    qr.add_data(dados)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    try:
        os.system('clear')
    finally:
        os.system('cls')

    img.save('codigoqr.png')

    print('Código QR gerado com sucesso!!!')

    opcao = int(input("Deseja gerar outro código?\n\n1 - Sim\n2 - Não: "))
    if opcao == 1:
        criarQr()
    else:
        print('Saindo...')
        exit()

    
criarQr()