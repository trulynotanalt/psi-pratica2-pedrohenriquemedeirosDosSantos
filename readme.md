### 1. Onde estão os modelos ORM no seu projeto?

## Os objetos estão presentes no arquivo seed.py, nos seguintes trechos de código, que criam novas entidades com base nas classes presentes em models.py:


     autor1 = Autor(nome="Augusto Cury", pais = "Brasil"),
    autor2 = Autor(nome = "Araki", pais = "japao"),
    autor3 = Autor(nome = "Cleysyvan" ,pais = "Brasil"),

    livros = [
        Livro(titulo="Ansiedade, o Mal do século", ano=2026, autor=autor1),
        Livro(titulo="O vendedor de sonhos", ano=1991, autor=autor1),
        Livro(titulo="Jojo steel ball run", ano=2016, autor=autor2),
        Livro(titulo="a hora da biologia", ano=2010, autor=autor3),
        Livro(titulo="Biologia, minha vida meu saber", ano=2020, autor=autor3),
        Livro(titulo="Reprodução assexuada dos homens", ano=2000, autor=autor3)
    ]
## Os relacionamentos estão presentes nos trechos que contém o relationship dentro do models.py

livros: Mapped[List["Livro"]] = relationship("Livro", back_populates="autor")

autor: Mapped["Autor"] = relationship("Autor", back_populates="livros")

## Os mapeamentos estão presentes nas linhas dentro do models.py que contém o mapped, demonstrando e especificando o tipo de atributo que será inferido nas classes 

# para os usuarios:
id: Mapped[int] = mapped_column(primary_key=True)
nome: Mapped[str] = mapped_column(String(100), nullable=False)
pais: Mapped[str] = mapped_column(String(50), nullable=False)

# para os livros:
id: Mapped[int] = mapped_column(primary_key=True)
titulo: Mapped[str] = mapped_column(String(150), nullable=False)
ano: Mapped[int] = mapped_column(Integer, nullable=False)


### 2. Qual classe representa o lado "um" e qual representa o lado "muitos" no relacionamento?

A classe Autor é o lado de um enquanto o lado de muitos é a classe Livros, notado pela presença ou ausência do List[] quando mapeamos os atributos

### 3. Para que serve o ForeignKey em Livro.autor_id ?

serve para vincular um livro ao id do autor, podendo acessar, dessa maneira, os recursos presentes na classe Autor podem ser acessadas a partir do livro.autores_id que recebe o autores.id

### 4. O que acontece se você esquecer o session.commit() após inserir os dados?


as operações realizadas no banco de dados não seriam salvadas, então é a mesma cois de mudar um código mas não salvar as alterações ou usar o simplesmente não registrar o código feito