from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# Справочники

class Apparatus(models.Model): # Экземпляр справочника аппаратов
    app_number=models.CharField(max_length=6, unique=True)
    app_desc=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.app_number


class Conveyor(models.Model): # Экземпляр справочника конвейеров
    conv_number=models.CharField(max_length=6, unique=True)
    conv_desc=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.conv_number


class Container(models.Model): # Экземпляр справочника емкостей
    cont_number=models.CharField(max_length=10, unique=True)
    cont_desc=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.cont_number


class Batch(models.Model): # Экземпляр справочника партий
    batch_name=models.CharField(max_length=50, unique=True)    
    
    def __str__(self):
        return str(self.batch_name)


class Marking(models.Model): # Экземпляр справочника артикулов
    marking_name=models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.marking_name)


# Таблицы


class Production(models.Model): # Экземпляр строки таблицы сводки
    date=models.DateField()
    marking=models.ForeignKey(Marking, on_delete=models.CASCADE)
    batch=models.ForeignKey(Batch, on_delete=models.CASCADE)
    cancelled=models.BooleanField(default=False)
    plan=models.IntegerField(default=10000)
    p_apparatus=models.ForeignKey(Apparatus, on_delete=models.CASCADE)
    p_container=models.ForeignKey(Container, on_delete=models.CASCADE)
    p_conveyor=models.ForeignKey(Conveyor, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.date)+" "+str(self.batch)+ " "+str(self.marking)


class Suppose_times(models.Model): # Экземпляр строки таблицы предполагаемых событий
    prod_row=models.OneToOneField(Production, on_delete=models.CASCADE)
    supp_app_test_time=models.TimeField(blank=True)
    supp_prod_adm_time=models.TimeField(blank=True)

    def __str__(self):
        return str(self.prod_row)+" "+str(self.supp_app_test_time)+ " "+str(self.supp_prod_adm_time)


class App_test_time(models.Model): # Экземпляр строки таблицы пробы из аппарата
    prod_row=models.OneToOneField(Production, on_delete=models.CASCADE)
    fix_time=models.TimeField(auto_now_add=True, blank=True)
    fix_user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.prod_row)+" "+str(self.fix_time)+ " "+str(self.fix_user)


class Prod_adm_time(models.Model): # Экземпляр строки таблицы допуска на фасовку
    prod_row=models.OneToOneField(Production, on_delete=models.CASCADE)
    fix_time=models.TimeField(auto_now_add=True, blank=True)
    fix_user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.prod_row)+" "+str(self.fix_time)+ " "+str(self.fix_user)


class Conv_test_time(models.Model): # Экземпляр строки таблицы пробы с конвейера
    prod_row=models.OneToOneField(Production, on_delete=models.CASCADE)
    fix_time=models.TimeField(auto_now_add=True, blank=True)
    fix_user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.prod_row)+" "+str(self.fix_time)+ " "+str(self.fix_user)


class Plug_adm_time(models.Model): # Экземпляр строки таблицы допуска на подключение
    prod_row=models.OneToOneField(Production, on_delete=models.CASCADE)
    fix_time=models.TimeField(auto_now_add=True, blank=True)
    fix_user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.prod_row)+" "+str(self.fix_time)+ " "+str(self.fix_user)