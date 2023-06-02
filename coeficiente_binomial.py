# A primeira funcao tem o objetivo de calcular o fatorial de um determinado numero, enquanto a segunda funcao (que utiliza a primeira 
# em seu conjunto de instrucoes), tem o objetivo de calcular o coeficiente binomial a partir de dois numeros digitados

def fatorial(x):
    f = 1
    while x > 1:
        f *= x
        x -= 1
    return f

def coeficienteBin():
    n = int(input("Digite o valor de n: "))
    k = int(input("Digite o valor de k: "))

    coef = int(fatorial(n) / (fatorial(k) * fatorial(n - k)))
    print(coef)

coeficienteBin()