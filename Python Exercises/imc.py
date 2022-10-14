
def imc(estatura, peso):
    return peso/(estatura**2)

peso = float(input('Ingrese su peso = '))
estatura = float(input('Ingrese su estatura = '))

indice = imc(estatura, peso)

print('Tu índice de masa corporal es: {}'.format(round(indice,2)))
