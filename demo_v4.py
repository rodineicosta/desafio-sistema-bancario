#!/usr/bin/env python3
"""
Demonstração das Funcionalidades Avançadas v4.0
Decoradores, Geradores e Iteradores
"""
import textwrap

from desafio import (
    PessoaFisica, ContaCorrente, Deposito, Saque,
    ContaIterador, log_transacao
)

def demonstracao_v4():
    """Demonstração das novas funcionalidades v4.0."""
    print("🚀 SISTEMA BANCÁRIO v4.0 - DEMONSTRAÇÃO AVANÇADA")
    print("="*60)

    # Preparando dados de teste.
    cliente1 = PessoaFisica(
        nome="Ana Silva",
        data_nascimento="15/05/1990",
        cpf="11111111111",
        endereco="Rua A, 123 - Centro - São Paulo/SP"
    )

    cliente2 = PessoaFisica(
        nome="Carlos Santos",
        data_nascimento="20/08/1985",
        cpf="22222222222",
        endereco="Av. B, 456 - Vila Nova - Rio de Janeiro/RJ"
    )

    conta1 = ContaCorrente.nova_conta(cliente=cliente1, numero=1)
    conta2 = ContaCorrente.nova_conta(cliente=cliente2, numero=2)

    cliente1.adicionar_conta(conta1)
    cliente2.adicionar_conta(conta2)

    print("\n1️⃣\tDEMONSTRAÇÃO DO DECORADOR DE LOG")
    print("-" * 60)

    @log_transacao
    def operacao_teste():
        """Função de teste para demonstrar o decorador."""
        print("   Executando operação de exemplo...")
        return "Operação concluída"

    resultado = operacao_teste()
    print(f"   Resultado: {resultado}")

    print("\n2️⃣\tREALIZANDO TRANSAÇÕES COM LOG")
    print("-" * 60)

    # Transações serão logadas automaticamente.
    transacoes = [
        Deposito(1000),
        Deposito(500),
        Saque(200),
        Saque(150),
        Deposito(300)
    ]

    print("📈 Realizando transações na conta de Ana Silva:")
    for transacao in transacoes:
        cliente1.realizar_transacao(conta1, transacao)

    print("\n📈 Realizando transações na conta de Carlos Santos:")
    cliente2.realizar_transacao(conta2, Deposito(2000))
    cliente2.realizar_transacao(conta2, Saque(300))
    cliente2.realizar_transacao(conta2, Deposito(100))

    print("\n3️⃣\tDEMONSTRAÇÃO DO GERADOR DE RELATÓRIOS")
    print("-" * 60)

    print("📋 Relatório completo da conta 1:")
    for i, transacao in enumerate(conta1.historico.gerar_relatorio(), 1):
        print(f"  {i}. {transacao['tipo']}: R$ {transacao['valor']:.2f} - {transacao['data']}")

    print("\n📈 Apenas depósitos da conta 1:")
    for i, transacao in enumerate(conta1.historico.gerar_relatorio("Deposito"), 1):
        print(f"  {i}. {transacao['tipo']}: R$ {transacao['valor']:.2f} - {transacao['data']}")

    print("\n📉 Apenas saques da conta 1:")
    for i, transacao in enumerate(conta1.historico.gerar_relatorio("Saque"), 1):
        print(f"  {i}. {transacao['tipo']}: R$ {transacao['valor']:.2f} - {transacao['data']}")

    print("\n4️⃣\tDEMONSTRAÇÃO DO ITERADOR PERSONALIZADO")
    print("-" * 60)

    contas = [conta1, conta2]

    print("🏦 Iterando sobre todas as contas:\n")
    for i, dados_conta in enumerate(ContaIterador(contas), 1):
        print(f"Conta {i}:\n")
        print(textwrap.dedent(dados_conta))

    print("\n5️⃣\tDEMONSTRAÇÃO DO GERADOR DE TRANSAÇÕES DO DIA")
    print("-" * 60)

    print("📅 Transações de hoje:")
    for transacao in conta1.historico.transacoes_do_dia():
        print(f"  • {transacao['tipo']}: R$ {transacao['valor']:.2f} - {transacao['data']}")

    print("\n6️⃣\tRESUMO FINAL")
    print("-" * 60)

    print("✅ Funcionalidades implementadas:")
    print("   🎯 Decorador de log para transações")
    print("   🔄 Gerador para relatórios filtrados")
    print("   📊 Gerador para transações por data")
    print("   🔍 Iterador personalizado para contas")
    print("   📈 Sistema de logging automático")

    print(f"\n💰 Saldo final Ana Silva: R$ {conta1.saldo:.2f}")
    print(f"💰 Saldo final Carlos Santos: R$ {conta2.saldo:.2f}")

    print("\n" + "="*60)
    print("🎉 DEMONSTRAÇÃO v4.0 CONCLUÍDA!")
    print("="*60)

if __name__ == "__main__":
    demonstracao_v4()
