from search import Search


nome_produto = input('Escreva caracteristicas ou dê o nome do produto a ser descrito')

produto = Search(nome_produto)
print(produto)