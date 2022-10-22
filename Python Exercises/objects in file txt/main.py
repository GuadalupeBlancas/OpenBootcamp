class Vehiculo():
    color = 'Rojo'

vehiculo = Vehiculo()
v = vehiculo.color

f = open('C:/Users/Yusuli/Desktop/objects in file txt/a.txt', 'w')
f.write(v)
f.close()