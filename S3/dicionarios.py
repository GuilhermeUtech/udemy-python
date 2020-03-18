#aula sobre dicionários
#o dicionario é como uma lista porém acessamos os dados de 
#maneira diferente, vamos mapear dos dados
#associa cada valor com uma chave

#definindo um dicionário
dicionarios ={'nome' : "Guilherme", 'idade' : 22, 'sexo' : "masculino"}
print(dicionarios['nome'])
print(dicionarios['idade'])
print(dicionarios['sexo'])

#dicinoarios aceitam vários tipos de dados

dicion = {'lista_de_listas' : [1,2,3, [4,5,6]]}
print(dicion['lista_de_listas'])

#dicionarios são mutaveis
dicionarios['nome'] = "daniel"
print(dicionarios)

#podemos criar dicionários vazios e ir adicionando
d = {}
d['cachorro'] = "Nina"
print(d)

#é bem parecido com o JSON

#Dicionários de dicionários

alunos = {'aluno_1': {'nome' : "Guilherme", 'sobrenome' : "Utech"}, 'aluno_2': {'nome': 'Jessica', 'sobrenome' : 'Cristine'}}
print(alunos)
print(alunos['aluno_1'])

#Métodos legais em dicionários
print(alunos.keys()) #mostra as chaves do dicionário
print(alunos.values()) #todos os valores
print(alunos.items()) #retorna todos os itens do dicionario









