from django.contrib import admin
from .models import Project


class YourModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, YourModelAdmin)
