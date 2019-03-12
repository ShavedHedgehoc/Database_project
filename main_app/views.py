from django.shortcuts import render
from .models import Production, App_test_time, Conv_test_time, Plug_adm_time, Prod_adm_time
from .models import Suppose_times
from django.template import RequestContext
from django.http import HttpResponseRedirect
import datetime

def index(request):    
    return render(request, 'index.html', locals())

def add_adm(request, id):    
    new_adm=App_test_time()
    new_adm.prod_row=Production.objects.get(id=id)
    new_adm.fix_user=request.user
    new_adm.save()    
    return HttpResponseRedirect("/")


def index(request):    
    return render(request, 'test_page.html', locals())

def table_view(request):
    now=datetime.datetime.now()    
    query_date=now.strftime("%Y-%m-%d")  
    # headers=[
    #     'Дата фасовки','Артикул','№ парт.', 'План','№ аппар.','№ емкости',
    #     '№ конв.','Время 1','Время 2','Проба из аппарата','Допуск на подключение',
    #     'Проба с конвейера','Допуск на фасовку','Начало фасовки',        
    # ] 
    headers=[
        'Дата фасовки','Артикул','№ парт.', 'План','№ аппар.','№ емкости',
        '№ конв.','Окончательная проба из аппарата (фактическое время)',
        'Допуск на подключение','Проба продукта с конвейера',
        'Допуск на фасовку','Фактическое время начала фасовки'        
    ]  
    records=Production.objects.select_related(
        'suppose_times','app_test_time', 'conv_test_time','plug_adm_time', 'prod_adm_time'
        )
    return render(request, 'table_view.html', {'records':records, 'headers':headers})
    
def test_page(request):    
    return render(request, 'test_page.html', locals())