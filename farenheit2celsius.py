# Funcao que tem o objtivo de calcular o valor de uma temperatura em Celsius a partir de seu valor em Farenheit

def faren2Cel():
    tf = float(input("Digite uma temperatura em Farenheit: "))
    tc = (tf - 32) * 5 / 9
    print("A temperatura em Celsius é", tc)

faren2Cel()