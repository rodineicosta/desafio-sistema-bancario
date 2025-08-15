import sqlite3
import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional

# Caminho do banco de dados.
DB_PATH = Path(__file__).parent / "banco_clientes.db"


class DatabaseManager:
    """Gerenciador de banco de dados para clientes."""

    def __init__(self):
        self.db_path = DB_PATH
        self.init_database()

    def init_database(self):
        """Inicializa o banco de dados e cria as tabelas."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()

                # Tabela para Pessoas Físicas.
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS pessoas_fisicas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        cpf TEXT UNIQUE NOT NULL,
                        data_nascimento TEXT NOT NULL,
                        endereco TEXT NOT NULL,
                        telefone TEXT,
                        email TEXT,
                        data_cadastro TEXT NOT NULL,
                        ativo BOOLEAN DEFAULT 1
                    )
                """)

                # Tabela para Pessoas Jurídicas.
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS pessoas_juridicas (
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
                    )
                """)

                conn.commit()
                print("✅ Banco de dados inicializado com sucesso!")

        except sqlite3.Error as e:
            print(f"❌ Erro ao inicializar banco de dados: {e}")

    def validar_cpf(self, cpf: str) -> bool:
        """Valida CPF usando algoritmo oficial."""
        # Remove caracteres não numéricos.
        cpf = re.sub(r'[^0-9]', '', cpf)

        # Verifica se tem 11 dígitos.
        if len(cpf) != 11:
            return False

        # Verifica se todos os dígitos são iguais.
        if cpf == cpf[0] * 11:
            return False

        # Calcula primeiro dígito verificador.
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = soma % 11
        digito1 = 0 if resto < 2 else 11 - resto

        # Calcula segundo dígito verificador.
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto

        # Verifica se os dígitos calculados coincidem.
        return cpf[-2:] == f"{digito1}{digito2}"

    def validar_cnpj(self, cnpj: str) -> bool:
        """Valida CNPJ usando algoritmo oficial."""
        # Remove caracteres não numéricos.
        cnpj = re.sub(r'[^0-9]', '', cnpj)

        # Verifica se tem 14 dígitos.
        if len(cnpj) != 14:
            return False

        # Verifica se todos os dígitos são iguais.
        if cnpj == cnpj[0] * 14:
            return False

        # Calcula primeiro dígito verificador.
        sequencia1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(cnpj[i]) * sequencia1[i] for i in range(12))
        resto = soma % 11
        digito1 = 0 if resto < 2 else 11 - resto

        # Calcula segundo dígito verificador.
        sequencia2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(cnpj[i]) * sequencia2[i] for i in range(13))
        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto

        # Verifica se os dígitos calculados coincidem.
        return cnpj[-2:] == f"{digito1}{digito2}"

    def inserir_pessoa_fisica(self, dados: Dict) -> bool:
        """Insere uma pessoa física no banco de dados."""
        try:
            # Validar CPF.
            cpf_limpo = re.sub(r'[^0-9]', '', dados['cpf'])
            if not self.validar_cpf(cpf_limpo):
                print("❌ CPF inválido!")
                return False

            # Verificar se CPF já existe.
            if self.cpf_existe(cpf_limpo):
                print("❌ CPF já cadastrado!")
                return False

            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO pessoas_fisicas
                    (nome, cpf, data_nascimento, endereco, telefone, email, data_cadastro)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    dados['nome'],
                    cpf_limpo,
                    dados['data_nascimento'],
                    dados['endereco'],
                    dados.get('telefone', ''),
                    dados.get('email', ''),
                    datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                ))
                conn.commit()
                print("✅ Pessoa física cadastrada com sucesso!")
                return True

        except sqlite3.IntegrityError:
            print("❌ Erro: CPF já cadastrado!")
            return False
        except sqlite3.Error as e:
            print(f"❌ Erro ao inserir pessoa física: {e}")
            return False

    def inserir_pessoa_juridica(self, dados: Dict) -> bool:
        """Insere uma pessoa jurídica no banco de dados."""
        try:
            # Validar CNPJ.
            cnpj_limpo = re.sub(r'[^0-9]', '', dados['cnpj'])
            if not self.validar_cnpj(cnpj_limpo):
                print("❌ CNPJ inválido!")
                return False

            # Verificar se CNPJ já existe.
            if self.cnpj_existe(cnpj_limpo):
                print("❌ CNPJ já cadastrado!")
                return False

            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO pessoas_juridicas
                    (razao_social, nome_fantasia, cnpj, endereco, telefone, email,
                     representante_legal, data_cadastro)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    dados['razao_social'],
                    dados.get('nome_fantasia', ''),
                    cnpj_limpo,
                    dados['endereco'],
                    dados.get('telefone', ''),
                    dados.get('email', ''),
                    dados['representante_legal'],
                    datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                ))
                conn.commit()
                print("✅ Pessoa jurídica cadastrada com sucesso!")
                return True

        except sqlite3.IntegrityError:
            print("❌ Erro: CNPJ já cadastrado!")
            return False
        except sqlite3.Error as e:
            print(f"❌ Erro ao inserir pessoa jurídica: {e}")
            return False

    def cpf_existe(self, cpf: str) -> bool:
        """Verifica se CPF já existe no banco."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 1 FROM pessoas_fisicas WHERE cpf = ?", (cpf,))
                return cursor.fetchone() is not None
        except sqlite3.Error:
            return False

    def cnpj_existe(self, cnpj: str) -> bool:
        """Verifica se CNPJ já existe no banco."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 1 FROM pessoas_juridicas WHERE cnpj = ?", (cnpj,))
                return cursor.fetchone() is not None
        except sqlite3.Error:
            return False

    def listar_pessoas_fisicas(self) -> List[Dict]:
        """Lista todas as pessoas físicas cadastradas."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id, nome, cpf, data_nascimento, endereco, telefone, email, data_cadastro
                    FROM pessoas_fisicas
                    WHERE ativo = 1
                    ORDER BY nome
                """)

                colunas = [desc[0] for desc in cursor.description]
                resultados = cursor.fetchall()

                return [dict(zip(colunas, row)) for row in resultados]

        except sqlite3.Error as e:
            print(f"❌ Erro ao listar pessoas físicas: {e}")
            return []

    def listar_pessoas_juridicas(self) -> List[Dict]:
        """Lista todas as pessoas jurídicas cadastradas."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id, razao_social, nome_fantasia, cnpj, endereco, telefone,
                           email, representante_legal, data_cadastro
                    FROM pessoas_juridicas
                    WHERE ativo = 1
                    ORDER BY razao_social
                """)

                colunas = [desc[0] for desc in cursor.description]
                resultados = cursor.fetchall()

                return [dict(zip(colunas, row)) for row in resultados]

        except sqlite3.Error as e:
            print(f"❌ Erro ao listar pessoas jurídicas: {e}")
            return []

    def buscar_cliente_por_documento(self, documento: str) -> Optional[Dict]:
        """Busca cliente por CPF ou CNPJ."""
        documento_limpo = re.sub(r'[^0-9]', '', documento)

        # Tentar buscar como CPF (11 dígitos).
        if len(documento_limpo) == 11:
            try:
                with sqlite3.connect(self.db_path) as conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        SELECT *, 'PF' as tipo FROM pessoas_fisicas
                        WHERE cpf = ? AND ativo = 1
                    """, (documento_limpo,))
                    resultado = cursor.fetchone()
                    if resultado:
                        colunas = [desc[0] for desc in cursor.description]
                        return dict(zip(colunas, resultado))
            except sqlite3.Error:
                pass

        # Tentar buscar como CNPJ (14 dígitos).
        elif len(documento_limpo) == 14:
            try:
                with sqlite3.connect(self.db_path) as conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        SELECT *, 'PJ' as tipo FROM pessoas_juridicas
                        WHERE cnpj = ? AND ativo = 1
                    """, (documento_limpo,))
                    resultado = cursor.fetchone()
                    if resultado:
                        colunas = [desc[0] for desc in cursor.description]
                        return dict(zip(colunas, resultado))
            except sqlite3.Error:
                pass

        return None

    def formatar_cpf(self, cpf: str) -> str:
        """Formata CPF para exibição."""
        if len(cpf) == 11:
            return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        return cpf

    def formatar_cnpj(self, cnpj: str) -> str:
        """Formata CNPJ para exibição."""
        if len(cnpj) == 14:
            return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
        return cnpj

    def obter_estatisticas(self) -> Dict:
        """Obtém estatísticas do banco de dados."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()

                # Contar pessoas físicas.
                cursor.execute("SELECT COUNT(*) FROM pessoas_fisicas WHERE ativo = 1")
                total_pf = cursor.fetchone()[0]

                # Contar pessoas jurídicas.
                cursor.execute("SELECT COUNT(*) FROM pessoas_juridicas WHERE ativo = 1")
                total_pj = cursor.fetchone()[0]

                return {
                    'pessoas_fisicas': total_pf,
                    'pessoas_juridicas': total_pj,
                    'total': total_pf + total_pj
                }

        except sqlite3.Error as e:
            print(f"❌ Erro ao obter estatísticas: {e}")
            return {'pessoas_fisicas': 0, 'pessoas_juridicas': 0, 'total': 0}
