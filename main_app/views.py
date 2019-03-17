import datetime

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.contrib import auth

from .models import Production, App_time, Conv_time, Plug_time, Prod_time
from .models import Supp_time
from .forms import MyForm



def index(request):  
    context={} 
    curr_user =auth.get_user(request).username
    # curr_user=uu_user.username
    # user_group=uu_user.groups.filter(id=1)
    context={'curr_user':curr_user}
    return render(request, 'index.html', context)




def add_adm(request, id, t_name): 
    if request.method=="POST":
        if request.user.is_anonymous:
            return HttpResponseNotFound("<h2>forbidden</h2>")
        if t_name == "app":
            new_adm=App_time()
        elif t_name == "plug":
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
    # query_date=now.strftime("%Y-%m-%d")      
    context={}
    headers=[               
        'Дата','Артикул','№ парт.','План',
        '№ аппар.','№ емкости',
        '№ конв.','Проба из аппарата',
        'Допуск на подключение','Проба с конвейера',
        'Допуск на фасовку','Начало фасовки'
    ]  
     
    prod_records=Production.objects.select_related(
        'app_time', 'plug_time', 'conv_time',
        'prod_time', 'start_time'
    )
    records=[]

    for i in prod_records:
        
        try:
            i_app_time=i.app_time.f_time
        except Production.app_time.RelatedObjectDoesNotExist:
            i_app_time=MyForm()
        
        try:
            i_plug_time=i.plug_time.f_time
        except Production.plug_time.RelatedObjectDoesNotExist:
            i_plug_time=""

        try:
            i_prod_time=i.prod_time.f_time
        except Production.prod_time.RelatedObjectDoesNotExist:
            i_prod_time=""
    
        try:            
            i_conv_time=i.conv_time.f_time
        except Production.conv_time.RelatedObjectDoesNotExist:
            i_conv_time=""

        try:
            i_start_time=i.start_time.f_time        
        except Production.start_time.RelatedObjectDoesNotExist:
            i_start_time=""

        a = {
            'field1':i.p_date,
            'field2':i.p_marking,
            'field3':i.p_batch,
            'field4':i.p_plan,
            'field5':i.p_apparatus,
            'field6':i.p_container,
            'field7':i.p_conveyor,
            'field8':i_app_time,            
            'field9':i_plug_time,
            'field10':i_prod_time,
            'field11':i_conv_time,
            'field12':i_start_time
        }
        records.append(a)
        
              

    
    context={'records':records, 'headers':headers}
    # return render(request, 'table_view.html', {'records':prod_records, 'headers':headers})
    return render(request, 'table_view22.html', context)
    
