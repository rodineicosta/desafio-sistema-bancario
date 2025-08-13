#!/usr/bin/env python3
"""
Demo do Sistema Bancário v4.1 - Lidando com Data, Hora e Fuso Horário
Funcionalidades: Limite de 10 transações diárias, timestamps detalhados, decorators
"""

import sys
from datetime import datetime
sys.path.append('.')
from desafio import *

def demo_v4_1():
    """Demonstração completa da versão 4.1."""
    print("🌟 SISTEMA BANCÁRIO V4.1 - DEMO COMPLETA")
    print("🕐 Funcionalidades: Data/Hora e Limite de Transações")
    print("="*65)

    # Criar cliente.
    print("\n1. 👤 Criando cliente...")
    cliente = PessoaFisica(
        nome="Maria Silva Santos",
        data_nascimento="15/03/1985",
        cpf="12345678901",
        endereco="Rua das Flores, 123 - São Paulo/SP"
    )

    # Criar conta.
    print("2. 🏦 Criando conta corrente...")
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=1001)
    cliente.adicionar_conta(conta)

    print(f"   ✅ Conta {conta.numero} criada na agência {conta.agencia}")
    print(f"   👤 Titular: {conta.cliente.nome}")

    # Depósito inicial.
    print("\n3. 💰 Realizando depósito inicial...")
    deposito_inicial = Deposito(5000.00)
    resultado = cliente.realizar_transacao(conta, deposito_inicial)
    print(f"   Status: {'✅ Sucesso' if resultado else '❌ Falha'}")
    print(f"   💵 Saldo atual: R$ {conta.saldo:.2f}")

    # Demonstrar múltiplas transações.
    print("\n4. 🔄 Testando múltiplas transações...")
    transacoes_teste = [
        ("Depósito", Deposito(1000.00)),
        ("Saque", Saque(500.00)),
        ("Depósito", Deposito(250.00)),
        ("Saque", Saque(100.00)),
        ("Depósito", Deposito(750.00)),
    ]

    for i, (tipo, transacao) in enumerate(transacoes_teste, 1):
        resultado = cliente.realizar_transacao(conta, transacao)
        status = "✅" if resultado else "❌"
        print(f"   {i}. {status} {tipo}: R$ {transacao.valor:.2f}")

    print(f"   💵 Saldo final: R$ {conta.saldo:.2f}")

    # Mostrar extrato detalhado.
    print("\n5. 📋 Extrato detalhado com timestamps:")
    print("   " + "="*55)
    print(f"   📅 Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"   👤 Titular: {conta.cliente.nome}")
    print(f"   🏦 Conta: {conta.agencia}-{conta.numero}")
    print("   " + "-"*55)

    for i, transacao in enumerate(conta.historico.transacoes, 1):
        emoji = "📈" if transacao['tipo'] == "Deposito" else "📉"
        print(f"   {i:2d}. {emoji} {transacao['tipo']}: R$ {transacao['valor']:>8.2f} - {transacao['data']}")

    print("   " + "-"*55)
    print(f"   💰 Saldo: R$ {conta.saldo:>8.2f}")
    print(f"   📊 Transações hoje: {len(list(conta.historico.transacoes_do_dia()))}/10")
    print("   " + "="*55)

    # Testar limite de transações.
    print("\n6. ⚠️  Testando limite de 10 transações diárias...")
    transacoes_restantes = 10 - len(list(conta.historico.transacoes_do_dia()))
    print(f"   Transações restantes hoje: {transacoes_restantes}")

    if transacoes_restantes > 0:
        print(f"   Fazendo {transacoes_restantes} transações restantes...")
        for i in range(transacoes_restantes):
            deposito = Deposito(50.00)
            resultado = cliente.realizar_transacao(conta, deposito)
            print(f"   {i+1}. {'✅' if resultado else '❌'} Depósito R$ 50,00")

    # Tentar transação além do limite.
    print("\n   🚫 Tentando 11ª transação (deve falhar)...")
    deposito_extra = Deposito(100.00)
    resultado = cliente.realizar_transacao(conta, deposito_extra)
    print(f"   Resultado: {'✅ Aceita' if resultado else '❌ Rejeitada (limite atingido)'}")

    # Mostrar gerador de relatório
    print("\n7. 📊 Testando gerador de relatório...")
    print("   Gerando relatório das transações de hoje:")

    contador = 0
    for relatorio in conta.historico.gerar_relatorio():
        tipo_emoji = "�" if relatorio['tipo'] == "Deposito" else "📉"
        print(f"   📝 {tipo_emoji} {relatorio['tipo']}: R$ {relatorio['valor']:.2f} - {relatorio['data']}")
        contador += 1
        if contador >= 3:  # Limitar saída
            print("   📝 ... (mais transações)")
            break

    # Iterator de contas.
    print("\n8. 🔍 Testando iterator de contas...")
    iterator = ContaIterador([conta])
    print("   Dados da conta via iterator:")
    for dado in iterator:
        for linha in dado.split('\n'):
            if linha.strip():
                print(f"   {linha}")
        break  # Só mostrar a primeira conta.

    # Estatísticas finais.
    print("\n9. 📈 Estatísticas finais:")
    total_transacoes = len(conta.historico.transacoes)
    transacoes_hoje = len(list(conta.historico.transacoes_do_dia()))

    depositos = [t for t in conta.historico.transacoes if t['tipo'] == 'Deposito']
    saques = [t for t in conta.historico.transacoes if t['tipo'] == 'Saque']

    total_depositado = sum(t['valor'] for t in depositos)
    total_sacado = sum(t['valor'] for t in saques)

    print(f"   📊 Total de transações: {total_transacoes}")
    print(f"   📊 Transações hoje: {transacoes_hoje}/10")
    print(f"   📈 Total depositado: R$ {total_depositado:.2f}")
    print(f"   📉 Total sacado: R$ {total_sacado:.2f}")
    print(f"   💰 Saldo final: R$ {conta.saldo:.2f}")

    print("\n" + "="*65)
    print("🎉 DEMO V4.1 CONCLUÍDA COM SUCESSO!")
    print("✨ Todas as funcionalidades de data/hora estão operacionais!")
    print("⏰ Sistema respeitando limite de 10 transações por dia!")
    print("="*65)

if __name__ == "__main__":
    demo_v4_1()
