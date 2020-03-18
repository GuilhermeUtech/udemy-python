#Aula sobre arquivos
meu_arquivo = open('texto.txt')
print(meu_arquivo.read())
#resentaod o ponteiro do arquivo
meu_arquivo.seek(0)
print("Voltando ao inicio do arquivo")
print(meu_arquivo.readline())
meu_arquivo.seek(0)

#iterando dentro de um arquivo de texto
for line in meu_arquivo:
    print(line)
ar
