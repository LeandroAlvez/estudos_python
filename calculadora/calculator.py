import os

print("================")
opcoes = {
    "+": "Soma",
    "-": "Subtração",
    "*": "Multiplicação",
    "/": "Divisão",
    "^": "Exponeciação"
}
while True:
    os.system('cls')
    i = 0
    for op, name in opcoes.items():
        print(i, ":", name)
        i += 1
    print()
    print("Escola uma operação: ")
    op = int(input())
    op_signal = list(opcoes.keys()) [op]

    print()
    print("A operação '{}' foi a escolhida.".format(op_signal))
    print("Digite o primeiro valor: ")
    v1 = int(input())
    print("Digite o outro valor: ")
    v2 = int(input())

    if op == 0:
        calc = v1 + v2
    elif op == 1:
        calc = v1 - v2
    elif op == 2:
        calc = v1 * v2
    elif op == 3:
        calc = v1 / v2
    elif op == 4:
        calc = v1 ** v2


    print()
    print("{} {} {} = {:,.2f}".format(v1, op_signal, v2, calc))
    print()
    print("=======================")

    print("Deseja fazer mais alguma operação, digite (s/n): ")
    interacao = input()
    if interacao.lower() != "s":
        break
    print("Obrigado por usar a calculadora do Leandro_team!")