from django.db import models

# Create your models here.
class Notebook(models.Model):
    tagid = models.CharField(max_length=50)
    fecha_ultima_mantencion = models.DateField()
    SO = models.CharField(max_length=50)
    def __str__(self):
        return self.tagid
