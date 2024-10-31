import random
livros = []
 
def cadastro_de_livros(titulo, autor, ano_de_puplicacao, gênero):
    novo_livro = {"titulo": "", "autor": "", "ano_de_puplicacao": "", "id": "" }
    id_aleatorio = random.randint(1000, 9999)
    novo_livro["titulo"] = titulo
    novo_livro["autor"] = autor
    novo_livro["ano_de_puplicacao"] = ano_de_puplicacao
    novo_livro["genero"] = gênero
    novo_livro["id"] = id_aleatorio

    livros.append(novo_livro)
    return "Livro cadastrado com sucesso"

cadastro_de_livros("Dom Casmurro", "Machado de Assis", 1899, "Ficção")
print(livros)