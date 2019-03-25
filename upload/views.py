import pandas as pd
import os
# import magic
import openpyxl
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import File_upload_form
from xlrd import XLRDError
from django.shortcuts import render_to_response
import xlrd
from main_app.models import Production, Batch, Marking
from main_app.models import Apparatus, Container, Conveyor
from datetime import datetime
from django.views.generic.edit import FormView
from django.views.generic import ListView
class Prod_View(ListView):
    model=Production
    template_name='prod.html'

# class File_form_view(FormView):
#     template_name='upload.html'
#     form_class=File_upload_form
#     success_url='success-pafge.html'

#     def form_valid(self,form):        
#         return super(File_form_view, self).form_valid(form)

def get_date(date_str):
    """ Функция для преобразования даты из DataFrame(str).
    Преобразует значаение вида "ГГГГ-ММ-ДД ЧЧ-ММ-СС"
    в значение вида "ГГГГ-ММ-ДД" """
    full_date = datetime.strptime(date_str,'%Y-%m-%d %H:%M:%S')
    short_date = full_date.strftime('%Y-%m-%d')
    return short_date


def nan_value_check(d_frame):
    """Возвращает два списка и Boolean: первый список - номера строк,
    в которых присутствуют пустые значения, второй список - номера полностью пустых строк.
    True - если эти списки не пустые"""
    list_full_nan=d_frame[d_frame.isnull().sum(axis=1)==7].index.tolist()
    list_nan=d_frame[(d_frame.isnull().sum(axis=1)>1) & (d_frame.isnull().sum(axis=1)<7)].index.tolist()
    if (len(list_nan)==0) and (len(list_full_nan)==0):
        nan_value=False
    else:
        nan_value=True
    return list_nan, list_full_nan, nan_value




def upload(request):    
    if request.method == "POST":
        form = File_upload_form(request.POST, request.FILES)
        if form.is_valid():            
            excel_file = request.FILES['filename']
            df = xl_file_proc(excel_file)  
            if df[1] != "Pass":
                form = File_upload_form()
                
                context = {'msg': df[1],'form':form}
                # return render(request, 'upload.html', context)
            else:
                df_to_append = df[0]
                nan_lists=nan_value_check(df_to_append)
                if not nan_lists[2]:                    
                    return HttpResponseRedirect(reverse('success'))
                else:
                    # form = File_upload_form()
                    context = {'msg': 
                    str(excel_file)+": \n"
                    "В загружаемом файле присутствуют следующие ошибки: \n"+
                    "Строки с пустыми значениями: " +str(len(nan_lists[0])) +"\n"+
                    "Полностью пустые строки: "+str(len(nan_lists[1])),
                    'form':form}
        else:
            msg=""
            context={'msg': msg,'form':form}
            
    else:
        form = File_upload_form()
        msg=""
        context={'msg':msg,'form':form}
    
    return render(request, 'upload.html', context)


def xl_file_proc(file_obj):
    """ Проверяем, совпадают ли заголовки с контрольными.
        При видимом совпадении заголовков, но при наличии лишнего столбца, 
        в df_headers присутствует лишний, пустой заголовок, по этому, 
        условие не выполняется"""
    headers_to_compare = [
        "date",
        "marking", 
        "batch", 
        "plan", 
        "apparatus", 
        "container", 
        "conveyor", 
    ]
    err_msg_list=[
        "Заголовки таблицы не совпадают с контрольными",
        "В файле нет данных, кроме заголовка",
        "Pass",
    ]
    xl = pd.ExcelFile(file_obj)
    sh = xl.sheet_names[0]
    r_df = pd.read_excel(xl, sheet_name = sh, dtype = str)
    if r_df is not None:
        df_count = len(r_df.index)
        df_headers = list(r_df.columns.values)        
        if df_headers != headers_to_compare:
            r_df = None
            err_msg = err_msg_list[0]
        else:
            if df_count == 0:
                r_df = None
                err_msg = err_msg_list[1]
            else:
                err_msg = err_msg_list[2]
    return r_df, err_msg




