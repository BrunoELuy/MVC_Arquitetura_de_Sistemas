from flask import Flask, render_template, jsonify, request
from models import listar_produtos, adicionar_produto

# Inicializa o Flask
app = Flask(__name__)

# Inicializa a rota principal responsável por mostrar os produtos via HTML
@app.route("/")
def pagina_produtos():

    # Pega a lista de produtos, guarda na variável, e retorna dentro do html
    produtos = listar_produtos()
    return render_template("produtos.html", produtos=produtos)

# Inicializa a rota responsável por mostrar os produtos no estilo JSON padrão API
@app.route("/api/produtos")
def api_listar_produtos():

    # Puxa os produtos, guarda na variável, formata e retorna no estilo JSON
    produtos = listar_produtos()
    data = [{"id": p.id, "nome": p.nome, "preco": p.preco} for p in produtos]
    return jsonify(data)

# Inicializa a rota responsável por adicionar um produto no estilo JSON padrão API
@app.route("/api/produtos", methods=["POST"])
def api_adicionar_produto():
    
    # Pega todas as informações para subir um novo produto
    dados = request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")

    # Adiciona o novo produto e retorna uma mensagem de sucesso
    adicionar_produto(nome, preco)
    return jsonify({"mensagem": "Produto adicionado com sucesso"})

# Roda o Flask
if __name__ == "__main__":
    app.run(debug=True)