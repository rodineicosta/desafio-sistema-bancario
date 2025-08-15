# 🏦 Sistema Bancário em Python - Versão 5 (DB API)

## 📖 Descrição do Projeto

Este projeto é parte do desafio **Banco de Dados**, da Formação **Santander 2025 - Back-End com Python**. A **Versão 5** implementa o gerencimento de cadastro de clientes Pessoa Física e Pessoa Jurídica através de um banco de dados SQLIte, mantendo todas as funcionalidades da versão anterior.

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
- **[9] Sistema de Clientes (BD)**: Gera relatórios filtrados usando geradores
- **[0] Sair**: Encerra o sistema

### 🗃️ Estrutura do Banco de Dados

#### Tabela: `pessoas_fisicas`

```sql
CREATE TABLE pessoas_fisicas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    data_nascimento TEXT NOT NULL,
    endereco TEXT NOT NULL,
    telefone TEXT,
    email TEXT,
    data_cadastro TEXT NOT NULL,
    ativo BOOLEAN DEFAULT 1
);
```

#### Tabela: `pessoas_juridicas`

```sql
CREATE TABLE pessoas_juridicas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    razao_social TEXT NOT NULL,
    nome_fantasia TEXT,
    cnpj TEXT UNIQUE NOT NULL,
    endereco TEXT NOT NULL,
    telefone TEXT,
    email TEXT,
    representante_legal TEXT NOT NULL,
    data_cadastro TEXT NOT NULL,
    ativo BOOLEAN DEFAULT 1
);
```

### 🚀 Funcionalidades Avançadas

### ✅ **Validação de Documentos**

- **CPF**: Validação completa usando algoritmo oficial;
- **CNPJ**: Validação completa usando algoritmo oficial;
- **Formatação automática**: XXX.XXX.XXX-XX e XX.XXX.XXX/XXXX-XX.

### 💾 **Operações CRUD**

- ✅ **Create**: Inserir novos clientes (PF e PJ);
- ✅ **Read**: Listar e buscar clientes;
- ✅ **Update**: Preparado para futuras expansões;
- ✅ **Delete**: Soft delete (marcar como inativo).

### 🔍 **Busca e Listagem**

- **Listar por tipo**: Pessoas físicas ou jurídicas separadamente;
- **Listar todos**: Visão consolidada de todos os clientes;
- **Busca por documento**: CPF ou CNPJ;
- **Ordenação**: Alfabética por nome/razão social.

### 📊 **Estatísticas**

- **Contadores**: Total de PF, PJ e geral;
- **Relatórios**: Informações do sistema.

