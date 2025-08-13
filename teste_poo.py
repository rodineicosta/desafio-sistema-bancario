#!/usr/bin/env python3
"""
Script de teste para o Sistema Bancário POO v3.0
"""
from desafio import (
    Cliente, PessoaFisica, Conta, ContaCorrente,
    Historico, Transacao, Deposito, Saque
)

def teste_classes_basicas():
    """Testa a criação e funcionamento das classes básicas."""
    print("="*50)
    print("🧪 TESTE 1: Classes Básicas")
    print("="*50)

    # Teste Cliente e PessoaFisica
    cliente = PessoaFisica(
        nome="João Silva",
        data_nascimento="01/01/1990",
        cpf="12345678901",
        endereco="Rua A, 123 - Centro - São Paulo/SP"
    )

    print(f"✅ Cliente criado: {cliente.nome}")
    print(f"   CPF: {cliente.cpf}")
    print(f"   Endereço: {cliente.endereco}")

    # Teste Conta
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=1)
    cliente.adicionar_conta(conta)

    print(f"✅ Conta criada: {conta.agencia}-{conta.numero}")
    print(f"   Titular: {conta.cliente.nome}")
    print(f"   Saldo inicial: R$ {conta.saldo:.2f}")

    return cliente, conta

def teste_transacoes(cliente, conta):
    """Testa as transações de depósito e saque."""
    print("\n" + "="*50)
    print("🧪 TESTE 2: Transações")
    print("="*50)

    # Teste Depósito
    print("\n📈 Testando Depósitos:")
    deposito1 = Deposito(1000)
    cliente.realizar_transacao(conta, deposito1)

    deposito2 = Deposito(500)
    cliente.realizar_transacao(conta, deposito2)

    print(f"   Saldo após depósitos: R$ {conta.saldo:.2f}")

    # Teste Saque válido
    print("\n📉 Testando Saques:")
    saque1 = Saque(200)
    cliente.realizar_transacao(conta, saque1)

    print(f"   Saldo após saque: R$ {conta.saldo:.2f}")

    # Teste Saque inválido (excede limite)
    print("\n❌ Testando Saque Inválido (excede limite):")
    saque_invalido = Saque(600)  # Excede limite de R$ 500
    cliente.realizar_transacao(conta, saque_invalido)

    # Teste múltiplos saques (excede limite diário)
    print("\n❌ Testando Múltiplos Saques (excede limite diário):")
    for i in range(4):  # Limite é 3 saques
        saque = Saque(100)
        print(f"   Saque {i+1}:")
        cliente.realizar_transacao(conta, saque)

    print(f"   Saldo final: R$ {conta.saldo:.2f}")

def teste_historico(conta):
    """Testa o histórico de transações."""
    print("\n" + "="*50)
    print("🧪 TESTE 3: Histórico")
    print("="*50)

    print(f"📋 Histórico da Conta {conta.numero}:")
    transacoes = conta.historico.transacoes

    if not transacoes:
        print("   Nenhuma transação encontrada.")
    else:
        for i, transacao in enumerate(transacoes, 1):
            print(f"   {i}. {transacao['tipo']} - R$ {transacao['valor']:.2f} - {transacao['data']}")

def teste_polimorfismo():
    """Testa o polimorfismo com diferentes tipos de transação."""
    print("\n" + "="*50)
    print("🧪 TESTE 4: Polimorfismo")
    print("="*50)

    # Criando cliente e conta para teste
    cliente = PessoaFisica(
        nome="Maria Santos",
        data_nascimento="15/05/1985",
        cpf="98765432100",
        endereco="Av. B, 456 - Jardins - Rio de Janeiro/RJ"
    )

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=2)
    cliente.adicionar_conta(conta)

    # Lista de transações diferentes
    transacoes = [
        Deposito(800),
        Saque(300),
        Deposito(200),
        Saque(150)
    ]

    print(f"👤 Cliente: {cliente.nome}")
    print(f"🏦 Conta: {conta.agencia}-{conta.numero}")
    print(f"💰 Saldo inicial: R$ {conta.saldo:.2f}")

    print("\n🔄 Executando transações polimórficas:")
    for i, transacao in enumerate(transacoes, 1):
        print(f"\n   {i}. {transacao.__class__.__name__} de R$ {transacao.valor:.2f}")
        cliente.realizar_transacao(conta, transacao)
        print(f"      Saldo atual: R$ {conta.saldo:.2f}")

def teste_heranca():
    """Testa a herança entre as classes."""
    print("\n" + "="*50)
    print("🧪 TESTE 5: Herança")
    print("="*50)

    # Teste herança Cliente -> PessoaFisica
    cliente = PessoaFisica("Ana Costa", "10/12/1992", "11122233344", "Rua C, 789")
    print(f"✅ PessoaFisica é instância de Cliente: {isinstance(cliente, Cliente)}")

    # Teste herança Conta -> ContaCorrente
    conta = ContaCorrente.nova_conta(cliente, 3)
    print(f"✅ ContaCorrente é instância de Conta: {isinstance(conta, Conta)}")

    # Teste herança Transacao -> Deposito/Saque
    deposito = Deposito(500)
    saque = Saque(200)
    print(f"✅ Deposito é instância de Transacao: {isinstance(deposito, Transacao)}")
    print(f"✅ Saque é instância de Transacao: {isinstance(saque, Transacao)}")

def teste_abstrato():
    """Testa se a classe abstrata não pode ser instanciada."""
    print("\n" + "="*50)
    print("🧪 TESTE 6: Classe Abstrata")
    print("="*50)

    try:
        transacao = Transacao()
        print("❌ ERRO: Conseguiu instanciar classe abstrata!")
    except TypeError as e:
        print(f"✅ Classe abstrata funcionando: {e}")

def main():
    """Executa todos os testes."""
    print("🏦 SISTEMA BANCÁRIO POO v3.0 - TESTES")
    print("="*60)

    try:
        # Testes básicos
        cliente, conta = teste_classes_basicas()

        # Testes de transações
        teste_transacoes(cliente, conta)

        # Teste de histórico
        teste_historico(conta)

        # Teste de polimorfismo
        teste_polimorfismo()

        # Teste de herança
        teste_heranca()

        # Teste de classe abstrata
        teste_abstrato()

        print("\n" + "="*60)
        print("🎉 TODOS OS TESTES CONCLUÍDOS!")
        print("="*60)

    except Exception as e:
        print(f"\n❌ ERRO durante os testes: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
