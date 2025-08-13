# 🏦 Sistema Bancário em Python - Versão 3.0 (POO)

## 📖 Descrição do Projeto

Este projeto é parte do desafio **Modelando o Sistema Bancário em POO com Python**, da Formação **Santander 2025 - Back-End com Python**. O objetivo é atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários, seguindo o modelo de classes UML.

A **Versão 3.0** do sistema implementa uma arquitetura orientada a objetos com classes abstratas, herança, polimorfismo e encapsulamento, seguindo os princípios SOLID e as melhores práticas de POO em Python.

## ⚡ Funcionalidades

### 🔹 Operações Disponíveis

- **[1] Depositar**: Permite realizar depósitos na conta
- **[2] Sacar**: Permite realizar saques com limitações de segurança
- **[3] Visualizar Extrato**: Exibe histórico de transações e saldo atual
- **[4] Nova Conta**: Cria nova conta vinculada a um cliente
- **[5] Novo Cliente**: Cadastra novo cliente no sistema
- **[6] Listar Contas**: Exibe todas as contas cadastradas
- **[7] Listar Clientes**: Exibe todos os clientes cadastrados
- **[0] Sair**: Encerra o sistema

## 🏗️ Arquitetura POO

### 📦 Classes Implementadas

#### 👤 **Cliente** (Classe Base)

- **Responsabilidade**: Gerenciar dados e contas do cliente;
- **Atributos**: `endereco`, `contas`;
- **Métodos**: `realizar_transacao()`, `adicionar_conta()`.

#### 🏛️ **PessoaFisica** (Herda de Cliente)

- **Responsabilidade**: Especialização para clientes pessoa física;
- **Atributos**: `nome`, `data_nascimento`, `cpf`, `endereco`;
- **Herança**: Herda comportamentos de `Cliente`.

#### 💳 **Conta** (Classe Base)

- **Responsabilidade**: Gerenciar operações básicas da conta;
- **Atributos**: `_saldo`, `_numero`, `_agencia`, `_cliente`, `_historico`;
- **Métodos**: `sacar()`, `depositar()`, propriedades de acesso.

#### 🏦 **ContaCorrente** (Herda de Conta)

- **Responsabilidade**: Conta com limites específicos;
- **Atributos**: `_limite` (R$ 500), `_limite_saques` (3 por dia);
- **Métodos**: Sobrescreve `sacar()` com validações adicionais.

#### 📜 **Historico**

- **Responsabilidade**: Armazenar histórico de transações;
- **Atributos**: `_transacoes`;
- **Métodos**: `adicionar_transacao()`.

#### 🔄 **Transacao** (Classe Abstrata - ABC)

- **Responsabilidade**: Definir contrato para transações;
- **Métodos abstratos**: `valor` (property), `registrar()`;
- **Uso**: Base para `Deposito` e `Saque`.

#### 📈 **Deposito** (Herda de Transacao)

- **Responsabilidade**: Implementar operação de depósito;
- **Atributos**: `_valor`;
- **Métodos**: `registrar()` - executa depósito na conta.

#### 📉 **Saque** (Herda de Transacao)

- **Responsabilidade**: Implementar operação de saque;
- **Atributos**: `_valor`;
- **Métodos**: `registrar()` - executa saque na conta.

### 🎯 Princípios POO Aplicados

#### 🔐 **Encapsulamento**

```python
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0         # Atributo protegido.
        self._numero = numero   # Atributo protegido.

    @property
    def saldo(self):            # Acesso controlado via property.
        return self._saldo
```

#### 🧬 **Herança**

```python
class ContaCorrente(Conta):     # Herda de Conta.
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)  # Chama construtor da classe pai.
        self._limite = limite
```

#### 🎭 **Polimorfismo**

```python
def realizar_transacao(self, conta, transacao):
    transacao.registrar(conta)  # Funciona para Deposito ou Saque.
```

#### 🎨 **Abstração**

```python
class Transacao(ABC):
    @abstractproperty
    def valor(self):            # Método que deve ser implementado.
        pass

    @abstractclassmethod
    def registrar(self, conta): # Método que deve ser implementado.
        pass
```

### 🔒 Regras de Negócio

#### Depósitos

- ✅ Aceita apenas valores positivos;
- ✅ Não há limite de valor ou quantidade;
- ✅ Atualiza automaticamente o saldo e histórico;
- ✅ **Implementado via classe `Deposito`**.

#### Saques

- ✅ Aceita apenas valores positivos;
- ✅ Limite máximo de **R$ 500,00 por saque**;
- ✅ Limite de **3 saques diários**;
- ✅ Verificação de saldo suficiente;
- ✅ Alertas em caso de violação das regras;
- ✅ **Implementado via classe `Saque`**.

#### Visualização de Extrato

- ✅ Lista todas as movimentações com *timestamp*;
- ✅ Exibe saldo atual;
- ✅ Formatação monetária: **R$ xxx.xx**;
- ✅ Mensagem quando não há movimentações;
- ✅ **Implementado via classe `Historico`**.

#### Gestão de Clientes

- ✅ Cadastro com: **Nome, Data Nascimento, CPF, Endereço**;
- ✅ CPF único por cliente (validação automática);
- ✅ Filtros inteligentes para busca por CPF;
- ✅ **Implementado via classe `PessoaFisica`**.

#### Gestão de Contas

- ✅ Múltiplas contas por cliente;
- ✅ Agência padrão: **0001**;
- ✅ Numeração sequencial automática;
- ✅ Vinculação obrigatória com cliente existente;
- ✅ **Implementado via classe `ContaCorrente`**.

## 🚀 Tecnologias Utilizadas

- **Python 3.8+**;
- **ABC (Abstract Base Classes)** - Para classes abstratas;
- **datetime** - Para timestamps das transações;
- **textwrap** - Para formatação do menu;
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
5. **Verificar Extrato**: Use `[3]` para ver movimentações.

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

### v3.0 - Sistema POO (Atual)

- Classes e objetos;
- Herança e polimorfismo;
- Classes abstratas;
- Encapsulamento.

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

## 🔧 Recursos Implementados v2.0

Para acompanhar a evolução do desafio da versão anterior, veja o arquivo [README v2](https://github.com/rodineicosta/desafio-sistema-bancario/blob/v2/README.md) para mais detalhes.

---

**Desenvolvido como parte do Desafio DIO + Santander 2025** 🚀

### Sistema Bancário v3.0 - Otimizado com Programação Orientada a Objeto com Python
