import database

# Função para inserir dados na tabela de anamneses
def inserir_anamnese(paciente_id, queixa_principal, historia_doenca_atual, historia_medica_pregressa,
                      historico_familiar, historico_cirurgico, medicamentos, alimentacao, exercicio,
                      moradia, trabalho):
    """
    Insere os dados de anamnese na tabela 'anamneses'.
    """
    try:
        database.execute_query('''INSERT INTO anamneses (paciente_id, queixa_principal, historia_doenca_atual,
                                                      historia_medica_pregressa, historico_familiar,
                                                      historico_cirurgico, medicamentos, alimentacao, exercicio,
                                                      moradia, trabalho)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                                (paciente_id, queixa_principal, historia_doenca_atual, historia_medica_pregressa,
                                 historico_familiar, historico_cirurgico, medicamentos, alimentacao, exercicio, moradia, trabalho))
    except Exception as e:
        print(f"Erro ao inserir anamnese: {e}")
        raise

# Função para buscar dados de anamnese para um paciente específico
def buscar_anamnese(paciente_id):
    """
    Busca as informações de anamnese de um paciente específico pelo seu ID.
    """
    try:
        dados = database.fetch_one('''
            SELECT p.nome, p.idade, p.sexo, p.profissao, p.estado_civil, p.endereco,
                   COALESCE(a.queixa_principal, ''), COALESCE(a.historia_doenca_atual, ''),
                   COALESCE(a.historia_medica_pregressa, ''), 		
                   COALESCE(a.historico_familiar, ''),
                   COALESCE(a.historico_cirurgico, ''), COALESCE(a.medicamentos, ''),
                   COALESCE(a.alimentacao, ''), COALESCE(a.exercicio, ''),
                   COALESCE(a.moradia, ''), COALESCE(a.trabalho, '')
            FROM pacientes p
            LEFT JOIN anamneses a ON p.id = a.paciente_id
            WHERE p.id = ?
        ''', (paciente_id,))
        return dados
    except Exception as e:
        print(f"Erro ao buscar anamnese: {e}")
        raise

# Função para buscar todas as anamneses
def buscar_todas_anamneses():
    """
    Busca todas as anamneses de todos os pacientes.
    """
    try:
        dados = database.fetch_all('''
            SELECT p.nome, p.idade, p.sexo, p.profissao, p.estado_civil, p.endereco,
                   COALESCE(a.queixa_principal, ''), COALESCE(a.historia_doenca_atual, ''),
                   COALESCE(a.historia_medica_pregressa, ''), 		
                   COALESCE(a.historico_familiar, ''),
                   COALESCE(a.historico_cirurgico, ''), COALESCE(a.medicamentos, ''),
                   COALESCE(a.alimentacao, ''), COALESCE(a.exercicio, ''),
                   COALESCE(a.moradia, ''), COALESCE(a.trabalho, '')
            FROM pacientes p
            LEFT JOIN anamneses a ON p.id = a.paciente_id
        ''')
        return dados
    except Exception as e:
        print(f"Erro ao buscar todas as anamneses: {e}")
        raise

# Função para atualizar uma anamnese existente
def atualizar_anamnese(paciente_id, queixa_principal, historia_doenca_atual, historia_medica_pregressa,
                        historico_familiar, historico_cirurgico, medicamentos, alimentacao, exercicio,
                        moradia, trabalho):
    """
    Atualiza os dados de anamnese para um paciente específico.
    """
    try:
        database.execute_query('''UPDATE anamneses SET queixa_principal = ?, historia_doenca_atual = ?,
                                  historia_medica_pregressa = ?, historico_familiar = ?, 
                                  historico_cirurgico = ?, medicamentos = ?, alimentacao = ?, 
                                  exercicio = ?, moradia = ?, trabalho = ?
                                  WHERE paciente_id = ?''', 
                                  (queixa_principal, historia_doenca_atual, historia_medica_pregressa,
                                   historico_familiar, historico_cirurgico, medicamentos, alimentacao,
                                   exercicio, moradia, trabalho, paciente_id))
    except Exception as e:
        print(f"Erro ao atualizar anamnese: {e}")
        raise
