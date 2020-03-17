x = 'olá'
print(type(x))
print(x)

a = "Olá tudo bem com vcs?"  #da pra fazer com " " e com ' '
b = 'Olá tudo bem com vcs?'

exemplo =  "i'm a beliver! \t bla bla bla" #exemplo de utilização de " " e ' ', \t da um tab dentro do texto
print(a,b,exemplo)

print(len(exemplo)) #len() mostra o tamanho da string

#acessando posição dos elementos:

print(exemplo[4])
print(exemplo[:]) # o : pega toda a string
print(exemplo[2:]) #começa na posicao 2 e vai até o final
print(exemplo[2:14]) #começa na posicao 2 e vai até o 14

#Concatenação de strings

str = "geroni"
ing = "mo"
print(str+ing)
ae = str + ing
print(ae)

#metodos inbutidos em string

print(ae.find('a'))
print(ae.find('g'))
print(a.split())







