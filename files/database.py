import sqlite3

def init_db():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            sexo TEXT NOT NULL,
            profissao TEXT NOT NULL,
            estado_civil TEXT NOT NULL,
            endereco TEXT NOT NULL
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS anamneses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            paciente_id INTEGER NOT NULL,
            queixa_principal TEXT NOT NULL,
            historia_doenca_atual TEXT NOT NULL,
            historia_medica_pregressa TEXT NOT NULL,
            historico_familiar TEXT NOT NULL,
            historico_cirurgico TEXT NOT NULL,
            medicamentos TEXT NOT NULL,
            alimentacao TEXT NOT NULL,
            exercicio TEXT NOT NULL,
            moradia TEXT NOT NULL,
            trabalho TEXT NOT NULL,
            FOREIGN KEY (paciente_id) REFERENCES pacientes (id)
        )
        ''')
        conn.commit()

def execute_query(query, params=()):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()

def fetch_one(query, params=()):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

def fetch_all(query, params=()):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
        