# def read_xl_file(r_file):
#     """ Функция возвращает список, состоящий из DataFrame и кода ошибки.
#     Анализируется только тип файла, заголовки и рамерность полученной
#     матрицы данных. Наличие пустых строк и пустых значений - в другой функции.
#     В случае ошибки - DataFrame = None, err_msg - сообщение для вывода
#     на страницу. При успешной загрузке - err_msg = Pass """
#     headers_to_compare = [  # Список заголовков загружаемого файла
#         "date",  # (используется для проверки назначения файла и размерности)
#         "marking",
#         "batch",
#         "plan",
#         "apparatus",
#         "container",
#         "conveyor"
#     ]
#     try:
#         # Пытаемся переименовать файл, если файл открыт - получаем IOError
#         os.rename(r_file, 'nameforisopenedcheck.xlsx')
#         os.rename('nameforisopenedcheck.xlsx', r_file)
#         xl = pd.ExcelFile(r_file)
#         sh = xl.sheet_names[0]
#         r_df = pd.read_excel(xl, sheet_name=sh, dtype=str)
#     except FileNotFoundError:  # Переданного файла не существует
#         r_df = None
#         err_msg = "Файла не существует"
#     except XLRDError:  # Попытка открыть не-Excel-файл с помощью XLRD
#         r_df = None
#         err_msg = "Файл не является файлом .xls .xlsx"
#     except IOError:  # Файл где-то открыт
#         r_df = None
#         err_msg = "Файл открыт. Закройте файл и попробуйте еще раз"
#     finally:
#         if r_df is not None:
#             df_count = len(r_df.index)
#             df_headers = list(r_df.columns.values)
#             """ Проверяем, совпадают ли заголовки с контрольными.
#             При видимом совпадении заголовков, но при наличии лишнего столбца,
#             в df_headers присутствует лишний, пустой заголовок, по этому,
#             условие не выполняется"""
#             if df_headers != headers_to_compare:
#                 r_df = None
#                 err_msg = "Заголовки таблицы не совпадают с контрольными"
#             else:
#                 if df_count == 0:
#                     r_df = None
#                     err_msg = "В файле нет данных, кроме заголовка"
#                 else:
#                     err_msg = "Pass"
#     return r_df, err_msg
# def rx(excel_file):
#     xl = pd.ExcelFile(excel_file)
#     sh = xl.sheet_names[0]
#     r_df = pd.read_excel(xl, sheet_name=sh, dtype=str)
#     return r_df


# def uploadfile1(filename):
#     BASE_DIR = os.path.split(__file__)
#     destination = os.path.join(BASE_DIR[0], filename.name)
#     with open(destination, 'wb+') as dest:
#         for chunk in filename:
#             dest.write(chunk)

#     return HttpResponseRedirect(reverse('success'))


# def uploadfile(request, filename):

#     df = read_xl_file(r'D:\Project\Database_project\upload\1.xlsm')
#     # if df[1] != "Pass":
    #     context = {'msg': df[1]}
    #     return render(request, 'err-page.html', context)
    # else:
    #     df_to_append = df[0]
    #     for index, row in df_to_append.iterrows():
    #         marking, _ = Marking.objects.get_or_create(
    #             r_name = row['marking'])
    #         u""" get_or_create возвращает объект модели и Boolean(True - создали
    #         новый объект, False - вернули существующий). Подчеркивание -
    #         пропускаем ненужное значение """
    #         batch, _ = Batch.objects.get_or_create(r_name = row['batch'])
    #         apparatus, _ = Apparatus.objects.get_or_create(
    #             rd_name = row['apparatus'])
    #         container, _ = Container.objects.get_or_create(
    #             rd_name = row['container'])
    #         conveyor, _ = Conveyor.objects.get_or_create(
    #             rd_name = row['conveyor'])
    #         new_prod_obj = Production.objects.create(
    #             p_date = get_date(row['date']), 
    #             p_marking = marking, 
    #             p_batch = batch, 
    #             p_apparatus = apparatus, 
    #             p_container = container, 
    #             p_conveyor = conveyor)
    #     context = {
    #         'msg': "Добавлено " + str(len(df_to_append)) + " новых строк"
    #     }
    #     return render(request, 'success-page.html', context)
