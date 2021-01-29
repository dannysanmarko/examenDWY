from django.db import models

# Create your models here.
class Producto(models.Model):
    title = models.TextField(max_length=50, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to='productos')
    link = models.URLField(verbose_name="Más información", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha creación")

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ['created']

    def __str__(self):
        return self.title