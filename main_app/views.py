import datetime

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

""" from .models import Production, App_test_time, Conv_test_time
from .models import Suppose_times, Plug_adm_time, Prod_adm_time """

from .models import Production2, App_test_time2, Plug_adm_time2


def index(request):    
    return render(request, 'index.html', locals())


def add_adm(request, id,t_name): 
    if request.method=="POST":
        if request.user.is_anonymous:
            return HttpResponseNotFound("<h2>forbidden</h2>")
        if t_name=="app":
            new_adm=App_test_time2()
        elif t_name=="plug":
            new_adm=Plug_adm_time2()
        new_adm.fix_row=Production2.objects.get(id=id)
        new_adm.fix_user=request.user
        new_adm.save()    
    return HttpResponseRedirect("/")


def edit_adm(request, id,t_name): 
    if request.method=="POST":
        if request.user.is_anonymous:
            return HttpResponseNotFound("<h2>forbidden</h2>")
        if t_name=="app":
            my_obj=App_test_time2
        elif t_name=="plug":
            my_obj=Plug_adm_time2        
        try:
            app = my_obj.objects.get(fix_row_id=id)
            app.delete()
            return HttpResponseRedirect("/")
        except my_obj.DoesNotExist:
            return HttpResponseNotFound("<h2>not found</h2>")
        

def index(request):    
    return render(request, 'test_page.html', locals())


def table_view(request):
    now=datetime.datetime.now()    
    query_date=now.strftime("%Y-%m-%d")      
    headers=[
        'Дата фасовки','Артикул','№ парт.', 'План','№ аппар.','№ емкости',
        '№ конв.','Окончательная проба из аппарата (фактическое время)',
        'Допуск на подключение','Проба продукта с конвейера',
        'Допуск на фасовку','Фактическое время начала фасовки'        
    ]  
    """ records=Production.objects.select_related(
        'suppose_times','app_test_time', 'conv_test_time',
        'plug_adm_time', 'prod_adm_time'
    ) """
    
    records=Production2.objects.select_related(
        'app_test_time2', 'plug_adm_time2'
    )
    # return render(request, 'table_view.html', {'records':records, 'headers':headers})
    return render(request, 'table_view1.html', {'records':records, 'headers':headers})

    
def test_page(request):    
    return render(request, 'test_page.html', locals())