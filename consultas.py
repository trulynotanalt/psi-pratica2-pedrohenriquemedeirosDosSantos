from sqlalchemy import func, select
from models import Autor, Livro

def listar_todos_livros(session):
    sele_livro = select(Livro)
    livros = session.scalars(sele_livro).all()
    print("Autores e seus livros")
    for livro in livros:
        print(f"Título: {livro.titulo}, Ano: {livro.ano}, Autor: {livro.autor.nome}")


def listar_livros_por_autor(session, nautor):
    sele_livro = select(Livro).join(Livro.autor).where(Autor.nome.ilike(f"%{nautor}%"))
    livros = session.scalars(sele_livro).all()
    print(f"--- Livros do autor '{nautor}' ---")
    for livro in livros:
        print(livro.titulo, livro.ano, livro.autor.nome)


def listar_livros_por_titulo(session, busca):
    sele_livro = select(Livro).where(Livro.titulo.ilike(f"%{busca}%"))
    livros = session.scalars(sele_livro).all()
    print(f"--- Livros com '{busca}' no título ---")
    for livro in livros:
        print(f"- {livro.titulo} ({livro.ano})")


def listar_autores_qtd_livros(session):
    sele_livro = (select(Autor.nome, func.count(Livro.id)).outerjoin(Autor.livros).group_by(Autor.id))
    resultados = session.execute(sele_livro).all()
    print("Quantidade de livros por autor ")
    for autor_nome, qtd in resultados:
        print(f"Autor: {autor_nome} | Quantidade de livros: {qtd}")


def exibir_detalhes_livros(session, livro_id):
    sele_livro = select(Livro).where(Livro.id == livro_id)
    livro = session.scalar(sele_livro)

    if livro:
        print(f"Detalhes do livro do id {livro_id} ")
        print(f"Titulo: {livro.titulo}")
        print(f"Autor: {livro.autor.nome}")
        print(f"Ano: {livro.ano}")
        print(f"País do Autor: {livro.autor.pais}")
    else:
        print(f"Livro do id {livro_id} não encontrado.")