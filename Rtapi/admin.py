from django.contrib import admin

# Register your models here.
from .models import Project,Scan
admin.site.register(Project)
admin.site.register(Scan)