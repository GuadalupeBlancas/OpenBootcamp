
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota 

        if nota >=6:
            print(nombre +'tu nota es aprobatoria')
        elif nota <= 6:
            print(nombre +'tu nota NO es aprobatoria')


print(Alumno(nombre= 'Liz ', nota= 3))

