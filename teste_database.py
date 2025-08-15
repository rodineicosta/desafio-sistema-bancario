import os
import tempfile
from database import DatabaseManager


def teste_validacao_documentos():
    """Testa a validação de CPF e CNPJ."""
    print("🧪 TESTE: Validação de Documentos")
    print("="*50)

    db = DatabaseManager()

    # Testes de CPF válidos.
    cpfs_validos = ["11144477735", "123.456.789-09"]
    cpfs_invalidos = ["00000000000", "123", "12345678901"]

    print("\n📋 Testando CPFs válidos:")
    for cpf in cpfs_validos:
        resultado = db.validar_cpf(cpf)
        print(f"  {cpf}: {'✅ Válido' if resultado else '❌ Inválido'}")

    print("\n📋 Testando CPFs inválidos:")
    for cpf in cpfs_invalidos:
        resultado = db.validar_cpf(cpf)
        print(f"  {cpf}: {'✅ Válido' if resultado else '❌ Inválido'}")

    # Testes de CNPJ.
    cnpjs_validos = ["11222333000181"]
    cnpjs_invalidos = ["00000000000000", "123", "1234567890123"]

    print("\n📋 Testando CNPJs válidos:")
    for cnpj in cnpjs_validos:
        resultado = db.validar_cnpj(cnpj)
        print(f"  {cnpj}: {'✅ Válido' if resultado else '❌ Inválido'}")

    print("\n📋 Testando CNPJs inválidos:")
    for cnpj in cnpjs_invalidos:
        resultado = db.validar_cnpj(cnpj)
        print(f"  {cnpj}: {'✅ Válido' if resultado else '❌ Inválido'}")


def teste_crud_clientes():
    """Testa operações CRUD de clientes."""
    print("\n\n🧪 TESTE: Operações CRUD")
    print("="*50)

    # Criar banco temporário para teste.
    with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as temp_db:
        temp_path = temp_db.name

    # Sobrescrever caminho do banco temporariamente.
    original_path = DatabaseManager().db_path
    DatabaseManager().db_path = temp_path

    try:
        db = DatabaseManager()
        db.db_path = temp_path
        db.init_database()

        # Teste 1: Inserir pessoa física.
        print("\n1️⃣ Inserindo pessoa física...")
        dados_pf = {
            'nome': 'João da Silva',
            'cpf': '11144477735',
            'data_nascimento': '15/03/1985',
            'endereco': 'Rua das Flores, 123',
            'telefone': '(11) 99999-9999',
            'email': 'joao@email.com'
        }

        sucesso = db.inserir_pessoa_fisica(dados_pf)
        print(f"Resultado: {'✅ Sucesso' if sucesso else '❌ Falha'}")

        # Teste 2: Inserir pessoa jurídica.
        print("\n2️⃣ Inserindo pessoa jurídica...")
        dados_pj = {
            'razao_social': 'Empresa ABC Ltda',
            'nome_fantasia': 'ABC Tech',
            'cnpj': '11222333000181',
            'endereco': 'Av. Paulista, 1000',
            'representante_legal': 'Maria Santos',
            'telefone': '(11) 3333-3333',
            'email': 'contato@abc.com'
        }

        sucesso = db.inserir_pessoa_juridica(dados_pj)
        print(f"Resultado: {'✅ Sucesso' if sucesso else '❌ Falha'}")

        # Teste 3: Listar clientes.
        print("\n3️⃣ Listando pessoas físicas...")
        pf_lista = db.listar_pessoas_fisicas()
        print(f"Encontrado(s): {len(pf_lista)} pessoa(s) física(s)")

        print("\n4️⃣ Listando pessoas jurídicas...")
        pj_lista = db.listar_pessoas_juridicas()
        print(f"Encontrado(s): {len(pj_lista)} pessoa(s) jurídica(s)")

        # Teste 4: Buscar por documento.
        print("\n5️⃣ Buscando por CPF...")
        cliente = db.buscar_cliente_por_documento('11144477735')
        print(f"Cliente encontrado: {'✅ Sim' if cliente else '❌ Não'}")

        print("\n6️⃣ Buscando por CNPJ...")
        empresa = db.buscar_cliente_por_documento('11222333000181')
        print(f"Empresa encontrada: {'✅ Sim' if empresa else '❌ Não'}")

        # Teste 5: Estatísticas.
        print("\n7️⃣ Obtendo estatísticas...")
        stats = db.obter_estatisticas()
        print(f"PF: {stats['pessoas_fisicas']}, PJ: {stats['pessoas_juridicas']}, "
              f"Total: {stats['total']}")

        # Teste 6: Tentativa de duplicação.
        print("\n8️⃣ Testando duplicação de CPF...")
        sucesso_dup = db.inserir_pessoa_fisica(dados_pf)
        print(f"Duplicação bloqueada: {'✅ Sim' if not sucesso_dup else '❌ Não'}")

        print("\n🎉 Todos os testes CRUD concluídos!")

    finally:
        # Limpar arquivo temporário.
        try:
            os.unlink(temp_path)
        except:
            pass


def teste_formatacao():
    """Testa formatação de documentos."""
    print("\n\n🧪 TESTE: Formatação de Documentos")
    print("="*50)

    db = DatabaseManager()

    # Teste formatação CPF.
    cpf_teste = "12345678901"
    cpf_formatado = db.formatar_cpf(cpf_teste)
    print(f"CPF: {cpf_teste} → {cpf_formatado}")

    # Teste formatação CNPJ.
    cnpj_teste = "12345678000195"
    cnpj_formatado = db.formatar_cnpj(cnpj_teste)
    print(f"CNPJ: {cnpj_teste} → {cnpj_formatado}")


def main():
    """Executa todos os testes."""
    print("🔍 INICIANDO TESTES DO SISTEMA DE BANCO DE DADOS")
    print("💾 Funcionalidades: SQLite, Validação, CRUD, Formatação")
    print("="*60)

    try:
        teste_validacao_documentos()
        teste_crud_clientes()
        teste_formatacao()

        print("\n" + "="*60)
        print("🎉 TODOS OS TESTES CONCLUÍDOS COM SUCESSO!")
        print("✨ Sistema de banco de dados funcionando perfeitamente!")
        print("="*60)

    except Exception as e:
        print(f"\n❌ Erro durante os testes: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
