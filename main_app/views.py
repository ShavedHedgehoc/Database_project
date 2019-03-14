import datetime

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

from .models import Production, App_time, Conv_time, Plug_time, Prod_time
from .models import Supp_time



def index(request):    
    h="Это мы напишем в заголовке"
    b="a это в теле мы напишем в заголовке"
    return render(request, 'index.html', locals())


def add_adm(request, id,t_name): 
    if request.method=="POST":
        if request.user.is_anonymous:
            return HttpResponseNotFound("<h2>forbidden</h2>")
        if t_name=="app":
            new_adm=App_time()
        elif t_name=="plug":
            new_adm=Plug_time()
        new_adm.f_row=Production.objects.get(id=id)
        new_adm.f_user=request.user
        new_adm.save()    
    return HttpResponseRedirect("/")


def edit_adm(request, id,t_name): 
    if request.method=="POST":
        if request.user.is_anonymous:
            return HttpResponseNotFound("<h2>forbidden</h2>")
        if t_name=="app":
            my_obj=App_time
        elif t_name=="plug":
            my_obj=Plug_time        
        try:
            app = my_obj.objects.get(f_row_id=id)
            app.delete()
            return HttpResponseRedirect("/")
        except my_obj.DoesNotExist:
            return HttpResponseNotFound("<h2>not found</h2>")
        



def table_view(request):
    now=datetime.datetime.now()    
    query_date=now.strftime("%Y-%m-%d")      
    headers=[               
        'Дата','Артикул','№ парт.','План',
        '№ аппар.','№ емкости',
        '№ конв.','Проба из аппарата',
        'Допуск на подключение','Проба с конвейера',
        'Допуск на фасовку','Начало фасовки'
    ]  
        
    records=Production.objects.select_related(
        'app_time', 'plug_time', 'conv_time',
        'prod_time', 'start_time'
    )
    # return render(request, 'table_view.html', {'records':records, 'headers':headers})
    return render(request, 'table_view.html', {'records':records, 'headers':headers})

    
def test_page(request):    
    return render(request, 'test_page.html', locals())