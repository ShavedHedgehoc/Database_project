from django.contrib import admin

# Register your models here.
from .models import apparatus, conveyor, container, production, lab_adm2


admin.site.register(apparatus)
admin.site.register(conveyor)
admin.site.register(container)
admin.site.register(production)
admin.site.register(lab_adm2)