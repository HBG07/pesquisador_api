from django.db import models


class Area(models.Model):
    nombre = models.CharField(primary_key=True, max_length=200)
    municipio = models.CharField(max_length=200)
    provincia = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = 'area'
        verbose_name_plural = 'areas'
        db_table = 'areas'
        ordering = ['nombre']


class Consultorio(models.Model):
    numero = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=250)
    nombreArea = models.ForeignKey(
        Area, max_length=200, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.numero)

    class Meta:
        verbose_name = 'consultorio'
        verbose_name_plural = 'consultorios'
        db_table = 'consultorios'
        ordering = ['numero']


class Pesquisado(models.Model):
    CI = models.CharField(primary_key=True, max_length=11)
    nombre = models.CharField(max_length=200)
    primerApellido = models.CharField(max_length=200)
    segundoApellido = models.CharField(max_length=200)
    numero = models.ForeignKey(Consultorio, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.CI

    class Meta:
        verbose_name = 'pesquisado'
        verbose_name_plural = 'pesquisados'
        db_table = 'pesquisados'
        ordering = ['CI']


class Pesquisa(models.Model):
    CI = models.ForeignKey(Pesquisado, max_length=11, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True)
    encamado = models.BooleanField()
    contacto = models.BooleanField()
    familiaRiesgo = models.BooleanField()

    def __str__(self) -> str:
        return str(self.CI) + ' / ' + str(self.fecha)

    class Meta:
        verbose_name = 'pesquisa'
        verbose_name_plural = 'pesquisas'
        db_table = 'pesquisas'
        ordering = ['CI', 'fecha']
        unique_together = [('CI','fecha',)]
