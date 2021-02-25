from django.contrib import admin
from .models import Photos


class PhotosAdmin(admin.ModelAdmin):
    list_display = ['gender']
    list_filter = ['gender']
    search_fields = ['gender']


admin.site.register(Photos, PhotosAdmin)
