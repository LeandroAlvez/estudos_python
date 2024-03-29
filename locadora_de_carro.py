import os
lista_portifolio = {
    'Chevrolet Tracker': 120,
    'Chevrolet Onix': 90,
    'Chevrolet Spin': 150,
    'Hyundai HB20': 85,
    'Hyundai Tucson': 120,
    'Fiat Uno': 60,
    'Fiat Mobi': 70,
    'Fiat Pulse': 130
}

lista_carros_alugados = {}

def menu_portifolio():
    indice = 0
    for carro, valor in lista_portifolio.items():
        print("[{}] {} - R${}/dia".format(indice, carro, valor))
        indice += 1

def carros_alugados():
    indice = 0
    for carro in lista_carros_alugados.keys():
        print("[{}] {}".format(indice, carro))
        indice += 1

def menu_homepage():
    print("="*40)
    print("Bem vindo à locadora de carros:")
    print("="*40)
    print("O que deseja fazer? ")
    print("0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro")
    selecao = int(input())
    return selecao

def selecao_menu():
    print("="*20)
    print("0 - continuar | 1 - Sair")
    print()
    selecao = int(input())
    return selecao

def selecao_menu_interno():
    print("="*20)
    print("0 - ir para o menu principal | 1 - Encerrar programa")
    print()
    selecao = int(input())
    return selecao

def buscar_carro(codigo_carro):
    carro = list(lista_portifolio)[codigo_carro]
    return(carro)

def valor_aluguel(codigo_carro, qtd_dias):
    preco_diaria = list(lista_portifolio.values())[codigo_carro] * qtd_dias
    return preco_diaria

def alugar_carro(codigo_carro, qtd_dias):
    carro = buscar_carro(codigo_carro)
    valor = valor_aluguel(codigo_carro, qtd_dias)
    return{"carro": carro, "valor": valor}

def devolver_carro(codigo_carro):
    carro = list(lista_carros_alugados)[codigo_carro]
    devolucao_carro = list(lista_carros_alugados.values())[codigo_carro]
    lista_carros_alugados.pop(carro)
    lista_portifolio[carro] = devolucao_carro
    print("Obrigado por devolver o carro {}".format(carro))
    return carro
    
    
while True:
    selecao_menu_principal = menu_homepage()
    if selecao_menu_principal == 0:
        os.system("cls")
        menu_portifolio()
        selecao_menu()
        selecao = selecao_menu
        if selecao == 0:
            os.system("cls")
        else:
            print()
    elif selecao_menu_principal == 1:
        os.system("cls")
        print ("[ALUGAR CARRO]  Dê uma olhada em nosso portifóilio.")
        print()
        menu_portifolio()
        print("Escolha o código do carro a alugar: ")
        codigo_carro = int(input())
        print("Por quantos dias deseja ficar com o carro: ")
        qtd_dias = int(input())
        aluguel = alugar_carro(codigo_carro, qtd_dias)
        os.system("cls")
        print("Você escolheu {} por {} dias.".format(aluguel.get("carro"), qtd_dias))
        print("O valor total do aluguel do {} por {} dias é R${:,.2f}. Deseja alugar o carro?".format(aluguel.get("carro"), qtd_dias, aluguel.get("valor")))
        print("0 - SIM | 1 - NÃO ")
        decisao_alugar = int(input())
        if decisao_alugar == 0:
            lista_carros_alugados[aluguel.get("carro")] = aluguel.get("valor")
            lista_portifolio.pop(aluguel.get("carro"))
            print("Parabéns você alugou o {} por {} dias.".format(aluguel.get("carro"), qtd_dias))
            print()
            print("="*20)
            selecao = selecao_menu_interno()
            if selecao == 0:
                 os.system("cls")
                 continue
            else:
             print("Obrigado por alugar o carro conosco, agradeçemos a preferência!")
            break
        else: 
            selecao = selecao_menu_interno()
            if selecao == 0:
                 os.system("cls")
                 menu_portifolio()
            else:
             print("Obrigado por alugar o carro conosco, agradeçemos a preferência!")
            continue
    else:
        selecao_menu_principal == 2
        os.system("cls")
        print("Segue a lista de carros alugados. Qual veículo vc deseja devolver? ")
        print()
        print("Lista de carros [ALUGADOS]")
        carros_alugados()
        print("-"*20)
        print("Digite o código do carro a ser devolvido: ")
        codigo_carro = int(input())
        print()
        carro_devolvido = devolver_carro(codigo_carro)
        print()
        selecao = selecao_menu_interno()
        if selecao == 0:
            os.system("cls")
            continue
        else:
             print("Obrigado por alugar o carro conosco, agradeçemos a preferência!")
        break



