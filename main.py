from database import criar_banco, get_sessao
from seed import popular_banco
from consultas import (
    listar_todos_livros,
    listar_livros_por_autor,
    listar_autores_qtd_livros,
    listar_livros_por_titulo,
    exibir_detalhes_livros,
)

def main():
    criar_banco()
    sessao = get_sessao()

    popular_banco(sessao)
    listar_todos_livros(sessao)
    listar_livros_por_titulo(sessao, "Biologia")
    listar_autores_qtd_livros(sessao)
    listar_livros_por_autor(sessao, "Augusto")
    exibir_detalhes_livros(sessao, 1)

    sessao.close()

if __name__ == "__main__":
    main()