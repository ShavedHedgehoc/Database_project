from django.shortcuts import render
from .models import production
from django.template import RequestContext


def index(request):    
    query_date="March 1, 2019"
    ##queryset=('SELECT * FROM main_app_boil WHERE date =%s' , [query_date])
    ##queryset='SELECT * FROM main_app_boil'
    ##records=boil.objects.raw('SELECT * FROM main_app_boil WHERE date =%s' , [query_date])
    ##records=boil.objects.raw('SELECT * FROM main_app_boil')
    records=production.objects.all()

    return render(request, 'table_view.html', locals())
# Create your views here.


## Кусок с запросом к серверу терминалов

##from django.shortcuts import render
##import requests
##import json
##
##def mydata():
##    response=requests.get("http://srv-webts:9000/MobileSMARTS/api/v1/Docs/Vzveshivanie")
##    get_data=response.json()
##    return get_data
##
##def index(request):
##    return render(request, 'webexample/main_page.html', {'vals':mydata()})


## Кусок кода с кнопкой загрузки и записи из Экселя

##from django.shortcuts import render
##from django.template import RequestContext
##from django.http import HttpResponseRedirect, HttpResponse
##from .models import my_table
##import pandas as pd
##
##def index(request):
##    all_records=my_table.objects.all()
##    if(request.GET.get('mybtn')):
##        return HttpResponseRedirect('upload')
##    else:
##        return render(request, 'table_view.html', locals())
##
##
##
##def upload(request):
##    if request.method=='POST':
##        cc=read_xl_file(request.FILES['myfile'])
##        for index, row in cc.iterrows():
##            table_c=my_table()
##            table_c.t_Date=row['t_Date']
##            table_c.t_Art=row['t_Art']
##            table_c.t_Batch=row['t_Batch']
##            table_c.t_Plan=row['t_Plan']
##            table_c.t_App=row['t_App']
##            table_c.save()
##        #     c=my_table.objects.create()
##        return render(request, 'success.html', locals())
##    return render(request, 'upload.html')
##
##def read_xl_file(r_file):
##    xl = pd.ExcelFile(r_file)
##    sh=xl.sheet_names[0]
##    r_df=pd.read_excel(xl, sheet_name=sh)
##    return r_df
