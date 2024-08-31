
DEPOSITOS = ''
SAQUES = ""
SAQUES_DISPONIVEIS = 3
SALDO = 500.0
MENU = """
        MENU
----------------------        
[A] SAQUE
[B] DEPOSITO
[C] EXTRATO
[D] SAIR
----------------------  
"""

while True:

    escolha = input(MENU)
    escolha = escolha.lower()

    if escolha == "a":
        VALOR_SAQUE = input("Favor informe o valor do seu saque: ")
        VALOR_SAQUE = float(VALOR_SAQUE)
        if VALOR_SAQUE <= SALDO:
            if (VALOR_SAQUE > 0):
                if (SAQUES_DISPONIVEIS > 0):
                    SAQUES = SAQUES +"R$" + str(VALOR_SAQUE) + " "
                    SALDO -= VALOR_SAQUE
                    SAQUES_DISPONIVEIS -= 1
                    print(f'Você possui {SAQUES_DISPONIVEIS} saques disponiveis')
                    print(SALDO)
                else:
                    print('Você atingiu o limite de saques disponiveis')
            else:
                print('Você só pode sacar valores positivos')
        else:
            print(f'Você não possui saldo suficiente para está operação, saldo atual R${SALDO}')

    elif escolha == "b":
        VALOR_DEPOSITO = float(input("Favor informar o valor do deposito"))
        if VALOR_DEPOSITO > 0:
            DEPOSITOS = DEPOSITOS +"R$" + str(VALOR_DEPOSITO) + " "
            SALDO += VALOR_DEPOSITO
            print(f'Saldo atual: R${SALDO}')
        else:
            print('Favor inserir um valor válido')
    elif escolha == "c":
        print(f'Saques realizados: {SAQUES}')
        print(f'Depositos realizados: {DEPOSITOS}')        

    elif escolha == "d":
        break
    else:
        print('Operação invalida, por favor seleciona uma opção valida do menu')