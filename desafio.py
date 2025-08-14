import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime, UTC
import functools
from pathlib import Path

ROOT_PATH = Path(__file__).parent

class ContaIterador:
    """Iterador personalizado para contas do banco."""

    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f"""\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
            """
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1


class Cliente:
    """Classe base para clientes do banco."""

    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        """Executa uma transação na conta do cliente com limite diário."""
        # Verificar limite de 10 transações por dia.
        data_hoje = datetime.now().strftime("%d/%m/%Y")
        transacoes_hoje = list(conta.historico.transacoes_do_dia(data_hoje))

        if len(transacoes_hoje) >= 10:
            print(f"\nOperação falhou! Você excedeu o número de transações permitidas para hoje ({len(transacoes_hoje)}/10).")
            print(f"Tente novamente amanhã.")
            return False

        transacao.registrar(conta)
        return True

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

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: ('{self.nome}', '{self.cpf}')>"


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
    """Classe para contas correntes com limite de saque."""

    def __init__(self, numero, cliente, limite=500):
        super().__init__(numero, cliente)
        self._limite = limite

    @classmethod
    def nova_conta(cls, cliente, numero, limite=500):
        """Método de classe para criar uma nova conta corrente."""
        return cls(numero, cliente, limite)

    def sacar(self, valor):
        """Realiza saque com verificação de limite de valor."""
        excedeu_limite = valor > self._limite

        if excedeu_limite:
            print(f"\nOperação falhou! O valor do saque excede o limite de R$ {self._limite:.2f}.")
            return False
        else:
            return super().sacar(valor)

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

    def gerar_relatorio(self, tipo_transacao=None):
        """Gerador que permite iterar sobre as transações, opcionalmente filtradas por tipo."""
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao

    def transacoes_do_dia(self, data=None):
        """Gerador que retorna transações de um dia específico."""
        if data is None:
            data = datetime.now().strftime("%d/%m/%Y")

        for transacao in self._transacoes:
            if transacao["data"].split()[0] == data:
                yield transacao


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

def log_transacao(func):
    """Decorador que registra data, hora e tipo de transação."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        data_hora = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")
        args_log = []
        for arg in args:
            if hasattr(arg, '__class__') and hasattr(arg, '__dict__'):
                args_log.append(f"<{arg.__class__.__name__}>")
            else:
                args_log.append(str(arg)[:50])

        kwargs_log = {k: (str(v)[:50] if not hasattr(v, '__dict__') else f"<{v.__class__.__name__}>")
                     for k, v in kwargs.items()}

        with open(ROOT_PATH / "log.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(
                f"[{data_hora}] - Função: '{func.__name__}' executada com argumentos {args_log} e {kwargs_log}. "
                f"Retornou: {resultado}\n"
            )
        return resultado
    return wrapper

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
[8]\tRelatório de Transações
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


@log_transacao
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


@log_transacao
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
    """Exibe o extrato da conta com data e hora das transações."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n" + "="*25 + " EXTRATO " + "="*25)
    print(f"Titular: {conta.cliente.nome}")
    print(f"Agência: {conta.agencia} | Conta: {conta.numero}")
    print(f"Data/Hora do extrato: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("-" * 58)

    transacoes = conta.historico.transacoes

    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for i, transacao in enumerate(transacoes, 1):
            tipo_emoji = "📈" if transacao['tipo'] == "Deposito" else "📉"
            print(f"{i:2d}. {tipo_emoji} {transacao['tipo']}: "
                  f"R$ {transacao['valor']:>8.2f} - {transacao['data']}")

    print("-" * 58)
    print(f"Saldo atual: R$ {conta.saldo:>8.2f}")
    print(f"Transações hoje: {len(list(conta.historico.transacoes_do_dia()))}/10")
    print("="*58)


@log_transacao
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


@log_transacao
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
    """Lista todas as contas usando iterador personalizado."""
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return

    print("\n" + "="*60 + " CONTAS CADASTRADAS " + "="*60)

    # Usando o iterador personalizado.
    for dados_conta in ContaIterador(contas):
        print("=" * 100)
        print(textwrap.dedent(dados_conta))


def relatorio_transacoes(clientes):
    """Gera relatório de transações usando gerador."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n" + "="*15 + " OPÇÕES DE RELATÓRIO " + "="*15)
    print("1 - Todas as transações")
    print("2 - Apenas depósitos")
    print("3 - Apenas saques")
    print("4 - Transações do dia")

    opcao = input("Escolha uma opção: ")

    print("\n" + "="*20 + " RELATÓRIO " + "="*20)

    if opcao == "1":
        print("📋 Todas as Transações:")
        for transacao in conta.historico.gerar_relatorio():
            print(f"  • {transacao['tipo']}: R$ {transacao['valor']:.2f} - {transacao['data']}")

    elif opcao == "2":
        print("📈 Apenas Depósitos:")
        for transacao in conta.historico.gerar_relatorio("Deposito"):
            print(f"  • {transacao['tipo']}: R$ {transacao['valor']:.2f} - {transacao['data']}")

    elif opcao == "3":
        print("📉 Apenas Saques:")
        for transacao in conta.historico.gerar_relatorio("Saque"):
            print(f"  • {transacao['tipo']}: R$ {transacao['valor']:.2f} - {transacao['data']}")

    elif opcao == "4":
        data = input("Informe a data (dd/mm/aaaa) ou deixe em branco para hoje: ").strip()
        if not data:
            data = None
        print(f"📅 Transações do dia {data or 'hoje'}:")
        for transacao in conta.historico.transacoes_do_dia(data):
            print(f"  • {transacao['tipo']}: R$ {transacao['valor']:.2f} - {transacao['data']}")

    else:
        print("Opção inválida!")
        return

    print("="*48)


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

        elif opcao == "8":
            relatorio_transacoes(clientes)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()