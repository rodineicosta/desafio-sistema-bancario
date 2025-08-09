def depositar(saldo, extrato):
    """Realiza operação de depósito"""
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def sacar(saldo, extrato, numero_saques, limite, limite_saques):
    """Realiza operação de saque"""
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
    elif excedeu_saques:
        print(f"Operação falhou! Número máximo de saques diários ({limite_saques}) excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    """Exibe o extrato da conta"""
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")


def main():
    """Função principal do sistema bancário"""
    menu = """
================ SISTEMA BANCÁRIO ================

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu)

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "2":
            saldo, extrato, numero_saques = sacar(
                saldo, extrato, numero_saques, limite, LIMITE_SAQUES
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato)

        elif opcao == "0":
            print("Obrigado por usar nosso sistema bancário!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()