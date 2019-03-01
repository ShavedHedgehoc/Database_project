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
class batch(models.Model):
    batch_name=models.CharField(max_length=50)
    marking=models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.batch_name)+" "+self.marking

class l_admission(models.Model):
    admission_time=models.TimeField()

""" class boil(models.Model):
    date=models.DateField()
    b_batch=models.ForeignKey(batch, on_delete=models.CASCADE)
    ##b_marking=models.CharField(max_length=50)
    cancelled=models.BooleanField(default=False)
    plan=models.IntegerField(default=10000)
    b_apparatus=models.ForeignKey(apparatus, on_delete=models.CASCADE)
    b_container=models.ForeignKey(container, on_delete=models.CASCADE)
    b_conveyor=models.ForeignKey(conveyor, on_delete=models.CASCADE)
    admission=models.ForeignKey(l_admission, on_delete=models.CASCADE)
    time_probe=models.TimeField()
    time_start=models.TimeField()

    def __str__(self):
        return str(self.date)+" "+self.b_batch.batch_name """

class lab_admission(models.Model):
    admission_batch=models.ForeignKey(batch, on_delete=models.CASCADE)
    admission_time=models.TimeField()

class production(models.Model):
    date=models.DateField()
    marking=models.CharField(max_length=50)
    batch=models.CharField(max_length=50)
    cancelled=models.BooleanField(default=False)
    plan=models.IntegerField(default=10000)
    p_apparatus=models.ForeignKey(apparatus, on_delete=models.CASCADE)
    p_container=models.ForeignKey(container, on_delete=models.CASCADE)
    p_conveyor=models.ForeignKey(conveyor, on_delete=models.CASCADE)
    time_probe=models.TimeField()
    time_start=models.TimeField()
    app_test_time=models.TimeField()
    admission_plug_time=models.TimeField()
    conv_probe_time=models.TimeField()
    adm_prod_time=models.TimeField()
    prod_fact_time=models.TimeField()