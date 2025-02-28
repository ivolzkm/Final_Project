# Flask Anamnese App

This is a Flask web application for collecting patient anamnesis data. The application guides the user through a series of forms to collect various health-related information.

## Templates

The application uses the following HTML templates:

- `index.html`: Tela inicial
- `escolha.html`: Tela de escolha entre aguardar ou preencher
- `nome_idade_sexo.html`: Passo 1 - Identificação (Nome, Idade, Sexo)
- `profissao_estado_endereco.html`: Passo 2 - Identificação (Profissão, Estado Civil, Endereço)
- `queixa_principal.html`: Passo 3 - Motivo da consulta
- `historia_doenca.html`: Passo 4 - Início da evolução dos sintomas
- `evolucao_sintomas.html`: Passo 5 - Evolução dos sintomas
- `fatores_sintomas.html`: Passo 6 - Fatores que pioram/melhoram os sintomas
- `doencas_preexistentes.html`: Passo 7 - Doenças pré-existentes
- `historico_cirurgico.html`: Passo 8 - Histórico de cirurgias e hospitalizações
- `medicamentos.html`: Passo 9 - Uso regular de medicamentos
- `historico_familiar.html`: Passo 10 - Doenças na família
- `familiar_saude.html`: Passo 11 - Problemas de saúde em familiares próximos
- `habitos.html`: Passo 12 - Hábitos de vida (fumo, álcool, drogas)
- `alimentacao_exercicio.html`: Passo 13 - Alimentação e exercícios físicos
- `moradia_trabalho.html`: Passo 14 - Condições de moradia e trabalho
- `obrigado.html`: Passo 15 - Confirmação do envio dos dados
- `erro.html`: Página de erro para exibir mensagens de erro

## Getting Started

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/flask-anamnese-app.git
    cd flask-anamnese-app
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the application:**
    ```sh
    python app.py
    ```

4. **Access the application:**
    Open your web browser and go to [http://localhost:5000](http://localhost:5000).

## Database

The application uses SQLite as the database. The database schema is automatically created when the application is started.

## License

This project is licensed under the MIT License.