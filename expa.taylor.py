import math as mt

#Expansão de taylor for funcao seno
def seno(x,n):
    valor_aproximado = 0
    for k in range(n):
        valor_aproximado += ((-1)**k) * (pow(x,2*k+1)/mt.factorial(2*k+1))

    return valor_aproximado
#Expansão de taylor for funcao e**ix
def eix(x,n):
    valor_aprox = 0
    for k in range(n):
        valor_aprox += (((-1)**k) * pow(x,2*k)/mt.factorial(2*k)
                        ) + (((-1)**k) * (pow(x,2*k+1)/mt.factorial(2*k+1))) *1j
    
    return valor_aprox