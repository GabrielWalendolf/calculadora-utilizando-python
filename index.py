"""
Requisitos:

    Aceitar dois números e uma operação (+, -, *, /).
    Exibir o resultado da operação ou uma mensagem de erro.

Passos:

    Solicite ao usuário dois números e uma operação.
    Use condicionais para realizar a operação.
    Valide divisões por zero.
"""

def calculadora():
    try:
        num_1 = int(input("digite o primeiro número: "))
        operacao = str(input("digite uma operação (+, -, *, /): "))
        num_2 = int(input("digite o segundo número: "))
        if operacao == '+':
            print(f"resultado: {num_1+num_2}")
        elif operacao == '-':
            print(f"resultado: {num_1-num_2}")
        elif operacao == '*':
            print(f"resultado: {num_1*num_2}")
        elif operacao == '/':
            print(f"Resultado: {num_1/num_2}")
        else:
            print("Erro: Operação inválida!")
    except ValueError:
        print("Erro: Entrada inválida!")
calculadora()