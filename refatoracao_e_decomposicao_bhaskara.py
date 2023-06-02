# funcoes que realizam a formula de Bhaskara, tal como no script anterior, mas aqui foram aplicados exercicios de refatoracao e de-
# composicao

def main():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    imprime_raizes(a, b, c)

def delta(a, b, c):
    delta = b**2 - 4*a*c

def imprime_raizes(a, b, c):
    if delta < 0:
        print("A equação nao possui raizes reais.")
    elif delta == 0:
        x = -b / 2*a
        print("A raiz da equação é", x,".")
    else:
        x1 = (-b + delta**(1/2))/(2*a)
        x2 = (-b - delta**(1/2))/(2*a)
        print("As raízes da equação são", x1, "e", x2, ".")

main()