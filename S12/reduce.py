#aula sobre reduce()
#O reduce() ele faz a mesma coisa que um map(), porém do reduce fica fazendo essa operação até reduzir um iteravel até um unico valor
list = [46,11,42,13]

max_find = lambda a,b: a if (a>b) else b
print(reduce(max_find, list))


