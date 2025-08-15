import textwrap
from database import DatabaseManager


class SistemaClientes:
    """Sistema principal de gerenciamento de clientes."""

    def __init__(self):
        self.db = DatabaseManager()

    def exibir_menu(self):
        """Exibe o menu principal do sistema."""
        menu_texto = """\n
================ SISTEMA DE CLIENTES ================
[1]\tCadastrar Pessoa Física
[2]\tCadastrar Pessoa Jurídica
[3]\tListar Pessoas Físicas
[4]\tListar Pessoas Jurídicas
[5]\tListar Todos os Clientes
[6]\tBuscar Cliente por Documento
[7]\tEstatísticas do Sistema
[8]\tVoltar ao Menu Principal
[0]\tSair
=> """
        return input(textwrap.dedent(menu_texto))

    def cadastrar_pessoa_fisica(self):
        """Cadastra uma nova pessoa física."""
        print("\n" + "="*50)
        print("         CADASTRO DE PESSOA FÍSICA")
        print("="*50)

        try:
            nome = input("Nome completo: ").strip()
            if not nome:
                print("❌ Nome é obrigatório!")
                return

            cpf = input("CPF (apenas números ou com formatação): ").strip()
            if not cpf:
                print("❌ CPF é obrigatório!")
                return

            data_nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
            if not data_nascimento:
                print("❌ Data de nascimento é obrigatória!")
                return

            endereco = input("Endereço completo: ").strip()
            if not endereco:
                print("❌ Endereço é obrigatório!")
                return

            telefone = input("Telefone (opcional): ").strip()
            email = input("E-mail (opcional): ").strip()

            dados = {
                'nome': nome,
                'cpf': cpf,
                'data_nascimento': data_nascimento,
                'endereco': endereco,
                'telefone': telefone,
                'email': email
            }

            self.db.inserir_pessoa_fisica(dados)

        except KeyboardInterrupt:
            print("\n❌ Operação cancelada pelo usuário.")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")

    def cadastrar_pessoa_juridica(self):
        """Cadastra uma nova pessoa jurídica."""
        print("\n" + "="*50)
        print("        CADASTRO DE PESSOA JURÍDICA")
        print("="*50)

        try:
            razao_social = input("Razão Social: ").strip()
            if not razao_social:
                print("❌ Razão Social é obrigatória!")
                return

            nome_fantasia = input("Nome Fantasia (opcional): ").strip()

            cnpj = input("CNPJ (apenas números ou com formatação): ").strip()
            if not cnpj:
                print("❌ CNPJ é obrigatório!")
                return

            endereco = input("Endereço completo: ").strip()
            if not endereco:
                print("❌ Endereço é obrigatório!")
                return

            representante_legal = input("Representante Legal: ").strip()
            if not representante_legal:
                print("❌ Representante Legal é obrigatório!")
                return

            telefone = input("Telefone (opcional): ").strip()
            email = input("E-mail (opcional): ").strip()

            dados = {
                'razao_social': razao_social,
                'nome_fantasia': nome_fantasia,
                'cnpj': cnpj,
                'endereco': endereco,
                'representante_legal': representante_legal,
                'telefone': telefone,
                'email': email
            }

            self.db.inserir_pessoa_juridica(dados)

        except KeyboardInterrupt:
            print("\n❌ Operação cancelada pelo usuário.")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")

    def listar_pessoas_fisicas(self):
        """Lista todas as pessoas físicas cadastradas."""
        print("\n" + "="*80)
        print("                        PESSOAS FÍSICAS CADASTRADAS")
        print("="*80)

        clientes = self.db.listar_pessoas_fisicas()

        if not clientes:
            print("📋 Nenhuma pessoa física cadastrada.")
            return

        for i, cliente in enumerate(clientes, 1):
            cpf_formatado = self.db.formatar_cpf(cliente['cpf'])

            info = f"""\
            [{i:2d}] Nome:\t\t{cliente['nome']}
                 CPF:\t\t{cpf_formatado}
                 Data Nasc.:\t{cliente['data_nascimento']}
                 Endereço:\t{cliente['endereco']}
                 Telefone:\t{cliente['telefone'] or 'Não informado'}
                 E-mail:\t\t{cliente['email'] or 'Não informado'}
                 Cadastro:\t{cliente['data_cadastro']}
            """
            print(textwrap.dedent(info))
            print("-" * 80)

        print(f"📊 Total: {len(clientes)} pessoa(s) física(s) cadastrada(s)")

    def listar_pessoas_juridicas(self):
        """Lista todas as pessoas jurídicas cadastradas."""
        print("\n" + "="*80)
        print("                       PESSOAS JURÍDICAS CADASTRADAS")
        print("="*80)

        clientes = self.db.listar_pessoas_juridicas()

        if not clientes:
            print("📋 Nenhuma pessoa jurídica cadastrada.")
            return

        for i, cliente in enumerate(clientes, 1):
            cnpj_formatado = self.db.formatar_cnpj(cliente['cnpj'])

            info = f"""\
            [{i:2d}] Razão Social:\t{cliente['razao_social']}
                 Nome Fantasia:\t{cliente['nome_fantasia'] or 'Não informado'}
                 CNPJ:\t\t{cnpj_formatado}
                 Endereço:\t{cliente['endereco']}
                 Repr. Legal:\t{cliente['representante_legal']}
                 Telefone:\t{cliente['telefone'] or 'Não informado'}
                 E-mail:\t\t{cliente['email'] or 'Não informado'}
                 Cadastro:\t{cliente['data_cadastro']}
            """
            print(textwrap.dedent(info))
            print("-" * 80)

        print(f"📊 Total: {len(clientes)} pessoa(s) jurídica(s) cadastrada(s)")

    def listar_todos_clientes(self):
        """Lista todos os clientes (PF e PJ) organizadamente."""
        print("\n" + "="*80)
        print("                          TODOS OS CLIENTES")
        print("="*80)

        # Listar pessoas físicas.
        pf_clientes = self.db.listar_pessoas_fisicas()
        pj_clientes = self.db.listar_pessoas_juridicas()

        if not pf_clientes and not pj_clientes:
            print("📋 Nenhum cliente cadastrado.")
            return

        # Exibir pessoas físicas.
        if pf_clientes:
            print("\n👤 PESSOAS FÍSICAS:")
            print("─" * 80)
            for cliente in pf_clientes:
                cpf_formatado = self.db.formatar_cpf(cliente['cpf'])
                print(f"  • {cliente['nome']} - CPF: {cpf_formatado}")

        # Exibir pessoas jurídicas.
        if pj_clientes:
            print("\n🏢 PESSOAS JURÍDICAS:")
            print("─" * 80)
            for cliente in pj_clientes:
                cnpj_formatado = self.db.formatar_cnpj(cliente['cnpj'])
                nome_exibicao = cliente['nome_fantasia'] or cliente['razao_social']
                print(f"  • {nome_exibicao} - CNPJ: {cnpj_formatado}")

        print("\n" + "─" * 80)
        print(f"📊 Total: {len(pf_clientes)} PF + {len(pj_clientes)} PJ = "
              f"{len(pf_clientes) + len(pj_clientes)} cliente(s)")

    def buscar_cliente(self):
        """Busca cliente por CPF ou CNPJ."""
        print("\n" + "="*50)
        print("           BUSCAR CLIENTE")
        print("="*50)

        documento = input("Informe CPF ou CNPJ: ").strip()
        if not documento:
            print("❌ Documento é obrigatório!")
            return

        cliente = self.db.buscar_cliente_por_documento(documento)

        if not cliente:
            print("❌ Cliente não encontrado!")
            return

        print("\n✅ Cliente encontrado:")
        print("="*50)

        if cliente['tipo'] == 'PF':
            cpf_formatado = self.db.formatar_cpf(cliente['cpf'])
            info = f"""\
            Tipo:\t\t👤 Pessoa Física
            Nome:\t\t{cliente['nome']}
            CPF:\t\t{cpf_formatado}
            Data Nasc.:\t{cliente['data_nascimento']}
            Endereço:\t{cliente['endereco']}
            Telefone:\t{cliente['telefone'] or 'Não informado'}
            E-mail:\t\t{cliente['email'] or 'Não informado'}
            Cadastro:\t{cliente['data_cadastro']}
            """
        else:  # PJ.
            cnpj_formatado = self.db.formatar_cnpj(cliente['cnpj'])
            info = f"""\
            Tipo:\t\t🏢 Pessoa Jurídica
            Razão Social:\t{cliente['razao_social']}
            Nome Fantasia:\t{cliente['nome_fantasia'] or 'Não informado'}
            CNPJ:\t\t{cnpj_formatado}
            Endereço:\t{cliente['endereco']}
            Repr. Legal:\t{cliente['representante_legal']}
            Telefone:\t{cliente['telefone'] or 'Não informado'}
            E-mail:\t\t{cliente['email'] or 'Não informado'}
            Cadastro:\t{cliente['data_cadastro']}
            """

        print(textwrap.dedent(info))

    def exibir_estatisticas(self):
        """Exibe estatísticas do sistema."""
        print("\n" + "="*50)
        print("        ESTATÍSTICAS DO SISTEMA")
        print("="*50)

        stats = self.db.obter_estatisticas()

        info = f"""\
        👤 Pessoas Físicas:\t{stats['pessoas_fisicas']:>5}
        🏢 Pessoas Jurídicas:\t{stats['pessoas_juridicas']:>5}
        ──────────────────────────────
        📊 Total de Clientes:\t{stats['total']:>5}
        """

        print(textwrap.dedent(info))

        # Informações do banco de dados.
        print(f"💾 Banco de dados: {self.db.db_path}")
        print(f"📅 Sistema ativo desde: início da sessão")

    def executar(self):
        """Executa o sistema principal."""
        print("🎉 Sistema de Gerenciamento de Clientes Inicializado!")

        while True:
            try:
                opcao = self.exibir_menu()

                if opcao == "1":
                    self.cadastrar_pessoa_fisica()

                elif opcao == "2":
                    self.cadastrar_pessoa_juridica()

                elif opcao == "3":
                    self.listar_pessoas_fisicas()

                elif opcao == "4":
                    self.listar_pessoas_juridicas()

                elif opcao == "5":
                    self.listar_todos_clientes()

                elif opcao == "6":
                    self.buscar_cliente()

                elif opcao == "7":
                    self.exibir_estatisticas()

                elif opcao == "8":
                    print("↩️  Voltando ao menu principal...")
                    break

                elif opcao == "0":
                    print("👋 Encerrando sistema de clientes...")
                    return False  # Indica para encerrar tudo.

                else:
                    print("❌ Opção inválida! Tente novamente.")

            except KeyboardInterrupt:
                print("\n👋 Sistema encerrado pelo usuário.")
                break
            except Exception as e:
                print(f"❌ Erro inesperado: {e}")

        return True  # Indica para voltar ao menu principal.


def main():
    """Função principal para teste independente."""
    sistema = SistemaClientes()
    sistema.executar()


if __name__ == "__main__":
    main()
