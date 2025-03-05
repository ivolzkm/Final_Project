import database

def limpar_banco():
    try:
        # Apagar todos os registros de cada tabela
        database.execute_query("DELETE FROM anamneses")
        database.execute_query("DELETE FROM pacientes")
        database.execute_query("DELETE FROM doctors")
        
        # Você também pode redefinir os IDs auto-incrementáveis, caso queira
        database.execute_query("DELETE FROM sqlite_sequence WHERE name='anamneses'")
        database.execute_query("DELETE FROM sqlite_sequence WHERE name='pacientes'")
        database.execute_query("DELETE FROM sqlite_sequence WHERE name='doctors'")
        
        print("Histórico do banco de dados limpo com sucesso.")
    except Exception as e:
        print(f"Erro ao limpar o banco de dados: {e}")

limpar_banco()
