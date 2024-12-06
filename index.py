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
            if num_2 != 0:
                print(f"Resultado: {num_1/num_2}")
            else:
                print("Erro: Divisão por zero!")
        else:
            print("Erro: Operação inválida!")
    except ValueError:
        print("Erro: Entrada inválida!")
calculadora()