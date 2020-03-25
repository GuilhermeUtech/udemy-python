#Aula sobre métodos especiais
class Book(object):
    def __init__(self, titulo, autor, paginas):
        print("livro criado")
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return "Título: {a}".format(a = self.titulo)
    def __len__(self):
        return self.paginas
    def __del__(self):
        print("Livro destruído")
    

livro = Book("livro sobre python", "Jorge bengola", 123)
print(livro)


