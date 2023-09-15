from django.contrib import admin
from .models import Rock

# class rockAdmin(admin.ModelAdmin):
#     list_display=['image']

admin.site.register(Rock)
