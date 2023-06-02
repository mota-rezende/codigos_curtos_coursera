# Funcao que calcula a media ponderada de tres notas com pesos respectivos de 20%, 40 % e 40%

def media_pond():
    av1 = float(input("Avaliacao 1:"))
    av2 = float(input("Avaliacao 2:"))
    av3 = float(input("Avaliacao 3:"))
    media = ((0.2*av1)+(0.4*av2)+(0.4*av3))
    print(media)

media_pond()