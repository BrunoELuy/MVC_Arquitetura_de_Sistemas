from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Cria o engine conectado a SQLite com a URI, \\\ serve para caminho relativo ao atual
# echo=True habilita logging:SQL, isso será impresso no console (útil para debug)
# Engine gerencia conexões com o banco; o ORM e sessio usam a engina
engine = create_engine("sqlite:///database.db", echo=True)

# Cria classe Base para o modelo, classe Produtos herda ela.
# Base contém metadata (objeto que conhece todas as tabelas definidas por classes que herdam ela)
Base = declarative_base()

# Define a classe que será mapada para uma tabela SQL
class Produtos(Base):
    # Define o nome da tabela no banco de dados = produtos
    __tablename__ = "produtos"

    # id será uma coluna para identificação de produto
    # Se a Coluna tiver Integer e Primary_key no SQLite, ela se torna AUTOINCREMENT
    # Isto significa que um produto novo recebe automáticamente o próximo id disponível
    # E cada id será único para um objeto, facilitando o mapeamento (primari_key=True)
    id = Column(Integer, primary_key=True)

    # Coluna de texto onde terá o nome do produto, máximo de 100 caracteres
    nome = Column(String(100))

    # Coluna numérica de ponto flutuante
    preco = Column(Float)

# Se caso ainda não existir no banco de dados, cria todas as tabelas conhecidas no Base.metadata
Base.metadata.create_all(engine)

# Isto cria uma fábrica de sessões, quando chamada retorna uma nova Session ligada ao engine
Session = sessionmaker(bind=engine)

# Sessão global usada para as funções abaixos, utilizada apenas em scripts pequenos
session = Session()

# Retorna a lista de todos os produtos
def listar_produtos():
    # session.query(Produtos) retorna uma consulta SELECT para Produtos
    # .all() executa a consulta e retorna uma lista de objetos Produtos
    # Resultado são objetos Python com atributos como .id .nome e .preco
    # Basicamente: SELECT * FROM Produtos
    return session.query(Produtos).all()

# Adiciona um novo produto ao banco de dados
def adicionar_produto(nome, preco):
    # Cria uma nova instância Python do modelo com base no nome e preço passados
    # Neste momento a instância existe, mas ainda não foi salva no DB (data base)
    novo = Produtos(nome=nome, preco=preco)

    # Marca esta instância como pendente para inserir no banco de dados, assim no comit ela sobe
    try:
        session.add(novo)
        # Feito o comit e confirma o envio ao banco de dados
        # Basicamente o comando INSERT do SQL
        session.comit()
        return novo
    except Exception:
        # Trativa, se caso não funcionar o commit, é revertido todas as instâncias e alterações
        session.rollback()
        raise