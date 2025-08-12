# 🏦 Sistema Bancário em Python - Versão 2.0

## 📖 Descrição do Projeto

Este projeto é parte do desafio **Otimizando o Sistema Bancário com Funções Python**, da Formação **Santander 2025 - Back-End com Python**. O objetivo é criar um Sistema Bancário em Python otimizado com funções modulares que simule operações bancárias completas, incluindo gestão de clientes e contas correntes.

A **Versão 2.0** do sistema implementa uma arquitetura modularizada com funções específicas, gestão de múltiplos usuários e contas, seguindo as melhores práticas de programação Python.

## ⚡ Funcionalidades

### 🔹 Operações Disponíveis

- **[1] Depositar**: Permite realizar depósitos na conta
- **[2] Sacar**: Permite realizar saques com limitações de segurança
- **[3] Visualizar Extrato**: Exibe histórico de transações e saldo atual
- **[4] Nova Conta Corrente**: Cria nova conta vinculada a um cliente
- **[5] Novo Cliente**: Cadastra novo cliente no sistema
- **[6] Listar Contas Correntes**: Exibe todas as contas cadastradas
- **[7] Listar Clientes**: Exibe todos os clientes cadastrados
- **[0] Sair**: Encerra o sistema

### 🔒 Regras de Negócio

#### Depósitos

- ✅ Aceita apenas valores positivos;
- ✅ Não há limite de valor ou quantidade;
- ✅ Atualiza automaticamente o saldo e extrato;
- ✅ **Função com argumentos posicionais apenas** (`positional only`).

#### Saques

- ✅ Aceita apenas valores positivos;
- ✅ Limite máximo de **R$ 500,00 por saque**;
- ✅ Limite de **3 saques diários**;
- ✅ Verificação de saldo suficiente;
- ✅ Alertas em caso de violação das regras;
- ✅ **Função com argumentos nomeados apenas** (`keyword only`).

#### Extrato

- ✅ Lista todas as movimentações (depósitos e saques);
- ✅ Exibe saldo atual;
- ✅ Formatação monetária: **R$ xxx.xx**;
- ✅ Mensagem quando não há movimentações;
- ✅ **Função com argumentos posicionais e nomeados** (`positional + keyword`).

#### Gestão de Clientes

- ✅ Cadastro com: **Nome, Data Nascimento, CPF, Endereço**;
- ✅ **CPF único** por cliente (não permite duplicatas);
- ✅ **Entrada flexível** de CPF (aceita formatação com pontos/hífens);
- ✅ **Armazenamento padronizado** (apenas números);
- ✅ Validação de dados obrigatórios.

#### Gestão de Contas

- ✅ **Agência fixa**: "0001"
- ✅ **Número sequencial** automático (inicia em 1);
- ✅ **Vinculação obrigatória** com cliente existente;
- ✅ **Um cliente pode ter múltiplas contas**;
- ✅ **Uma conta pertence a apenas um cliente**.

## 🚀 Como Executar

### Pré-requisitos

- Python 3.6 ou superior.

### Executando o Sistema

```bash
# Clone o repositório.
git clone https://github.com/rodineicosta/desafio-sistema-bancario.git

# Navegue até o diretório.
cd desafio-sistema-bancario

# Execute o sistema.
python desafio.py
```

## 🎮 Como Usar

1. **Execute o programa**
2. **Escolha uma opção do menu**:
   - Digite `1` para depositar
   - Digite `2` para sacar
   - Digite `3` para visualizar extrato
   - Digite `4` para criar nova conta corrente
   - Digite `5` para cadastrar novo cliente
   - Digite `6` para listar contas correntes
   - Digite `7` para listar clientes
   - Digite `0` para sair
3. **Siga as instruções na tela**

### Fluxo Recomendado de Uso

```text
1. Primeiro, cadastre um cliente (opção 5);
2. Depois, crie uma conta para este cliente (opção 4);
3. Realize operações bancárias (opções 1, 2, 3);
4. Use as listagens para verificar dados (opções 6, 7).
```

### Exemplo de Uso Completo

