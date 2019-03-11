from django.db import models
from django.contrib.auth.models import User


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


class production(models.Model):
    date=models.DateField()
    marking=models.CharField(max_length=50)
    batch=models.CharField(max_length=50)
    cancelled=models.BooleanField(default=False)
    plan=models.IntegerField(default=10000)
    p_apparatus=models.ForeignKey(apparatus, on_delete=models.CASCADE)
    p_container=models.ForeignKey(container, on_delete=models.CASCADE)
    p_conveyor=models.ForeignKey(conveyor, on_delete=models.CASCADE)
    # time_probe=models.TimeField(blank=True, null=True)
    # time_start=models.TimeField(blank=True, null=True)
    # app_test_time=models.TimeField(blank=True, null=True)
    # admission_plug_time=models.TimeField(blank=True, null=True)
    # conv_probe_time=models.TimeField(blank=True, null=True)
    # adm_prod_time=models.TimeField(blank=True, null=True)
    # prod_fact_time=models.TimeField(blank=True, null=True)

    def __str__(self):
        return str(self.date)+" "+self.batch+ " "+self.marking


class lab_adm2(models.Model):
    prod_row=models.OneToOneField(production, on_delete=models.CASCADE)
    admission_time=models.TimeField()
    lab_user=models.ForeignKey(User, on_delete=models.CASCADE)

class plug_adm(models.Model):
    prod_row=models.OneToOneField(production, on_delete=models.CASCADE)
    admission_time=models.TimeField(auto_now_add=True, blank=True)
    lab_user=models.ForeignKey(User, on_delete=models.CASCADE)
 
    