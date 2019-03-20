"""new_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [    
    url(r'^$', views.index, name='index'),    
    url(r'^2$', views.table_view, name='table_view'),
    path('add_adm/<slug:t_name>/<int:id>',views.add_adm, name='add_adm'),
    path('edit_adm/<slug:t_name>/<int:id>',views.edit_adm, name='edit_adm'), 
    path('success', views.success, name='success'),   
    path('errorpage', views.errorpage, name='errorpage'),   
]
