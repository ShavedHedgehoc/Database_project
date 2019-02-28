from django.db import models

# Create your models here.

class apparatus(models.Model): # Экземпляр справочника аппаратов
    app_number=models.CharField(max_length=6)
    app_desc=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.app_number

class conveyor(models.Model): # Экземпляр справочника конвейеров
    conv_number=models.CharField(max_length=6)
    conv_desc=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.conv_number

class container(models.Model): # Экземпляр справочника емкостей
    cont_number=models.CharField(max_length=6)
    cont_desc=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.cont_number

class boil(models.Model):
    date=models.DateField()
    batch=models.CharField(max_length=50)
    marking=models.CharField(max_length=50)
    cancelled=models.BooleanField(default=False)
    plan=models.IntegerField(default=10000)
    b_apparatus=models.ForeignKey(apparatus, on_delete=models.CASCADE)
    b_container=models.ForeignKey(container, on_delete=models.CASCADE)
    b_conveyor=models.ForeignKey(conveyor, on_delete=models.CASCADE)
    time_probe=models.TimeField()
    time_start=models.TimeField()

    def __str__(self):
        return str(self.date)+" "+self.batch+" "+self.marking

class lab_admission(models.Model):
    pass
