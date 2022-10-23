from functools import reduce

numero = [1,2,3,4,5,6,7,8,9,10]

def suma(x):
    if x % 2 == 0:
        return True
    return False

resultado = filter(suma, numero)
print(sum(resultado))