from django.db import models

class directores(models.Model):
    name = models.CharField(max_length=50, help_text='Ingresa el nombre del director')

    def __str__(self):
        return self.name

class peliculas(models.Model):
    titulo = models.CharField(max_length=60)
    resumen = models.CharField(max_length=150)
    director = models.ForeignKey('directores', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo
