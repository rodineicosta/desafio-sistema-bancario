#!/usr/bin/env python3
"""
Testes Automatizados para Sistema Bancário v4.0
Decoradores, Geradores e Iteradores
"""
from desafio import (
    PessoaFisica, ContaCorrente, Deposito, Saque,
    ContaIterador, Historico, log_transacao
)

def teste_decorador_log():
    """Testa o decorador de log."""
    print("🧪 TESTE: Decorador de Log")
    print("-" * 30)

    @log_transacao
    def funcao_teste():
        return "Teste realizado"

    resultado = funcao_teste()
    assert resultado == "Teste realizado"
    print("✅ Decorador funcionando corretamente")

def teste_gerador_relatorios():
    """Testa o gerador de relatórios."""
    print("\n🧪 TESTE: Gerador de Relatórios")
    print("-" * 30)

    historico = Historico()

    # Simulando transações.
    historico.adicionar_transacao(Deposito(100))
    historico.adicionar_transacao(Saque(50))
    historico.adicionar_transacao(Deposito(200))

    # Teste: todas as transações.
    todas = list(historico.gerar_relatorio())
    assert len(todas) == 3
    print("✅ Gerador de todas as transações funcionando")

    # Teste: apenas depósitos.
    depositos = list(historico.gerar_relatorio("Deposito"))
    assert len(depositos) == 2
    assert all(t["tipo"] == "Deposito" for t in depositos)
    print("✅ Filtro de depósitos funcionando")

    # Teste: apenas saques.
    saques = list(historico.gerar_relatorio("Saque"))
    assert len(saques) == 1
    assert all(t["tipo"] == "Saque" for t in saques)
    print("✅ Filtro de saques funcionando")

def teste_iterador_contas():
    """Testa o iterador personalizado de contas."""
    print("\n🧪 TESTE: Iterador Personalizado")
    print("-" * 30)

    # Criando contas de teste.
    cliente1 = PessoaFisica("Ana", "01/01/1990", "111", "Rua A")
    cliente2 = PessoaFisica("Carlos", "02/02/1985", "222", "Rua B")

    conta1 = ContaCorrente.nova_conta(cliente1, 1)
    conta2 = ContaCorrente.nova_conta(cliente2, 2)

    contas = [conta1, conta2]

    # Testando iterador.
    dados_contas = list(ContaIterador(contas))
    assert len(dados_contas) == 2

    # Verificando se os dados são strings formatadas.
    assert isinstance(dados_contas[0], str)
    assert isinstance(dados_contas[1], str)

    # Verificando se contêm as informações esperadas.
    assert "Ana" in dados_contas[0]
    assert "Carlos" in dados_contas[1]
    assert "0001" in dados_contas[0]  # Agência.
    assert "0001" in dados_contas[1]  # Agência.

    print("✅ Iterador personalizado funcionando")

def teste_transacoes_do_dia():
    """Testa o gerador de transações do dia."""
    print("\n🧪 TESTE: Transações do Dia")
    print("-" * 30)

    historico = Historico()

    # Adicionando transações.
    historico.adicionar_transacao(Deposito(100))
    historico.adicionar_transacao(Saque(50))

    # Testando transações de hoje.
    from datetime import datetime
    hoje = datetime.now().strftime("%d/%m/%Y")

    transacoes_hoje = list(historico.transacoes_do_dia(hoje))
    assert len(transacoes_hoje) == 2

    print("✅ Gerador de transações do dia funcionando")

def teste_integrado():
    """Teste integrado de todas as funcionalidades."""
    print("\n🧪 TESTE: Integração Completa")
    print("-" * 30)

    # Criando cliente e conta.
    cliente = PessoaFisica("Teste", "01/01/2000", "12345678901", "Rua Teste")
    conta = ContaCorrente.nova_conta(cliente, 1)
    cliente.adicionar_conta(conta)

    # Realizando transações.
    transacoes = [
        Deposito(1000),
        Saque(200),
        Deposito(500),
        Saque(100)
    ]

    for transacao in transacoes:
        cliente.realizar_transacao(conta, transacao)

    # Verificando saldo.
    assert conta.saldo == 1200  # 1000 - 200 + 500 - 100.

    # Testando gerador de relatórios.
    depositos = list(conta.historico.gerar_relatorio("Deposito"))
    saques = list(conta.historico.gerar_relatorio("Saque"))

    assert len(depositos) == 2
    assert len(saques) == 2

    # Testando iterador.
    contas = [conta]
    dados = list(ContaIterador(contas))
    assert "1200" in dados[0]  # Verificando se o saldo aparece na string formatada.

    print("✅ Teste integrado bem-sucedido")

def executar_todos_os_testes():
    """Executa todos os testes."""
    print("🚀 SISTEMA BANCÁRIO v4.0 - TESTES AUTOMATIZADOS")
    print("=" * 60)

    try:
        teste_decorador_log()
        teste_gerador_relatorios()
        teste_iterador_contas()
        teste_transacoes_do_dia()
        teste_integrado()

        print("\n" + "=" * 60)
        print("🎉 TODOS OS TESTES PASSARAM!")
        print("✅ Decoradores funcionando")
        print("✅ Geradores funcionando")
        print("✅ Iteradores funcionando")
        print("✅ Integração funcionando")
        print("=" * 60)

    except AssertionError as e:
        print(f"\n❌ TESTE FALHOU: {e}")
    except Exception as e:
        print(f"\n💥 ERRO INESPERADO: {e}")

if __name__ == "__main__":
    executar_todos_os_testes()
