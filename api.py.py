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
        'titulo' : 'O senhor dos aneis - A sociedade do Anel'
        'autor' : 'autor1'
    },
        {
        'id': 2,
        'titulo' : 'O senhor dos aneis - 2'
        'autor' : 'autor1'
    },
        {
        'id': 3,
        'titulo' : 'O senhor dos aneis - 3'
        'autor' : 'autor1'
    }
]
