#!/usr/bin/env python3
"""
Demonstração Interativa do Sistema Bancário POO v3.0
"""
from desafio import (
    PessoaFisica, ContaCorrente, Deposito, Saque
)

def demonstracao_completa():
    """Demonstração completa das funcionalidades POO."""
    print("🏦 SISTEMA BANCÁRIO POO v3.0 - DEMONSTRAÇÃO")
    print("="*60)

    # 1. Criando clientes
    print("\n1️⃣ CRIANDO CLIENTES")
    print("-" * 30)

    cliente1 = PessoaFisica(
        nome="João Silva",
        data_nascimento="15/08/1990",
        cpf="12345678901",
        endereco="Rua das Flores, 123 - Centro - São Paulo/SP"
    )

    cliente2 = PessoaFisica(
        nome="Maria Santos",
        data_nascimento="22/03/1985",
        cpf="98765432100",
        endereco="Av. Paulista, 456 - Bela Vista - São Paulo/SP"
    )

    print(f"✅ {cliente1.nome} cadastrado (CPF: {cliente1.cpf})")
    print(f"✅ {cliente2.nome} cadastrada (CPF: {cliente2.cpf})")

    # 2. Criando contas
    print("\n2️⃣ CRIANDO CONTAS")
    print("-" * 30)

    conta1 = ContaCorrente.nova_conta(cliente=cliente1, numero=1)
    conta2 = ContaCorrente.nova_conta(cliente=cliente2, numero=2)

    cliente1.adicionar_conta(conta1)
    cliente2.adicionar_conta(conta2)

    print(f"🏛️ Conta {conta1.agencia}-{conta1.numero} criada para {conta1.cliente.nome}")
    print(f"🏛️ Conta {conta2.agencia}-{conta2.numero} criada para {conta2.cliente.nome}")

    # 3. Operações de depósito
    print("\n3️⃣ REALIZANDO DEPÓSITOS")
    print("-" * 30)

    deposito1 = Deposito(1500)
    deposito2 = Deposito(2000)
    deposito3 = Deposito(800)

    print(f"📈 Depositando R$ {deposito1.valor:.2f} na conta de {cliente1.nome}:")
    cliente1.realizar_transacao(conta1, deposito1)

    print(f"\n📈 Depositando R$ {deposito2.valor:.2f} na conta de {cliente2.nome}:")
    cliente2.realizar_transacao(conta2, deposito2)

    print(f"\n📈 Depositando mais R$ {deposito3.valor:.2f} na conta de {cliente1.nome}:")
    cliente1.realizar_transacao(conta1, deposito3)

    # 4. Operações de saque
    print("\n4️⃣ REALIZANDO SAQUES")
    print("-" * 30)

    saque1 = Saque(400)
    saque2 = Saque(600)  # Este vai falhar (excede limite)
    saque3 = Saque(300)

    print(f"📉 Sacando R$ {saque1.valor:.2f} da conta de {cliente1.nome}:")
    cliente1.realizar_transacao(conta1, saque1)

    print(f"\n📉 Tentando sacar R$ {saque2.valor:.2f} da conta de {cliente2.nome}:")
    cliente2.realizar_transacao(conta2, saque2)

    print(f"\n📉 Sacando R$ {saque3.valor:.2f} da conta de {cliente2.nome}:")
    cliente2.realizar_transacao(conta2, saque3)

    # 5. Múltiplos saques para testar limite
    print("\n5️⃣ TESTANDO LIMITE DE SAQUES")
    print("-" * 30)

    print(f"🔢 Testando múltiplos saques na conta de {cliente1.nome}:")
    for i in range(1, 5):  # 4 saques, mas limite é 3
        saque = Saque(100)
        print(f"   Saque {i} de R$ {saque.valor:.2f}:")
        cliente1.realizar_transacao(conta1, saque)

    # 6. Exibindo saldos finais
    print("\n6️⃣ SALDOS FINAIS")
    print("-" * 30)

    print(f"💰 {cliente1.nome}: R$ {conta1.saldo:.2f}")
    print(f"💰 {cliente2.nome}: R$ {conta2.saldo:.2f}")

    # 7. Histórico de transações
    print("\n7️⃣ HISTÓRICO DE TRANSAÇÕES")
    print("-" * 30)

    print(f"\n📋 Histórico de {cliente1.nome}:")
    for i, transacao in enumerate(conta1.historico.transacoes, 1):
        print(f"   {i}. {transacao['tipo']} - R$ {transacao['valor']:.2f} - {transacao['data']}")

    print(f"\n📋 Histórico de {cliente2.nome}:")
    for i, transacao in enumerate(conta2.historico.transacoes, 1):
        print(f"   {i}. {transacao['tipo']} - R$ {transacao['valor']:.2f} - {transacao['data']}")

    # 8. Demonstração de polimorfismo
    print("\n8️⃣ DEMONSTRAÇÃO DE POLIMORFISMO")
    print("-" * 30)

    transacoes_mistas = [
        Deposito(200),
        Saque(150),
        Deposito(300),
        Saque(250)
    ]

    print(f"🔄 Executando transações polimórficas para {cliente1.nome}:")
    saldo_anterior = conta1.saldo

    for i, transacao in enumerate(transacoes_mistas, 1):
        print(f"   {i}. {transacao.__class__.__name__} de R$ {transacao.valor:.2f}")
        cliente1.realizar_transacao(conta1, transacao)
        print(f"      Saldo: R$ {conta1.saldo:.2f}")

    print(f"\n💡 Variação do saldo: R$ {conta1.saldo - saldo_anterior:.2f}")

    print("\n" + "="*60)
    print("🎉 DEMONSTRAÇÃO CONCLUÍDA COM SUCESSO!")
    print("✨ Todos os conceitos de POO foram aplicados:")
    print("   • Encapsulamento (atributos privados)")
    print("   • Herança (PessoaFisica ← Cliente, ContaCorrente ← Conta)")
    print("   • Polimorfismo (Deposito/Saque implementam Transacao)")
    print("   • Abstração (classe abstrata Transacao)")
    print("="*60)

if __name__ == "__main__":
    demonstracao_completa()
