from flask import Flask, render_template, request, redirect, url_for, session, abort
from werkzeug.security import generate_password_hash, check_password_hash
import database

app = Flask(__name__, static_folder='static')
app.secret_key = "uma_chave_secreta"  # Necessário para usar sessions

database.init_db()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/escolha_perfil', methods=['POST'])
def escolha_perfil():
    perfil = request.form.get('perfil')
    if perfil == 'doutor':
        return redirect(url_for('login'))
    elif perfil == 'paciente':
        return redirect(url_for('index'))
    else:
        return render_template('home.html', error="Escolha um perfil válido.")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        doctor = database.fetch_one("SELECT * FROM doctors WHERE username = ?", (username,))
        
        if doctor and check_password_hash(doctor[2], password):
            session['doctor_authenticated'] = True
            return redirect(url_for('pacientes'))
        else:
            return render_template('login.html', error="Credenciais inválidas.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()
        hashed_password = generate_password_hash(password)
        try:
            database.execute_query("INSERT INTO doctors (username, password) VALUES (?, ?)", (username, hashed_password))
            return redirect(url_for('login'))
        except Exception as e:
            return render_template('erro.html', mensagem=f"Erro ao salvar no banco de dados: {e}. Tente novamente.")
    return render_template('register.html')

@app.route('/escolha', methods=['GET', 'POST'])
def escolha():
    if request.method == 'POST':
        acao = request.form.get('acao')
        if acao == 'avaliacao':
            return redirect(url_for('nome_idade_sexo'))
        elif acao == 'aguardar':
            return render_template('aguardar.html')
    return render_template('escolha.html')

@app.route('/nome_idade_sexo', methods=['GET', 'POST'])
def nome_idade_sexo():
    if request.method == 'POST':
        session['nome'] = request.form.get('nome', '').strip()
        session['idade'] = request.form.get('idade', '').strip()
        session['sexo'] = request.form.get('sexo', '').strip()
        return redirect(url_for('profissao_estado_endereco'))
    return render_template('nome_idade_sexo.html', nome=session.get('nome', ''), idade=session.get('idade', ''), sexo=session.get('sexo', ''))

@app.route('/profissao_estado_endereco', methods=['GET', 'POST'])
def profissao_estado_endereco():
    if request.method == 'POST':
        session['profissao'] = request.form.get('profissao', '').strip()
        session['estado_civil'] = request.form.get('estado_civil', '').strip()
        session['endereco'] = request.form.get('endereco', '').strip()
        return redirect(url_for('queixa_principal'))
    return render_template('profissao_estado_endereco.html', profissao=session.get('profissao', ''), estado_civil=session.get('estado_civil', ''), endereco=session.get('endereco', ''))

@app.route('/queixa_principal', methods=['GET', 'POST'])
def queixa_principal():
    if request.method == 'POST':
        session['queixa_principal'] = request.form.get('queixa_principal', '').strip()
        return redirect(url_for('historia_doenca'))
    return render_template('queixa_principal.html', queixa_principal=session.get('queixa_principal', ''))

@app.route('/historia_doenca', methods=['GET', 'POST'])
def historia_doenca():
    if request.method == 'POST':
        session['historia_doenca'] = request.form.get('historia_doenca', '').strip()
        return redirect(url_for('evolucao_sintomas'))
    return render_template('historia_doenca.html', historia_doenca=session.get('historia_doenca', ''))

@app.route('/evolucao_sintomas', methods=['GET', 'POST'])
def evolucao_sintomas():
    if request.method == 'POST':
        session['evolucao_sintomas'] = request.form.get('evolucao_sintomas', '').strip()
        return redirect(url_for('doencas_preexistentes'))
    return render_template('evolucao_sintomas.html', evolucao_sintomas=session.get('evolucao_sintomas', ''))

@app.route('/doencas_preexistentes', methods=['GET', 'POST'])
def doencas_preexistentes():
    if request.method == 'POST':
        session['doencas_preexistentes'] = request.form.get('doencas_preexistentes', '').strip()
        return redirect(url_for('historico_cirurgico'))
    return render_template('doencas_preexistentes.html', doencas_preexistentes=session.get('doencas_preexistentes', ''))

@app.route('/historico_cirurgico', methods=['GET', 'POST'])
def historico_cirurgico():
    if request.method == 'POST':
        session['historico_cirurgico'] = request.form.get('historico_cirurgico', '').strip()
        return redirect(url_for('medicamentos'))
    return render_template('historico_cirurgico.html', historico_cirurgico=session.get('historico_cirurgico', ''))

@app.route('/medicamentos', methods=['GET', 'POST'])
def medicamentos():
    if request.method == 'POST':
        session['medicamentos'] = request.form.get('medicamentos', '').strip()
        return redirect(url_for('historico_familiar'))
    return render_template('medicamentos.html', medicamentos=session.get('medicamentos', ''))

@app.route('/historico_familiar', methods=['GET', 'POST'])
def historico_familiar():
    if request.method == 'POST':
        session['historico_familiar'] = request.form.get('historico_familiar', '').strip()
        return redirect(url_for('alimentacao'))
    return render_template('historico_familiar.html', historico_familiar=session.get('historico_familiar', ''))

@app.route('/alimentacao', methods=['GET', 'POST'])
def alimentacao():
    if request.method == 'POST':
        session['alimentacao'] = request.form.get('alimentacao', '').strip()
        return redirect(url_for('exercicio'))
    return render_template('alimentacao.html', alimentacao=session.get('alimentacao', ''))

@app.route('/exercicio', methods=['GET', 'POST'])
def exercicio():
    if request.method == 'POST':
        session['exercicio'] = request.form.get('exercicio', '').strip()
        return redirect(url_for('finalizar_registro'))
    return render_template('exercicio.html', exercicio=session.get('exercicio', ''))

@app.route('/finalizar_registro', methods=['GET', 'POST'])
def finalizar_registro():
    # Verificação dos dados da sessão
    if 'queixa_principal' not in session or 'nome' not in session or 'idade' not in session:
        return redirect(url_for('queixa_principal'))

    try:
        database.execute_query('''INSERT INTO pacientes (nome, idade, sexo, profissao, estado_civil, endereco)
                                  VALUES (?, ?, ?, ?, ?, ?)''',
                               (session['nome'], session['idade'], session['sexo'], session['profissao'],
                                session['estado_civil'], session['endereco']))
        paciente_id = database.fetch_one('SELECT last_insert_rowid()')[0]
        print(f"Paciente ID: {paciente_id}")  # Adicionando depuração

        database.execute_query('''INSERT INTO anamneses (paciente_id, queixa_principal, historia_doenca_atual,
                              historia_medica_pregressa, historico_familiar, historico_cirurgico, medicamentos,
                              alimentacao, exercicio)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                               (paciente_id, session['queixa_principal'], session['historia_doenca'],
                                session['doencas_preexistentes'], session['historico_familiar'],
                                session.get('historico_cirurgico', ''), session.get('medicamentos', ''),
                                session.get('alimentacao', ''), session.get('exercicio', '')))
        print(f"Paciente {paciente_id} salvo com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")  # Adicionando depuração
        return render_template('erro.html', mensagem=f"Erro ao salvar os dados: {e}. Tente novamente.")

    # Limpar a sessão após salvar os dados
    session.clear()
    return redirect(url_for('obrigado'))  # Redireciona para a página de agradecimento

@app.route('/erro')
def erro():
    mensagem = request.args.get('mensagem', 'Ocorreu um erro inesperado.')
    return render_template('erro.html', mensagem=mensagem)

@app.route('/obrigado')
def obrigado():
    return render_template('obrigado.html')

@app.route('/pacientes')
def pacientes():
    if 'doctor_authenticated' not in session or not session['doctor_authenticated']:
        abort(403)  # Garante que só médicos autenticados acessem

    try:
        lista_pacientes = database.fetch_all("SELECT id, nome, idade FROM pacientes")
        print(f"Lista de pacientes: {lista_pacientes}")
        return render_template('pacientes.html', pacientes=lista_pacientes)
    except Exception as e:
        print(f"Erro ao recuperar lista de pacientes: {e}")  # Adicionando depuração
        return render_template('erro.html', mensagem=f"Erro ao recuperar lista de pacientes: {e}")

@app.route('/relatorio/<int:paciente_id>')
def relatorio_paciente(paciente_id):
    if 'doctor_authenticated' not in session or not session['doctor_authenticated']:
        abort(403)  # Apenas médicos autenticados podem acessar

    try:
        dados = database.fetch_one('''
            SELECT p.nome, p.idade, p.sexo, p.profissao, p.estado_civil, p.endereco,
                   COALESCE(a.queixa_principal, ''), COALESCE(a.historia_doenca_atual, ''),
                   COALESCE(a.historia_medica_pregressa, ''), COALESCE(a.historico_familiar, ''),
                   COALESCE(a.historico_cirurgico, ''), COALESCE(a.medicamentos, ''),
                   COALESCE(a.alimentacao, ''), COALESCE(a.exercicio, '')
            FROM pacientes p
            LEFT JOIN anamneses a ON p.id = a.paciente_id
            WHERE p.id = ?
        ''', (paciente_id,))
        print(f"Dados do paciente {paciente_id}: {dados}")  # Adicionando depuração

        if not dados:
            return render_template('erro.html', mensagem="Nenhum dado encontrado para esse paciente.")

        return render_template('relatorio.html', **{
            'nome': dados[0], 'idade': dados[1], 'sexo': dados[2], 'profissao': dados[3],
            'estado_civil': dados[4], 'endereco': dados[5], 'queixa_principal': dados[6],
            'historia_doenca': dados[7], 'historia_medica_pregressa': dados[8],
            'historico_familiar': dados[9], 'historico_cirurgico': dados[10], 
            'medicamentos': dados[11], 'alimentacao': dados[12], 'exercicio': dados[13]
        })
    except Exception as e:
        print(f"Erro ao recuperar relatório: {e}")  # Adicionando depuração
        return render_template('erro.html', mensagem=f"Erro ao recuperar relatório: {e}")

if __name__ == '__main__':
    app.run(debug=True)
