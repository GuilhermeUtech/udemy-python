#aula sobre mensurar tempo de execução
#Timeit

import timeit
string = '-'.join(str(n) for n in range(100))
#print(string)
print(timeit.timeit('"-".join(str(n) for n in range(100))', number = 10000))
#tem que passar como string o trecho de código
