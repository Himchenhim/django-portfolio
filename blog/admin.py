from django.contrib import admin
from .models import Article


class YourModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, YourModelAdmin)
