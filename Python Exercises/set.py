
nameCountry = input('Ingresa nombres de paises: ')

if nameCountry != '':
    ncl = set(nameCountry.split(','))
    print(ncl)