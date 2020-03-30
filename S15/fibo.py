#Fazer um fibo bem massa

def fibo(n):
    anterior = 0
    atual = 1
    for i in range(n):
        proximo = anterior + atual
        print(proximo)
        anterior = atual
        atual = proximo
    
fibo(100)
        
         
