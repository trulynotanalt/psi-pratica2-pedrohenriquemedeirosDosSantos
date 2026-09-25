from sqlalchemy import  String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship


class Base(DeclarativeBase):
    pass
class Autor(Base):
    __tablename__ = "autores"

    id: Mapped[int] =  mapped_column(primary_key = True)
    nome: Mapped[str] =  mapped_column(String(50))
    pais : Mapped[str] =  mapped_column(String(60))
    livros: Mapped[list[Livro]] = relationship("Livro", back_populates="autor")


class Livro(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(primary_key= True)
    titulo: Mapped[str] = mapped_column(String(160))
    ano: Mapped[int] = mapped_column(Integer)
    autor_id: Mapped[int]= mapped_column(ForeignKey("autores.id"))
    autor: Mapped[Autor] = relationship("Autor", back_populates="livros")