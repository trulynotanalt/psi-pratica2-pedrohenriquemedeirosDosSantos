from models import Autor, Livro

def popular_banco(session):
    

    autor1 = Autor(nome="Augusto Cury", pais = "Brasil"),
    autor2 = Autor(nome = "Araki", pais = "japao"),
    autor3 = Autor(nome = "Cleysyvan" ,pais = "Brasil"),

    Livros = [
        Livro(titulo="Ansiedade, o Mal do século", ano=2026, autor=autor1),
        Livro(titulo="O vendedor de sonhos", ano=1991, autor=autor1),
        Livro(titulo="Jojo steel ball run", ano=2016, autor=autor2),
        Livro(titulo="a hora da biologia", ano=2010, autor=autor3),
        Livro(titulo="Biologia, minha vida meu saber", ano=2020, autor=autor3),
        Livro(titulo="Reprodução assexuada dos homens", ano=2000, autor=autor3)
    ]

    session.add_all([autor1,autor2,autor3])
    session.add_all(Livros)
    session.commit()