# 🏦 Sistema Bancário em Python - Versão 4.1

## 📖 Descrição do Projeto

Este projeto é parte do desafio **Lidando com Data, Hora e Fuso Horário no Python**, da Formação **Santander 2025 - Back-End com Python**. A **Versão 4.1** implementa o limite de dez (10) transações diárias para uma conta, com exibição de aviso sobre o referido limite excedido para o dia.

A exibição de data e hora no extrato já estava implementada nas versões anteriores ao desafio atual.

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

#### 🕐 **Gerenciamento de Data/Hora**

- **Timestamps automáticos**: Todas as transações recebem timestamp automático no formato `dd/mm/aaaa hh:mm:ss`;
- **Controle diário**: Sistema distingue transações por data para aplicar regras de negócio;
- **Extrato temporal**: Visualização cronológica de todas as operações.

#### 📊 **Limite de Transações Diárias**

- **10 transações por dia**: Substituição do antigo limite de 3 saques por um limite mais flexível;
- **Validação centralizada**: Controle realizado na classe `Cliente` via método `realizar_transacao()`;
- **Mensagens informativas**: Feedback claro sobre status das transações e limites.

#### 🎯 **Decorador de Log (@log_transacao)**

```python
@log_transacao
def registrar(self, conta):
    # Funcionalidade com log automático.
```

- **Função**: Registra automaticamente data/hora de todas as transações;
- **Aplicação**: Todas as funções de transação (depósito, saque, criação de conta, etc.);
- **Formato**: `🕒 [DD/MM/AAAA HH:MM:SS] Executando 'Nome da Operação'`.

#### 🔄 **Gerador de Relatórios (yield)**

```python
def gerar_relatorio(self):
    for transacao in self._transacoes:
        yield transacao

def transacoes_do_dia(self, data=None):
    for transacao in self._transacoes:
        if data_transacao == data_hoje:
            yield transacao
```

- **Função**: Permite iterar sobre transações com filtros específicos;
- **Filtros Disponíveis**:
  - Todas as transações;
  - Apenas depósitos;
  - Apenas saques;
  - Transações por data específica.
- **Vantagem**: Economia de memória com lazy evaluation.

#### 🔍 **Iterador Personalizado (ContaIterador)**

```python
# Permite iteração sobre contas com formatação personalizada.
for conta_info in ContaIterador(contas):
    print(conta_info)
```

- **Classe**: `ContaIterador`;
- **Função**: Itera sobre todas as contas retornando dados estruturados;
- **Dados Retornados**: agência, número, titular, saldo, tipo de conta;
- **Uso**: Sistema de listagem de contas otimizado.

## 🚀 Tecnologias Utilizadas

- **Python 3.8+**;
- **ABC (Abstract Base Classes)** - Para classes abstratas;
- **`datetime`** - Para manipulação de data/hora;
- **`textwrap`** - Para formatação do menu;
- **`functools`** - Para Decorators avançados;
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

### 3️⃣ Demonstração Completa

```bash
python demo_v4.py
```

### 4️⃣ Testes Automatizados

```bash
python teste_v4.py
```

## 💡 Como Usar

### 🔸 Fluxo Recomendado

1. **Criar Cliente**: Use `[5]` para cadastrar um novo cliente;
2. **Criar Conta**: Use `[4]` para criar conta vinculada ao cliente;
3. **Realizar Depósito**: Use `[1]` para adicionar fundos;
4. **Realizar Saques**: Use `[2]` para sacar dinheiro;
5. **Verificar Extrato**: Use `[3]` para ver movimentações;
6. **Relatório de Transações**: Use `[8]` para ver relatórios.

### 🔸 Exemplo de Uso

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

### v4.1 - Limite Flexível de Transações e Manipulação de Data e Hora

- Limite de 10 transações diárias;
- Implementado controle por data/hora;
- Centralizada validação no método `Cliente.realizar_transacao()`;
- Melhorado extrato com *timestamps* detalhados;
- Mantidas todas as funcionalidades v4.0 (decorators/generators/iterators).

---

## 📚 Conceitos Demonstrados

### Python Avançado

- **Decorators**: `@log_transacao` com `@functools.wraps`;
- **Generators**: `yield` para eficiência de memória;
- **Iterators**: Protocolo `__iter__` e `__next__`.

### Data/Hora

- **datetime.now()**: Timestamps automáticos;
- **strftime()**: Formatação personalizada;
- **Comparação de datas**: Filtragem por período.

### POO

- **Herança**: Classes base abstratas;
- **Polimorfismo**: Transações especializadas;
- **Encapsulamento**: Dados protegidos.

---

## 🎯 Objetivos Alcançados

- ✅ **Implementação completa** do desafio "Lidando com Data, Hora e Fuso Horário";
- ✅ **Limite flexível** de 10 transações diárias;
- ✅ **Controle temporal** preciso das operações;
- ✅ **Compatibilidade** com funcionalidades v4.0;
- ✅ **Código testado** e documentado;
- ✅ **Arquitetura escalável** para futuras expansões.

---

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

Sistema Bancário v4.1 - Lidando com Data, Hora e Fuso Horário no Python
