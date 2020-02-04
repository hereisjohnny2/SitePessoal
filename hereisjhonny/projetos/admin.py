from django.contrib import admin
from .models import Project, Colaborator, PrintImage

# Register your models here.
admin.site.register(Project)
admin.site.register(Colaborator)
admin.site.register(PrintImage)
