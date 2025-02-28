import sqlite3
import sys

def init_db():
    try:
        with sqlite3.connect("anamnese.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS pacientes (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                idade INTEGER NOT NULL,
                                sexo TEXT NOT NULL,
                                profissao TEXT NOT NULL,
                                estado_civil TEXT NOT NULL,
                                endereco TEXT NOT NULL)''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS anamneses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    paciente_id INTEGER NOT NULL,
                    queixa_principal TEXT NOT NULL,
                    historia_doenca_atual TEXT NOT NULL,
                    historia_medica_pregressa TEXT NOT NULL,
                    historico_familiar TEXT NOT NULL,
                    historico_cirurgico TEXT,
                    medicamentos TEXT,
                    alimentacao TEXT,
                    exercicio TEXT,
                    moradia TEXT,
                    trabalho TEXT,
                    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (paciente_id) REFERENCES pacientes(id))''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS doctors (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT NOT NULL UNIQUE,
                                password TEXT NOT NULL)''')
            conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao inicializar o banco de dados: {e}", file=sys.stderr)

def execute_query(query, params=()):
    try:
        with sqlite3.connect("anamnese.db") as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao executar query: {e}", file=sys.stderr)

def fetch_one(query, params=()):
    try:
        with sqlite3.connect("anamnese.db") as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Erro ao executar query: {e}", file=sys.stderr)
        return None
