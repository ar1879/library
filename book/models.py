from tabnanny import verbose
from django.utils import timezone
from django.db import models


# Create your models here.

class Author(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Nombre', max_length=150, blank=False, null=False)
    last_name = models.CharField('Apellido', max_length=100, blank=False, null=False)
    nationality = models.CharField('Nacionalidad', max_length=100, blank=False, null=False)
    state = models.BooleanField('Estado', default=True)
    


    def __str__(self):
       return self.name

    class Meta:
        ordering = ['name']       
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Titulo', max_length=150, blank=False, null=False)
    publication_date = models.DateField('Fecha_publicacion', default=timezone.now)
    author_id = models.ForeignKey("Author", verbose_name='Autor', on_delete=models.CASCADE)
    #foreign key = uno() a muchos = un autor puede tener muchos libros y no viceversa
    class Meta:
        ordering = ['title']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    
    def __str__(self):
        return self.title

    