from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        app_label = 'proyecto_Bisaguirre'

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        app_label = 'proyecto_Bisaguirre'

class Tarea(models.Model):
    descripcion = models.CharField(max_length=200)
    completada = models.BooleanField(default=False)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        app_label = 'proyecto_Bisaguirre'
    