```text
================ MENU ================
[1]	Depositar
[2]	Sacar
[3]	Visualizar Extrato
[4]	Nova Conta Corrente
[5]	Novo Cliente
[6]	Listar Contas Correntes
[7]	Listar Clientes
[0]	Sair
=> 5

Informe o CPF: 123.456.789-10
Informe o nome completo: João da Silva
Informe a data de nascimento (dd/mm/aaaa): 15/08/1990
Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): Rua das Flores, 123 - Centro - São Paulo/SP

=== Cliente cadastrado com sucesso! ===

=> 4

Informe o CPF do cliente: 123.456.789-10

=== Conta criada com sucesso! ===

=> 1

Informe o valor do depósito: 1000

=== Depósito de R$ 1000.00 realizado com sucesso! ===
```

## 🏗️ Estrutura do Código

A **Versão 2.0** foi desenvolvida com arquitetura modular avançada e segue as melhores práticas de Python:

```python
# Funções principais do sistema.
def depositar(saldo, valor, extrato, /)             # Positional-only arguments.
def sacar(*, saldo, valor, extrato, limite, ...)    # Keyword-only arguments.
def exibir_extrato(saldo, /, *, extrato)            # Mixed arguments.

# Gestão de clientes.
def criar_usuario(usuarios)                         # Cadastro de clientes.
def filtrar_usuario(cpf, usuarios)                  # Busca de clientes.
def listar_usuarios(usuarios)                       # Listagem de clientes.

# Gestão de contas.
def criar_conta(agencia, numero_conta, usuarios)    # Criação de contas.
def listar_contas(contas)                           # Listagem de contas.

# Interface e controle.
def menu()                                          # Menu com textwrap.
def main()                                          # Função principal.
```

### 🚀 Características Técnicas Avançadas

#### **Argumentos de Função Especializados:**

- ✅ **Positional-only** (`/`): Função `depositar()`;
- ✅ **Keyword-only** (`*`): Função `sacar()`;
- ✅ **Mixed arguments**: Função `exibir_extrato()`;
- ✅ **Multiple return values**: Retorno de tuplas.

#### **Gestão de Dados:**

- ✅ **Listas de dicionários** para armazenamento;
- ✅ **Filtragem avançada** com list comprehensions;
- ✅ **Validação robusta** de entrada de dados;
- ✅ **Normalização de CPF** (entrada flexível, armazenamento padronizado).

#### **Interface e UX:**

- ✅ **Menu formatado** com biblioteca `textwrap`;
- ✅ **Mensagens padronizadas** de sucesso/erro;
- ✅ **Formatação consistente** de saídas;
- ✅ **Navegação intuitiva** numerada.

#### **Validações e Segurança:**

- ✅ **CPF único** por cliente;
- ✅ **Vinculação obrigatória** conta-cliente;
- ✅ **Limites de saque** rigorosamente controlados;
- ✅ **Entrada flexível** com validação robusta.

## 🔧 Recursos Implementados v2.0

### **🎯 Novos Recursos:**

- **Gestão completa de clientes** com dados pessoais;
- **Sistema de contas correntes** com numeração automática;
- **Busca inteligente** por CPF (aceita qualquer formato);
- **Listagens organizadas** de clientes e contas;
- **Arquitetura modular** com funções especializadas.

### **🔄 Melhorias da v1.0:**

- **Interface renovada** com menu formatado;
- **Validações aprimoradas** para todas as operações;
- **Código mais limpo** e documentado;
- **Reutilização de código** através de funções;
- **Escalabilidade** para múltiplos usuários.

### **📊 Funcionalidades Técnicas:**

- **Entrada de dados flexível** (CPF com ou sem formatação);
- **Armazenamento padronizado** (apenas números no CPF);
- **Controle de estado** (saldos, limites, histórico);
- **Feedback detalhado** ao usuário;
- **Tratamento de erros** abrangente.

## 📝 Exemplos de Saída

### Extrato Bancário

```text
============================== EXTRATO ==============================
Depósito:		R$ 1000.00
Saque:			R$ 200.00
Depósito:		R$ 500.00
Saque:			R$ 100.00

Saldo:			R$ 1200.00
====================================================================
```

### Listagem de Clientes