## 🔧 Como Executar

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/rodineicosta/desafio-sistema-bancario.git
cd desafio-sistema-bancario
```

### 2️⃣ Execução Independente

```bash
python sistema_clientes.py
```

### 3️⃣ Integrado ao Sistema Bancário

```bash
python desafio.py
# Escolher opção [9] Sistema de Clientes (BD).
```

### 4️⃣ Executar Testes

```bash
python teste_database.py
```

## 📋 Menu do Novo Sistema de Clientes (BD)

```
================ SISTEMA DE CLIENTES ================
[1]    Cadastrar Pessoa Física
[2]    Cadastrar Pessoa Jurídica
[3]    Listar Pessoas Físicas
[4]    Listar Pessoas Jurídicas
[5]    Listar Todos os Clientes
[6]    Buscar Cliente por Documento
[7]    Estatísticas do Sistema
[8]    Voltar ao Menu Principal
[0]    Sair
```

## 🧪 Exemplos de Uso

### **Cadastro de Pessoa Física**

```
Nome completo: João da Silva
CPF: 123.456.789-09
Data de nascimento: 15/03/1985
Endereço: Rua das Flores, 123 - São Paulo/SP
Telefone: (11) 99999-9999
E-mail: joao@email.com
```

### **Cadastro de Pessoa Jurídica**

```
Razão Social: Empresa ABC Ltda
Nome Fantasia: ABC Tech
CNPJ: 12.345.678/0001-95
Endereço: Av. Paulista, 1000 - São Paulo/SP
Representante Legal: Maria Santos
Telefone: (11) 3333-3333
E-mail: contato@abc.com
```

## 🔒 Validações Implementadas

### **CPF**

- ✅ Formato numérico (11 dígitos);
- ✅ Dígitos verificadores corretos;
- ✅ Rejeição de sequências repetidas;
- ✅ Unicidade no banco de dados.

### **CNPJ**

- ✅ Formato numérico (14 dígitos);
- ✅ Dígitos verificadores corretos;
- ✅ Rejeição de sequências repetidas;
- ✅ Unicidade no banco de dados.

### **Campos Obrigatórios**

- **PF**: Nome, CPF, Data de Nascimento, Endereço;
- **PJ**: Razão Social, CNPJ, Endereço, Representante Legal.

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **SQLite3** (banco de dados);
- **Regex** (validação de entrada);
- **Pathlib** (manipulação de caminhos);
- **Datetime** (timestamps);
- **Textwrap** (formatação de saída).

## 📈 Benefícios

### **Para o Banco**

- ✅ **Integridade de dados** garantida;
- ✅ **Validação automática** de documentos;
- ✅ **Histórico completo** de cadastros;
- ✅ **Busca eficiente** por clientes;
- ✅ **Relatórios estatísticos** instantâneos.

### **Para os Usuários**

- ✅ **Interface intuitiva** e organizada;
- ✅ **Feedback claro** em todas as operações;
- ✅ **Validação em tempo real**;
- ✅ **Formatação automática** de documentos;
- ✅ **Navegação simples** entre funcionalidades.

## 🎯 Integração com Sistema Bancário Existente

O sistema de clientes está **perfeitamente integrado** ao sistema bancário principal:

1. **Acesso via menu principal** (opção 9);
2. **Retorno automático** ao menu bancário;
3. **Compartilhamento de dados** (preparado para futuras integrações);
4. **Consistência visual** e de funcionalidades.

---

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

### v4.2 - Registro de transações em arquivo de log

- Cria arquivo `log.txt`;
- Registra transação com data em formato UTC, nome da função, argumentos e retorno;
- Mantidas todas as funcionalidades da v4.1.

### v4.3 - Gerenciamento de Pacotes, Convenções e Boas Práticas Python

- Ordenamento correto das importações;
- Espaçamentos entre linhas;
- Limite máximo de caracteres por linha;
- Mantidas todas as funcionalidades da v4.2.


### v5 - Banco de Dados

- Banco de dados SQLite criado com tabelas para PF e PJ;
- Inserção de dados com validação completa;
- Listagem categorizada de clientes;
- Validação de CPF/CNPJ usando algoritmos oficiais;
- Interface intuitiva com feedback claro;
- Mantidas todas as funcionalidades da v4.3.

---

## 📚 Conceitos Demonstrados

### Banco de Dados

- **Arquivo**: Criação de arquivo para armazenamento das informações;
- **Tabelas**: Criação de tabelas para cadastro de PF e PJ;
- **Validação**: Garantia de unicidade dos campos CPF e CNPJ, com validação;
- **Consultas**: Listagem de clientes por documento, por categoria e geral.

### Python Avançado

- **Decorators**: `@log_transacao` com `@functools.wraps`;
- **Generators**: `yield` para eficiência de memória;
- **Iterators**: Protocolo `__iter__` e `__next__`;
- **Representação**: `__repr__` para definir a representação em string de um objeto;
- **Arquivos**: `pathlib`, `with`, `open()` e `write()` para manipulação de arquivos;
- **Convenções**: Utilizações de pacotes:
  - `flake8` para verificações;
  - `isort` para ordenação de importações;
  - `black` para formatação de código.

### Data/Hora

- **datetime.now()**: *Timestamps* automáticos;
- **datetime.now(UTC)**: *Timestamps* em formato *Coordinated Universal Time*;
- **strftime()**: Formatação personalizada;
- **Comparação de datas**: Filtragem por período.

### POO

- **Herança**: Classes base abstratas;
- **Polimorfismo**: Transações especializadas;
- **Encapsulamento**: Dados protegidos.

---

## 🎯 Objetivos Alcançados

- ✅ **Implementação completa** do desafio "Banco de Dados";
- ✅ **Criação de arquivo** de de banco de dados para armazenamento de informações;
- ✅ **Inclusão de registros** em tabelas separadas por categoria, com validação de dados;
- ✅ **Recuperação de informações** detalhadas por consultas ao banco de dados;
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

## 🔧 Recursos Implementados na v4.3

Para acompanhar a evolução do desafio da versão anterior, veja o arquivo [README v4.3](https://github.com/rodineicosta/desafio-sistema-bancario/blob/v4.3/boas-praticas/README.md) para mais detalhes.

---

### 🚀 Desenvolvido como parte do Desafio DIO + Santander 2025

Sistema Bancário v5 (DB API) - Banco de Dados com Python
