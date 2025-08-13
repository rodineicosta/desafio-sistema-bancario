# 🏦 Sistema Bancário em Python - Versão 4.0 (Avançado)

## 📖 Descrição do Projeto

Este projeto é parte do desafio **Sistema Bancário com Python**, da Formação **Santander 2025 - Back-End com Python**. A **Versão 4.0** implementa funcionalidades avançadas como **decoradores**, **geradores** e **iteradores**, mantendo toda a arquitetura POO da versão anterior.

A **Versão 4.0** adiciona recursos avançados de Python como logging automático de transações, relatórios inteligentes com filtros, e iteração personalizada sobre as contas do banco.

## ⚡ Funcionalidades

### 🔹 Operações Disponíveis

- **[1] Depositar**: Permite realizar depósitos na conta
- **[2] Sacar**: Permite realizar saques com limitações de segurança
- **[3] Visualizar Extrato**: Exibe histórico de transações e saldo atual
- **[4] Nova Conta**: Cria nova conta vinculada a um cliente
- **[5] Novo Cliente**: Cadastra novo cliente no sistema
- **[6] Listar Contas**: Exibe todas as contas cadastradas usando iterador personalizado
- **[7] Listar Clientes**: Exibe todos os clientes cadastrados
- **[8] Relatório de Transações**: Gera relatórios filtrados usando geradores
- **[0] Sair**: Encerra o sistema

### 🚀 Funcionalidades Avançadas

#### 🎯 **Decorador de Log**

- **Função**: Registra automaticamente data/hora de todas as transações;
- **Aplicação**: Todas as funções de transação (depósito, saque, criação de conta, etc.);
- **Formato**: `🕒 [DD/MM/AAAA HH:MM:SS] Executando 'Nome da Operação'`.

#### 🔄 **Gerador de Relatórios**

- **Função**: Permite iterar sobre transações com filtros específicos;
- **Filtros Disponíveis**:
  - Todas as transações;
  - Apenas depósitos;
  - Apenas saques;
  - Transações por data específica.
- **Vantagem**: Economia de memória com lazy evaluation.

#### 🔍 **Iterador Personalizado**

- **Classe**: `ContaIterador`;
- **Função**: Itera sobre todas as contas retornando dados estruturados;
- **Dados Retornados**: agência, número, titular, saldo, tipo de conta;
- **Uso**: Sistema de listagem de contas otimizado.

## 🚀 Tecnologias Utilizadas

- **Python 3.8+**;
- **ABC (Abstract Base Classes)** - Para classes abstratas;
- **datetime** - Para timestamps das transações;
- **textwrap** - Para formatação do menu;
- **functools** - Para manutenção da identidade original da função decorada;
- **POO** - Programação Orientada a Objetos;
- **Type Hints** - Para melhor documentação do código.

## 📋 Pré-requisitos

- Python 3.8 ou superior;
- Conhecimento básico de POO;
- Terminal/Prompt de comando.

## 🔧 Como Executar

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/rodineicosta/desafio-sistema-bancario.git
cd desafio-sistema-bancario
```

### 2️⃣ Execute o sistema

```bash
python desafio.py
```

## 💡 Como Usar

### 🔸 Fluxo Recomendado

1. **Criar Cliente**: Use `[5]` para cadastrar um novo cliente;
2. **Criar Conta**: Use `[4]` para criar conta vinculada ao cliente;
3. **Realizar Depósito**: Use `[1]` para adicionar fundos;
4. **Realizar Saques**: Use `[2]` para sacar dinheiro;
5. **Verificar Extrato**: Use `[3]` para ver movimentações;
6. **Relatório de Transações**: Use `[8]` para ver relatórios.

### 🔸 Exemplo de Uso Completo

```
```text
================ MENU ================
[1]    Depositar
[2]    Sacar
[3]    Extrato
[4]    Nova Conta
[5]    Novo Cliente
[6]    Listar Contas
[7]    Listar Clientes
[8]    Relatório de Transações
[0]    Sair
=> 5

Informe o CPF: 12345678901
Informe o nome completo: João Silva
Informe a data de nascimento (dd/mm/aaaa): 01/01/1990
Informe o endereço: Rua A, 123 - Centro - São Paulo/SP

=== Cliente criado com sucesso! ===
```

## 🔄 Evolução do Projeto

### v1.0 - Sistema Básico

- Funções simples;
- Operações básicas;
- Uma única conta.

### v2.0 - Sistema com Funções

- Funções especializadas;
- Múltiplos clientes e contas;
- Argumentos tipados (positional/keyword-only).

### v3.0 - Sistema POO

- Classes e objetos;
- Herança e polimorfismo;
- Classes abstratas;
- Encapsulamento.

### v4.0 - Sistema com Decoradores, Geradores e Iteradores

- Decorador de log;
- Gerador de relatório;
- Iterador personalizado.

## 🤝 Contribuição

1. Faça um fork do projeto;
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`);
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`);
4. Push para a branch (`git push origin feature/AmazingFeature`);
5. Abra um Pull Request.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Rodinei Costa**

- DIO: [Rodinei Costa](https://www.dio.me/users/rodineicosta);
- GitHub: [@rodineicosta](https://github.com/rodineicosta);
- LinkedIn: [Rodinei Costa](https://linkedin.com/in/rodineicosta).

## 🎓 Reconhecimentos

- **DIO (Digital Innovation One)** - Plataforma de ensino;
- **Santander 2025** - Programa de formação;
- **Python Software Foundation** - Linguagem Python.

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela!** ⭐

- ✅ **Vinculação obrigatória** conta-cliente;
- ✅ **Limites de saque** rigorosamente controlados;
- ✅ **Entrada flexível** com validação robusta.

## 🔧 Recursos Implementados na v3.0

Para acompanhar a evolução do desafio da versão anterior, veja o arquivo [README v3](https://github.com/rodineicosta/desafio-sistema-bancario/blob/v3/README.md) para mais detalhes.

---

### 🚀 Desenvolvido como parte do Desafio DIO + Santander 2025

Sistema Bancário v4.0 - Implementado com Decoradores, Geradores e Iteradores com Python
