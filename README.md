# 🏦 Sistema Bancário em Python

## 📖 Descrição do Projeto

Este projeto é parte do desafio **Criando um Sistema Bancário com Python**, da Formação **Santander 2025 - Back-End com Python**. O objetivo é criar um Sistema Bancário em Python que simule operações bancárias essenciais de forma funcional e eficiente.

O desafio do projeto visa criar um Sistema Bancário em Python, com o objetivo de implementar três operações essenciais: **depósito**, **saque** e **visualização de extrato**.

## ⚡ Funcionalidades

### 🔹 Operações Disponíveis

- **[1] Depositar**: Permite realizar depósitos na conta
- **[2] Sacar**: Permite realizar saques com limitações de segurança
- **[3] Extrato**: Exibe histórico de transações e saldo atual
- **[0] Sair**: Encerra o sistema

### 🔒 Regras de Negócio

#### Depósitos

- ✅ Aceita apenas valores positivos;
- ✅ Não há limite de valor ou quantidade;
- ✅ Atualiza automaticamente o saldo e extrato.

#### Saques

- ✅ Aceita apenas valores positivos;
- ✅ Limite máximo de **R$ 500,00 por saque**;
- ✅ Limite de **3 saques diários**;
- ✅ Verificação de saldo suficiente;
- ✅ Alertas em caso de violação das regras.

#### Extrato

- ✅ Lista todas as movimentações (depósitos e saques);
- ✅ Exibe saldo atual;
- ✅ Formatação monetária: **R$ xxx.xx**;
- ✅ Mensagem quando não há movimentações.

## 🚀 Como Executar

### Pré-requisitos

- Python 3.6 ou superior

### Executando o Sistema

```bash
# Clone o repositório (se aplicável)
git clone https://github.com/rodineicosta/desafio-sistema-bancario.git

# Navegue até o diretório
cd desafio-sistema-bancario

# Execute o sistema
python desafio.py
```

## 🎮 Como Usar

1. **Execute o programa**
2. **Escolha uma opção do menu**:
   - Digite `1` para depositar;
   - Digite `2` para sacar;
   - Digite `3` para ver o extrato;
   - Digite `0` para sair.
3. **Siga as instruções na tela**

### Exemplo de Uso

```text
================ SISTEMA BANCÁRIO ================

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> 1
Informe o valor do depósito: 1000
Depósito de R$ 1000.00 realizado com sucesso!
```

## 🏗️ Estrutura do Código

O sistema foi desenvolvido com uma arquitetura modular e organizada:

```python
def depositar(saldo, extrato)        # Gerencia operações de depósito.
def sacar(...)                       # Gerencia operações de saque.
def exibir_extrato(saldo, extrato)   # Exibe extrato e saldo.
def main()                           # Função principal do sistema.
```

### Características Técnicas

- ✅ **Código modular** com funções específicas;
- ✅ **Sem dependências externas** (Python puro);
- ✅ **Tratamento de erros** para entradas inválidas;
- ✅ **Interface simples** e intuitiva;
- ✅ **Documentação** com docstrings.

## 🔧 Recursos Implementados

- **Validação de entrada**: Impede valores negativos ou inválidos;
- **Controle de limites**: Monitora limites diários e por transação;
- **Histórico completo**: Mantém registro de todas as operações;
- **Feedback ao usuário**: Mensagens claras de sucesso/erro;
- **Formatação monetária**: Padrão brasileiro (R$ xxx.xx).

## 📝 Exemplo de Extrato

```text
================ EXTRATO ================
Depósito: R$ 1000.00
Saque: R$ 200.00
Depósito: R$ 500.00
Saque: R$ 100.00

Saldo atual: R$ 1200.00
==========================================
```

## 🎯 Objetivos do Desafio

Este projeto visa desenvolver:

- **Lógica de programação** em Python;
- **Estruturas condicionais** e de repetição;
- **Manipulação de strings** e formatação;
- **Controle de fluxo** e validações.

## 📚 Tecnologias Utilizadas

- **Python 3.x**;
- **Programação procedural**;
- **Estruturas de dados básicas** (strings, números, booleanos).

## 🏆 Sobre o Curso

Este projeto faz parte do curso de **Santander 2025 - Back-End com Python** da **DIO (Digital Innovation One)** em parceria com o **Santander**. O curso visa capacitar desenvolvedores em Python para o mercado de trabalho.

---

**Desenvolvido como parte do Desafio DIO + Santander 2025** 🚀
