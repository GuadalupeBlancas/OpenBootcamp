class Vehiculo:
    color = 'Rojo'
    ruedas = 4  
    puertas = 2

class Coche(Vehiculo):
    velocidad = 100
    Cilindrada = 50

c = Coche()
c.color, c.ruedas, c.puertas, c.velocidad, c.Cilindrada

print(c.color, c.ruedas, c.puertas, c.velocidad, c.Cilindrada) 