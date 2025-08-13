import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    """Classe base para clientes do banco."""

    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        """Executa uma transação na conta do cliente."""
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        """Adiciona uma conta à lista de contas do cliente."""
        self.contas.append(conta)


class PessoaFisica(Cliente):
    """Classe para clientes pessoa física."""

    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    """Classe base para contas bancárias."""

    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        """Método de classe para criar uma nova conta."""
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        """Realiza saque na conta."""
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")

        elif valor > 0:
            self._saldo -= valor
            print(f"\n=== Saque de R$ {valor:.2f} realizado com sucesso! ===")
            return True

        else:
            print("\nOperação falhou! O valor informado é inválido.")

        return False

    def depositar(self, valor):
        """Realiza depósito na conta."""
        if valor > 0:
            self._saldo += valor
            print(f"\n=== Depósito de R$ {valor:.2f} realizado com sucesso! ===")
            return True
        else:
            print("\nOperação falhou! O valor informado é inválido.")
            return False


class ContaCorrente(Conta):
    """Classe para contas correntes com limite e limite de saques."""

    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, cliente, numero, limite=500, limite_saques=3):
        """Método de classe para criar uma nova conta corrente."""
        return cls(numero, cliente, limite, limite_saques)

    def sacar(self, valor):
        """Realiza saque com verificação de limite."""
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes
             if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print(f"\nOperação falhou! O valor do saque excede o limite de R$ {self._limite:.2f}.")

        elif excedeu_saques:
            print(f"\nOperação falhou! Número máximo de saques diários ({self._limite_saques}) excedido.")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    """Classe para gerenciar o histórico de transações."""

    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        """Adiciona uma transação ao histórico."""
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            }
        )


class Transacao(ABC):
    """Classe abstrata para transações."""

    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    """Classe para transações de saque."""

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        """Registra o saque na conta."""
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    """Classe para transações de depósito."""

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        """Registra o depósito na conta."""
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def menu():
    """Exibe o menu principal do sistema."""
    menu_texto = """\n
================ MENU ================
[1]\tDepositar
[2]\tSacar
[3]\tVisualizar Extrato
[4]\tNova Conta
[5]\tNovo Cliente
[6]\tListar Contas
[7]\tListar Clientes
[0]\tSair
=> """
    return input(textwrap.dedent(menu_texto))


def filtrar_cliente(cpf, clientes):
    """Filtra cliente por CPF."""
    cpf_numeros = ''.join(filter(str.isdigit, cpf))
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf_numeros]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    """Recupera a conta do cliente."""
    if not cliente.contas:
        print("\nCliente não possui conta!")
        return

    # FIXME: não permite cliente escolher a conta.
    return cliente.contas[0]


def depositar(clientes):
    """Realiza operação de depósito."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    """Realiza operação de saque."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    """Exibe o extrato da conta."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n" + "="*20 + " EXTRATO " + "="*20)
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}: R$ {transacao['valor']:.2f} - {transacao['data']}"

    print(extrato)
    print(f"\nSaldo:\tR$ {conta.saldo:.2f}")
    print("="*48)


def criar_cliente(clientes):
    """Cria um novo cliente."""
    cpf = input("Informe o CPF: ")

    # Filtrar apenas os números do CPF para armazenamento.
    cpf_numeros = ''.join(filter(str.isdigit, cpf))

    # Verificar se foi informado algum número.
    if not cpf_numeros:
        print("\nCPF deve conter pelo menos um número!")
        return

    cliente = filtrar_cliente(cpf_numeros, clientes)

    if cliente:
        print("\nJá existe cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf_numeros, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta, clientes, contas):
    """Cria uma nova conta."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado, fluxo de criação de conta encerrado!")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    """Lista todas as contas."""
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return

    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def listar_clientes(clientes):
    """Lista todos os clientes cadastrados."""
    if not clientes:
        print("\nNenhum cliente cadastrado.")
        return

    for cliente in clientes:
        # Formatação do CPF: XXX.XXX.XXX-XX.
        cpf_formatado = f"{cliente.cpf[:3]}.{cliente.cpf[3:6]}.{cliente.cpf[6:9]}-{cliente.cpf[9:]}"

        # Formatação da data: DD/MM/AAAA.
        data_formatada = cliente.data_nascimento
        if "/" not in data_formatada and len(data_formatada) == 8:
            data_formatada = f"{data_formatada[:2]}/{data_formatada[2:4]}/{data_formatada[4:]}"

        linha = f"""\
            Nome:\t\t{cliente.nome}
            Data Nasc.:\t{data_formatada}
            CPF:\t\t{cpf_formatado}
            Endereço:\t{cliente.endereco}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    """Função principal do sistema bancário POO."""
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            depositar(clientes)

        elif opcao == "2":
            sacar(clientes)

        elif opcao == "3":
            exibir_extrato(clientes)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "5":
            criar_cliente(clientes)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            listar_clientes(clientes)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()