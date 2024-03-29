import os
import time

carros_disponiveis = [
    ("Chevrolet Tracker", 120), 
    ("Chevrolet Onix", 90), 
    ("Chevrolet Spin", 150), 
    ("Hyundai HB20", 85), 
    ("Hyundai Tucson", 120),
    ("Fiat Uno", 60), 
    ("Fiat Mobi", 70), 
    ("Fiat Pulse", 130)
]

carros_alugados = []
## função menu interno para navegação entre encerrar o programa e voltar para pagina inicial do sistema
def menu_interno():
    print("="*40)
    print("="*40)
    print("0 - Ir para Homepage | 1 - Encerrar programa")
    print()
    selecao = int(input())
    return selecao

def homepage():
    print("="*40)
    print("Bem vindo a locadora de carros online!")
    print("="*40)
    print("O que deseja fazer?")
    print("0 - Mostrar portifólio | 1 - Alugar carro | 2 - Devolver carro")
    selecao_menu_principal = int(input())
    return selecao_menu_principal

def mostrar_carros(carros_disponiveis):
    for i, carros in enumerate(carros_disponiveis):
        print(f"{[i]} {carros[0]} - R${carros[1]:.2f} / dia.")

while True:
    selecao = homepage()
    if selecao == 0:
        os.system("cls")
        mostrar_carros(carros_disponiveis)
        selecao = menu_interno()
        if selecao == 0:
            os.system("cls")
            continue
        else:
            print("Você acabou de usar os sistema locadora de carros online!")
            break
    elif selecao == 1:
            os.system("cls")
            print("="*40)
            print("[ALUGAR] Aqui está a lista de carros disponíveis.")
            print("="*40)
            mostrar_carros(carros_disponiveis)
            print()
            print("="*40)
            print("Deseja alugar algum veículo? Digite 0 - SIM | 1 - Voltar a HOMEPAGE")
            confirmacao_alugar = int(input())
            if confirmacao_alugar == 0:
                print("Digite o código do carro que deseja alugar:")
                codigo_carro = int(input())
                print("Por quantos dias deseja ficar com o carro?")
                qtd_dias = int(input())
                os.system("cls")
                print(f"Você escolheu o {carros_disponiveis[codigo_carro][0]} por {qtd_dias}.")
                print("O valor é de R${:.2f}. Deseja alugar?".format(carros_disponiveis[codigo_carro][1] * qtd_dias))
                print("0 - SIM | 1 - NÃO")
                selecao = int(input())
                if selecao == 0:
                    os.system("cls")
                    print("Aguarde enquanto realizamos a reserva do seu veículo...")
                    print("="*40)
                    time.sleep(0.5)
                    print("3..")
                    time.sleep(1.2)
                    print("2..")
                    time.sleep(1.2)
                    print("1..")
                    time.sleep(1.2)
                    os.system("cls")
                    print("Parabéns você alugou o {} por {} dias.".format(carros_disponiveis[codigo_carro][0], qtd_dias))
                    carros_alugados.append(carros_disponiveis.pop(codigo_carro))
                    print("="*40)
                    print("Oque você deseja fazer agora?")
                    print("0 - Ir para HOMEPAGE | 1 - Encerrar Programa")
                    selecao = int(input())
                    if selecao == 0:
                        os.system("cls")
                        continue
                    else:
                        print("Você acabou de usar os sistema locadora de carros online!")
                    break
            else:
                os.system("cls")
                continue    
    elif selecao == 2:
        if len(carros_alugados) == 0:
            os.system("cls")
            print("No momento não temos nenhum veículo alugado")
            print("-"*40)
            print(input("Aperte ENTER para voltar a HOMEPAGE... "))
            os.system("cls")
            continue
        else:    
            os.system("cls")
            print("="*40)
            print("[Devolução] Aqui está a lista de carros alugados.")
            print("="*40)
            mostrar_carros(carros_alugados)
            print("Deseja realizar a devolução de algum veículo? 0 - SIM | 1 - NÂO" )
            selecao = int(input())
            if selecao == 0:
                 print("Digite o código do veículo a ser devolvido:")
                 codigo_carro = int(input())
                 print(input("Aperte ENTER para confirmar..."))
                 os.system("cls")
                 print("Realizando a devolução, aguarde!")
                 print("="*40)
                 time.sleep(0.5)
                 print("3...")
                 time.sleep(1.2)
                 print("2...")
                 time.sleep(1.2)
                 print("1...")
                 time.sleep(1.2)
                 os.system("cls")
                 print("O veículo {} foi devolvido com sucesso!".format(carros_alugados[codigo_carro][0]))
                 carros_disponiveis.append(carros_alugados.pop(codigo_carro))
                 print()
                 print ("Oque você deseja fazer agora?")
                 print("0 - Ir para HOMEPAGE | 1 - Encerrar programa")
                 selecao = int(input())
                 if selecao == 0:
                    os.system("cls")
                    continue
                 else:
                    print("Você acabou de usar os sistema locadora de carros online!")
                 break
            else:
                os.system("cls")
                continue