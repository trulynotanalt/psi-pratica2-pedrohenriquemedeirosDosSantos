from sqlalchemy import func, select
from models import Autor, Livro

def listar_todos_livros(session):
    sele_livro = select(Livro)
    livros = session.scalars(sele_livro).all()
    print("Autores e seus livros")
    for livro in livros:
        print(f"Titulo: {livro.titulo},  Ano: {livro.ano} , Autor: {livro.autor}  ")


def listar_livros_por_autor(session, nautor):
    sele_livro = select(Livro).where(Autor.nome.ilike(f"%{nautor}"))       
    livros = session.scalars(sele_livro).all()
    print(nautor)
    for livro in livros:
        print(livro.titulo, livro.ano, livro.autor.nome)

def listar_livros_por_titulo(session, busca):
    sele_livro = select(Livro).join(Livro.autor).where(Livro.titulo.ilike(f"%{busca}%"))
    livros = session.scalars(sele_livro).all()
    print(f"Livros com '{busca} ' no titulo")
    for livro in livros:
        print(f"- {livro.titulo} ({livro.ano})")        

def listar_autores_qtd_livros(session):
    sele_livro = (
        select(Autor.nome, func.count(Livro.id))
        .outerjoin(Autor.livros)
        .group_by(Autor.id)
    )
    resultados = session.execute(sele_livro).all()
    print("Quantidade de livros por autor")
    for autor_nome, qtd in resultados:
        print(f"Autor: {autor_nome} | Quantidade de livros: {qtd}")

def exibir_detalhes_livros(session,livro_id):
    sele_livro = select(Livro).where(Livro.id == livro_id)
    livro = session.scalars(sele_livro)
    print(f"Detalhes do livro{livro_id}")

    if livro:
        print(livro.titulo)
        print(livro.autor.nome)
        print(livro.ano)
        print(livro.autor.pais)
    else:
        print("Não temos livros")               