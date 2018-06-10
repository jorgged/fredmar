from django.db import models

# Create your models here.
class misionEmpresa(models.Model):
    mision = models.CharField(max_length=1000)
    def __str__(self):
        return self.mision

class visionEmpresa(models.Model):
    vision = models.CharField(max_length=1000)
    def __str__(self):
        return self.vision

class horarioEmpresa(models.Model):
    turno = models.CharField(max_length=20)
    def __str__(self):
        return self.turno

class telefonoEmpresa(models.Model):
    tlf = models.CharField(max_length=15)
    def __str__(self):
        return self.tlf