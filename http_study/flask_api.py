from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados
DB_CONFIG = {
    'host': 'localhost',  # Altere para o seu host MySQL
    'user': 'root',  # Altere para o seu usuário MySQL
    'password': '153321',  # Altere para a sua senha MySQL
    'database': 'cadastro_pessoas'
}

def conectar_db():
    """Função para conectar ao banco de dados MySQL."""
    try:
        mydb = mysql.connector.connect(**DB_CONFIG)
        return mydb
    except mysql.connector.Error as err:
        return None, f"Erro ao conectar ao MySQL: {err}"

@app.route('/cadastro', methods=['POST'])
def cadastrar_pessoa():
    """Endpoint para receber os dados e salvar no banco de dados."""
    data = request.get_json()

    if not data:
        return jsonify({'erro': 'Nenhum dado fornecido.'}), 400

    # Validação dos campos obrigatórios (você pode adicionar mais validações)
    campos_obrigatorios = ['nome_completo', 'idade', 'rua', 'bairro', 'cidade', 'estado', 'cep', 'banco', 'nacionalidade']
    if not all(campo in data for campo in campos_obrigatorios):
        return jsonify({'erro': 'Todos os campos obrigatórios devem ser fornecidos.'}), 400

    try:
        mydb = conectar_db()
        if not mydb:
            return jsonify({'erro': 'Não foi possível conectar ao banco de dados.'}), 500

        cursor = mydb.cursor()
        sql = "INSERT INTO pessoas (nome_completo, idade, rua, bairro, cidade, estado, cep, banco, nacionalidade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (data['nome_completo'], data['idade'], data['rua'], data['bairro'], data['cidade'], data['estado'], data['cep'], data['banco'], data['nacionalidade'])
        cursor.execute(sql, values)
        mydb.commit()
        cursor.close()
        mydb.close()

        return jsonify({'mensagem': 'Dados cadastrados com sucesso!', 'id_inserido': cursor.lastrowid}), 201

    except mysql.connector.Error as err:
        return jsonify({'erro': f"Erro ao inserir dados: {err}"}), 500

if __name__ == '__main__':
    app.run(debug=True)