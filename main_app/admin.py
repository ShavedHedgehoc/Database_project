from django.contrib import admin

# Register your models here.

""" from .models import Batch, Marking, Apparatus, Container, Conveyor
from .models import Suppose_times
from .models import Production, App_test_time, Conv_test_time, Plug_adm_time, Prod_adm_time """

from .models import Apparatus, Container, Conveyor, Batch, Marking
from .models import Production, App_time, Conv_time, Plug_time, Prod_time, Supp_time

admin.site.register(Apparatus)
admin.site.register(Container)
admin.site.register(Conveyor)
admin.site.register(Batch)
admin.site.register(Marking)
admin.site.register(Production)
admin.site.register(App_time)
admin.site.register(Conv_time)
admin.site.register(Plug_time)
admin.site.register(Prod_time)
admin.site.register(Supp_time)