from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField('Nombre',max_length=100, blank=True)
    last_name = models.CharField('Apellido', max_length=100, blank=True)
    email = models.EmailField('Email', max_length=254, unique=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']        
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'