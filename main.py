# instalar biblioteca request ---- pip install request

# integração com Database (REST API)
import requests
import json

# ---------------------------------- LINK DE CONEXÃO COM BD ------------------------------------------------------

link = 'https://fluxodecaixapython-default-rtdb.firebaseio.com/'

desligar = 1
while desligar == 1:

    # ---------------------------------- CRIAR MENU ------------------------------------------------------------------
    print()
    print('~' * 20, 'Menu', '~' * 20)
    print()
    print('Selecione o que deseja fazer:')
    print('1 - Lançar uma Venda')
    print('2 - Editar Venda')
    print('3 - Consultar Venda')
    print('4 - Deletar Venda')

    operacao = int(input('Operação a ser realizada: '))

    # ---------------------------------- CRIAR VENDA ----------------------------------------------------------------
    # Criar Venda (POST)
    if operacao == 1:

        print()
        print()
        print('LANÇAMENTO DE VENDA')
        print()

        # Criar biblioteca com dados da venda
        venda = {}

        venda['cliente'] = str(input('Nome do cliente: '))
        venda['produto'] = str(input('Nome do produto: '))
        venda['preco'] = float(input('Preço do produto: '))
        venda['quantidade'] = int(input('Quantidade: '))
        venda['total'] = venda['preco'] * venda['quantidade']

        requisicao = requests.post(f'{link}/vendas/.json', data=json.dumps(venda))
        print()
        print('Deseja realizar mais alguma operação? ')
        desligar = int(input('Se sim digite 1, se não digite 2: '))
        if desligar == 2:
            break

    # ---------------------------------- EDITAR VENDA --------------------------------------------------------------
    elif operacao == 2:

        print()
        print()
        print('EDIÇÃO DE VENDA')
        print()
        requisicao = requests.get(f'{link}/vendas/.json')
        dic_requisicao = requisicao.json()

        for id_venda in dic_requisicao:
            # print(id_venda)
            id_vendas = requests.get(f'{link}/vendas/{id_venda}/.json')
            dadosvenda = id_vendas.json()
            print('Id da venda:', id_venda)
            print('Cliente:', dadosvenda['cliente'])
            print('produto:', dadosvenda['produto'])
            print('preço: R$', dadosvenda['preco'])
            print('Quantidade:', dadosvenda['quantidade'])
            print('valor total: R$', dadosvenda['total'])
            print()

        altvenda = input('Qual venda deseja alterar? Favor digitar id: ')
        venda = {}
        print()
        print('O que deseja alterar?')
        print('1 - nome do cliente')
        print('2 - produto vendido')
        print('3 - preco do produto')
        print('4 - quantidade de produtos')
        print('Digite a opção abaixo')
        escalt = int(input())
        cancel = 1
        while cancel != 2:
            if escalt == 1:
                venda['cliente'] = str(input('Nome do cliente: '))
                requisicao = requests.patch(f'{link}/vendas/{altvenda}/.json', data=json.dumps(venda))
                cancel = 2
            elif escalt == 2:
                venda['produto'] = str(input('Nome do produto: '))
                requisicao = requests.patch(f'{link}/vendas/{altvenda}/.json', data=json.dumps(venda))
                cancel = 2
            elif escalt == 3:
                venda['preco'] = float(input('Preço do produto: '))
                requisicao = requests.patch(f'{link}/vendas/{altvenda}/.json', data=json.dumps(venda))
                cancel = 2
            elif escalt == 4:
                venda['quantidade'] = int(input('Quantidade: '))
                requisicao = requests.patch(f'{link}/vendas/{altvenda}/.json', data=json.dumps(venda))
                cancel = 2


    # -------------------------------- CONSULTAR VENDAS ---------------------------------------------------

    elif operacao == 3:
        print()
        print()
        print('CONSULTAR VENDAS')
        print()
        requisicao = requests.get(f'{link}/vendas/.json')
        dic_requisicao = requisicao.json()

        for id_venda in dic_requisicao:
            id_vendas = requests.get(f'{link}/vendas/{id_venda}/.json')
            dadosvenda = id_vendas.json()
            print('ID da Venda:', id_venda)
            print('Cliente:', dadosvenda['cliente'])
            print('produto:', dadosvenda['produto'])
            print('preço: R$', dadosvenda['preco'])
            print('Quantidade:', dadosvenda['quantidade'])
            print('valor total: R$', dadosvenda['total'])
            print()

        # -------------------------------- DELETAR VENDAS ---------------------------------------------------
    elif operacao == 4:
        print()
        print()
        print('DELETAR VENDA')
        print()
        requisicao = requests.get(f'{link}/vendas/.json')
        dic_requisicao = requisicao.json()

        for id_venda in dic_requisicao:
            id_vendas = requests.get(f'{link}/vendas/{id_venda}/.json')
            dadosvenda = id_vendas.json()
            print('Id da venda:', id_venda)
            print('Cliente:', dadosvenda['cliente'])
            print('produto:', dadosvenda['produto'])
            print('preço:', dadosvenda['preco'])
            print('Quantidade:', dadosvenda['quantidade'])
            print('valor total: R$', dadosvenda['total'])
            print()

        id_del_venda = input('Digite o ID da venda que deseja deletar: ')
        requisicao = requests.delete(f'{link}/vendas/{id_del_venda}/.json')
        print('operação concluída!')

    else:
        print('Opção escolhida é inválida!')
    print()
    print('Deseja realizar mais alguma operação? ')
    desligar = int(input('Se sim digite 1, se não digite 2: '))
