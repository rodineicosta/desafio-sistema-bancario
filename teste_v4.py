#!/usr/bin/env python3
"""
Teste da versão 4.1 do Sistema Bancário
Foco: Validação do limite de 10 transações diárias e funcionalidades de data/hora
"""

import sys
from datetime import datetime, timedelta
sys.path.append('.')
from desafio import *

def teste_limite_transacoes_diarias():
    """Testa o limite de 10 transações diárias."""
    print("🧪 TESTE V4.1: Limite de 10 transações diárias")
    print("="*60)

    # Criar cliente e conta.
    cliente = PessoaFisica(nome="Teste Limite", data_nascimento="01/01/1990", cpf="12345678999", endereco="Rua Teste, 123")
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=1)
    cliente.adicionar_conta(conta)

    # Fazer depósito inicial.
    print("\n1. Fazendo depósito inicial de R$ 1000,00")
    deposito = Deposito(1000.00)
    resultado = cliente.realizar_transacao(conta, deposito)
    print(f"   Resultado: {'✅ Sucesso' if resultado else '❌ Falha'}")
    print(f"   Saldo atual: R$ {conta.saldo:.2f}")

    # Testar múltiplas transações.
    print("\n2. Testando múltiplas transações:")
    transacoes_ok = 0

    for i in range(2, 12):  # Transações 2 a 11 (já fizemos 1).
        if i <= 10:
            # Dentro do limite.
            deposito = Deposito(10.00)
            resultado = cliente.realizar_transacao(conta, deposito)
            print(f"   Transação {i}: {'✅ Aceita' if resultado else '❌ Rejeitada'}")
            if resultado:
                transacoes_ok += 1
        else:
            # Fora do limite (11ª transação).
            deposito = Deposito(10.00)
            resultado = cliente.realizar_transacao(conta, deposito)
            print(f"   Transação {i}: {'✅ Aceita' if resultado else '❌ Rejeitada (limite atingido)'}")

    print(f"\n   Total de transações do dia: {len(list(conta.historico.transacoes_do_dia()))}")
    print(f"   Saldo final: R$ {conta.saldo:.2f}")

    # Verificar histórico.
    print("\n3. Verificando histórico de transações:")
    for i, transacao in enumerate(conta.historico.transacoes[-5:], 1):  # Últimas 5.
        print(f"   {i}. {transacao['tipo']}: R$ {transacao['valor']:.2f} - {transacao['data']}")

    return len(list(conta.historico.transacoes_do_dia())) == 10

def teste_funcionalidades_datetime():
    """Testa as funcionalidades de data e hora."""
    print("\n\n🧪 TESTE V4.1: Funcionalidades de Data/Hora")
    print("="*60)

    # Criar cliente e conta.
    cliente = PessoaFisica(nome="Teste DateTime", data_nascimento="15/06/1985", cpf="98765432100", endereco="Av. Tempo, 456")
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=2)
    cliente.adicionar_conta(conta)

    print("\n1. Testando timestamps das transações:")

    # Fazer algumas transações com pequenos intervalos.
    import time

    for i in range(3):
        deposito = Deposito(100.00)
        antes = datetime.now()
        resultado = cliente.realizar_transacao(conta, deposito)
        depois = datetime.now()

        if resultado:
            ultima_transacao = conta.historico.transacoes[-1]
            print(f"   Transação {i+1}: {ultima_transacao['data']}")
            print(f"   Intervalo: Entre {antes.strftime('%H:%M:%S')} e {depois.strftime('%H:%M:%S')}")

        time.sleep(0.1)  # Pequeno delay para garantir timestamps diferentes.

    print("\n2. Testando gerador de transações do dia:")
    transacoes_hoje = list(conta.historico.transacoes_do_dia())
    print(f"   Transações encontradas hoje: {len(transacoes_hoje)}")

    for transacao in transacoes_hoje:
        print(f"   - {transacao['tipo']}: R$ {transacao['valor']:.2f}")

    return len(transacoes_hoje) == 3

def teste_decorator_log():
    """Testa o decorator de log de transações."""
    print("\n\n🧪 TESTE V4.1: Decorator de Log")
    print("="*60)

    cliente = PessoaFisica(nome="Teste Log", data_nascimento="10/12/1992", cpf="11122233344", endereco="Rua Log, 789")
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=3)
    cliente.adicionar_conta(conta)

    print("\n1. Testando log de depósito:")
    deposito = Deposito(500.00)
    # O decorator vai imprimir automaticamente.
    resultado = cliente.realizar_transacao(conta, deposito)

    print("\n2. Testando log de saque:")
    saque = Saque(100.00)
    resultado = cliente.realizar_transacao(conta, saque)

    return True

def main():
    """Executa todos os testes da v4.1."""
    print("🔍 INICIANDO TESTES DO SISTEMA BANCÁRIO V4.1")
    print("💫 Funcionalidades: Data/Hora e Limite de Transações")
    print("="*60)

    resultados = []

    # Teste 1: Limite de transações.
    try:
        resultado1 = teste_limite_transacoes_diarias()
        resultados.append(("Limite 10 transações", resultado1))
    except Exception as e:
        print(f"❌ Erro no teste de limite: {e}")
        resultados.append(("Limite 10 transações", False))

    # Teste 2: Funcionalidades de data/hora.
    try:
        resultado2 = teste_funcionalidades_datetime()
        resultados.append(("Funcionalidades DateTime", resultado2))
    except Exception as e:
        print(f"❌ Erro no teste de datetime: {e}")
        resultados.append(("Funcionalidades DateTime", False))

    # Teste 3: Decorator de log.
    try:
        resultado3 = teste_decorator_log()
        resultados.append(("Decorator de Log", resultado3))
    except Exception as e:
        print(f"❌ Erro no teste de decorator: {e}")
        resultados.append(("Decorator de Log", False))

    # Relatório final.
    print("\n\n📊 RELATÓRIO FINAL DOS TESTES V4.1")
    print("="*60)

    sucessos = 0
    for nome, resultado in resultados:
        status = "✅ PASSOU" if resultado else "❌ FALHOU"
        print(f"{nome:<25} {status}")
        if resultado:
            sucessos += 1

    print("-"*60)
    print(f"Total: {sucessos}/{len(resultados)} testes passaram")

    if sucessos == len(resultados):
        print("\n🎉 TODOS OS TESTES DA V4.1 PASSARAM!")
        print("✨ Sistema bancário com data/hora funcionando perfeitamente!")
    else:
        print(f"\n⚠️  {len(resultados) - sucessos} teste(s) falharam")
        print("🔧 Verifique os logs acima para mais detalhes")

if __name__ == "__main__":
    main()
