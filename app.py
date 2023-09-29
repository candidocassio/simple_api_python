# API
#     - Obejtivos 
#     1 - Objetivos - criar api de livros
#     2 - URL Base - localhost.com 
#     3 - ENDpoint
            # - localhost/livros (GET)
            # - localhost/livros (POST)
            # - localhost/livros/id (GET)
            # - localhost/livros/id (PUT)
            # - localhost/livro/id (DELETE)
#     4 - Quais recursos - Livros

# flask

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo' : 'O senhor dos aneis - A sociedade do Anel',
        'autor' : 'autor1'
    },
    
    {
        'id': 2,
        'titulo' : 'O senhor dos aneis - 2',
        'autor' : 'autor1'
    },
    
    {
        'id': 3,
        'titulo' : 'O senhor dos aneis - 3',
        'autor' : 'autor1'
    }
]

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_um_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])      

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
        return jsonify(livros)

        
app.run(port=5000, host='localhost',debug=True)
