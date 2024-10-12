menu = """

[c] Criar Conta
[e] Entrar
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

nome = ""
senha = ""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "c":
       
        nome = input("Digite o seu nome:")

        if nome == " ":
            print("Nome inválido")
            
        else:
            senha = input("Digite a sua senha:")
            if senha == " ":
                print("Senha inválida")

            else:
                print ("Conta criada com sucesso!")
    
    elif opcao == "e":

            nome1 = input("Digite o seu nome:")

            if nome1 == nome:
                senha1 = input("Digite a sua senha:")

                if senha1 == senha:
                    print("\nBem vindo, você está logado!")

                else:
                    print("Senha inválida")
                        
            else:
                print("Não existem registros com este nome!")

    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
