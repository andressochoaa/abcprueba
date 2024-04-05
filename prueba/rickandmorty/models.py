from django.db import models

class Personaje(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    imagen = models.ImageField(upload_to="imagenes/", verbose_name="Imagen", null=True)
    descripcion = models.TextField(verbose_name="Descripción", blank=True)

    def __str__(self):
        fila = "Nombre: {0}, Imagen: {1}, Descripción: {2}".format(self.nombre, self.imagen, self.descripcion)
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

# Create your models here.