```text
====================================================================================================
            Nome:		   João da Silva Santos
            Data Nasc.:	15/08/1990
            CPF:		   12345678910
            Endereço:	Rua das Flores, 123 - Centro - São Paulo/SP
====================================================================================================
            Nome:		   Maria Oliveira Costa
            Data Nasc.:	22/03/1985
            CPF:		   98765432100
            Endereço:	Av. Paulista, 1000 - Bela Vista - São Paulo/SP
```

### Listagem de Contas

```text
====================================================================================================
            Agência:	0001
            C/C:		1
            Titular:	João da Silva Santos
====================================================================================================
            Agência:	0001
            C/C:		2
            Titular:	Maria Oliveira Costa
```

## 🧠 Conceitos Python Aplicados

### **Recursos Avançados:**

- ✅ **Positional-only parameters** (`/`) - `depositar(saldo, valor, extrato, /)`;
- ✅ **Keyword-only parameters** (`*`) - `sacar(*, saldo=..., valor=...)`;
- ✅ **Mixed parameters** - `exibir_extrato(saldo, /, *, extrato)`;
- ✅ **Multiple return values** - Funções retornam tuplas;
- ✅ **List comprehensions** - Filtragem de dados;
- ✅ **Filter function** - Extração de números do CPF;
- ✅ **Biblioteca textwrap** - Formatação de menu;
- ✅ **Docstrings** - Documentação completa das funções.

### **Estruturas de Dados:**

- ✅ **Listas** para coleções de usuários e contas;
- ✅ **Dicionários** para representar entidades (usuário, conta);
- ✅ **Strings** para armazenamento de extrato e CPF;
- ✅ **Tuplas** para retorno múltiplo de funções.

### **Validações e Controle:**

- ✅ **Validação de tipos** (float para valores monetários);
- ✅ **Controle de fluxo** com estruturas condicionais;
- ✅ **Loops** para interface contínua;
- ✅ **Tratamento de casos especiais** (CPF duplicado, conta inexistente).

## 🧪 Casos de Teste

### **Teste de CPF Flexível:**

```python
# Entradas aceitas (todas armazenadas como: 12345678910).
"123.456.789-10"  ✅
"123 456 789 10"  ✅
"12345678910"     ✅
"123-456-789.10"  ✅
```

### **Teste de Limites de Saque:**

```python
# Cenário: 3 saques de R$ 100 cada.
Saque 1: R$ 100.00  ✅ (Permitido - 1/3)
Saque 2: R$ 100.00  ✅ (Permitido - 2/3)
Saque 3: R$ 100.00  ✅ (Permitido - 3/3)
Saque 4: R$ 100.00  ❌ (Negado - Limite diário atingido)
```

### **Teste de Vinculação Conta-Cliente:**

```python
# Cenário: Criar conta sem cliente cadastrado.
CPF informado: 11111111111
Cliente existe? ❌
Resultado: "Cliente não encontrado, fluxo encerrado!"
```

## 📚 Tecnologias e Bibliotecas

- **Python 3.6+** - Linguagem principal;
- **textwrap** - Formatação de texto e menu;
- **Funções built-in**: `filter()`, `input()`, `print()`, `len()`;
- **Estruturas nativas**: `list`, `dict`, `str`, `float`, `int`;
- **Programação funcional** - Funções como cidadãos de primeira classe.

## 🎯 Objetivos do Desafio v2.0

Esta versão avançada visa desenvolver:

- **Programação funcional** com parâmetros especializados;
- **Modularização** e reutilização de código;
- **Gestão de dados** com estruturas complexas;
- **Validação robusta** de entrada do usuário;
- **Interface profissional** e organizada;
- **Escalabilidade** para sistemas maiores.

## 🏆 Evolução do Projeto

### **v1.0 → v2.0:**

- 🔄 **3 funções** → **9 funções especializadas**;
- 🔄 **Operações básicas** → **Sistema completo de gestão**;
- 🔄 **Usuário único** → **Múltiplos clientes e contas**;
- 🔄 **Interface simples** → **Menu profissional com textwrap**;
- 🔄 **Validação básica** → **Validação robusta e flexível**.

---

**Desenvolvido como parte do Desafio DIO + Santander 2025** 🚀

#### Sistema Bancário v2.0 - Otimizado com Funções Python
