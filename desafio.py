import textwrap


def depositar(saldo, valor, extrato, /):
    """
    Realiza operação de depósito.

    Args:
        saldo (float): Saldo atual da conta (positional only)
        valor (float): Valor a ser depositado (positional only)
        extrato (str): Histórico de transações (positional only)

    Returns:
        tuple: (novo_saldo, novo_extrato)
    """
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t\tR$ {valor:.2f}\n"
        print(f"\n=== Depósito de R$ {valor:.2f} realizado com sucesso! ===")
    else:
        print("\n Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza operação de saque.

    Args:
        saldo (float): Saldo atual da conta (keyword only)
        valor (float): Valor a ser sacado (keyword only)
        extrato (str): Histórico de transações (keyword only)
        limite (float): Limite por saque (keyword only)
        numero_saques (int): Número de saques realizados (keyword only)
        limite_saques (int): Limite diário de saques (keyword only)

    Returns:
        tuple: (novo_saldo, novo_extrato)
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print(f"\n Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")

    elif excedeu_saques:
        print(f"\n Operação falhou! Número máximo de saques diários ({limite_saques}) excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t\tR$ {valor:.2f}\n"
        print(f"\n=== Saque de R$ {valor:.2f} realizado com sucesso! ===")

    else:
        print("\n Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    """
    Exibe o extrato da conta.

    Args:
        saldo (float): Saldo atual da conta (positional only)
        extrato (str): Histórico de transações (keyword only)
    """
    print("\n" + "="*30 + " EXTRATO " + "="*30)
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\t\tR$ {saldo:.2f}")
    print("="*68)


def criar_usuario(usuarios):
    """
    Cria um novo usuário no sistema.

    Args:
        usuarios (list): Lista de usuários cadastrados

    Returns:
        None
    """
    cpf = input("Informe o CPF: ")

    # Filtrar apenas os números do CPF para armazenamento
    cpf_numeros = ''.join(filter(str.isdigit, cpf))

    # Verificar se foi informado algum número
    if not cpf_numeros:
        print("\n CPF deve conter pelo menos um número!")
        return

    usuario = filtrar_usuario(cpf_numeros, usuarios)

    if usuario:
        print("\n Já existe cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf_numeros, "endereco": endereco})

    print("=== Cliente cadastrado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    """
    Filtra e retorna um usuário pelo CPF.

    Args:
        cpf (str): CPF do usuário (pode conter caracteres especiais)
        usuarios (list): Lista de usuários

    Returns:
        dict or None: Usuário encontrado ou None
    """
    # Filtrar apenas os números do CPF para busca
    cpf_numeros = ''.join(filter(str.isdigit, cpf))

    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf_numeros]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    """
    Cria uma nova conta corrente.

    Args:
        agencia (str): Número da agência
        numero_conta (int): Número da conta
        usuarios (list): Lista de usuários

    Returns:
        dict or None: Nova conta criada ou None
    """
    cpf = input("Informe o CPF do cliente: ")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Cliente não encontrado, fluxo de criação de conta corrente encerrado!")


def listar_contas(contas):
    """
    Lista todas as contas cadastradas.

    Args:
        contas (list): Lista de contas
    """
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def listar_usuarios(usuarios):
    """
    Lista todos os usuários cadastrados.

    Args:
        usuarios (list): Lista de usuários
    """
    for usuario in usuarios:
        linha = f"""\
            Nome:\t\t{usuario['nome']}
            Data Nasc.:\t{usuario['data_nascimento']}
            CPF:\t\t{usuario['cpf']}
            Endereço:\t{usuario['endereco']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def menu():
    """
    Exibe o menu principal do sistema.

    Returns:
        str: Menu formatado
    """
    menu_texto = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tVisualizar Extrato
    [4]\tNova Conta Corrente
    [5]\tNovo Cliente
    [6]\tListar Contas Correntes
    [7]\tListar Clientes
    [0]\tSair
    => """
    return textwrap.dedent(menu_texto)


def main():
    """Função principal do sistema bancário"""
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = input(menu())

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo_anterior = saldo
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            # Incrementa numero_saques apenas se o saque foi bem-sucedido
            if saldo < saldo_anterior:  # Saldo diminuiu, logo saque foi realizado
                numero_saques += 1

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            criar_usuario(usuarios)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            listar_usuarios(usuarios)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()