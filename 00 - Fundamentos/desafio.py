menu = """

[0] Depositar
[1] Sacar 
[2] Extrato
[3] Sair

Informe a operação => """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: 
    operaçao = input (menu)
    if operaçao == "0": 
        valor = float(input("Informe o valor do depósito:"))
        if valor > 0: 
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Valor depositado!")
        else: 
            print("Operação inválida! O valor informado não é permito.")
    elif operaçao == "1": 
        valor = float(input("Informe o valor do saque: "))
        exedeu_saudo = valor > saldo
        exedeu_limite = valor > limite 
        exedeu_saques = numero_saques >= LIMITE_SAQUES
        if exedeu_saudo: 
            print("Operação falhou! Você não tem saldo suficiente.")
        elif exedeu_limite:
            print("Operação falhou! O valor informado é maior que o limite permitido.")
        elif exedeu_saques:
            print("Operação falhou! Você exedeu o número de saques diários.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Valor sacado!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif operaçao == "2": 
        print("\n======== EXTRATO ========")
        print(f"\nSaldo: R$ {saldo:.2f}")
    elif operaçao == "3":
        print("Operação finalizada!")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
