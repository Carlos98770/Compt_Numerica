import math as mt

#Resolucao de equcoes nao lineares
#Metodo da bisserçao
def f(x):
    pass

def bissercao(a,b,tolerancia):
    if f(a)*f(b) >= 0:
        return print("INTERVALO INVALIDO")
    x0 = 0
    cont = 0
    while True:
        x = (a+b)/2

        
        if f(a)*f(x) < 0:
            b = x
        
        else:
            a = x

        erro = abs(x-x0) / x

        if erro < tolerancia:
            print('Numero de Passos: ',cont)
            return x

        x0 = x
        cont +=1
        

a = 0.5
b = 2.0
tol = 2e-2
print(bissercao(a,b,tol))
