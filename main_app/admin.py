from django.contrib import admin

# Register your models here.
from .models import apparatus, conveyor, container, production


admin.site.register(apparatus)
admin.site.register(conveyor)
admin.site.register(container)
admin.site.register(production)
