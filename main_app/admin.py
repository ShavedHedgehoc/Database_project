from django.contrib import admin

# Register your models here.

from .models import Batch, Marking, Apparatus, Container, Conveyor
from .models import Suppose_times
from .models import Production, App_test_time, Conv_test_time, Plug_adm_time, Prod_adm_time

admin.site.register(Batch)
admin.site.register(Marking)
admin.site.register(Apparatus)
admin.site.register(Container)
admin.site.register(Conveyor)
admin.site.register(Production)
admin.site.register(Suppose_times)
admin.site.register(App_test_time)
admin.site.register(Conv_test_time)
admin.site.register(Plug_adm_time)
admin.site.register(Prod_adm_time)
