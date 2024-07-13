from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html

class YtAdmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src="{}" width="40">'.format(object.photo.url))

    list_display=('id','myphoto','name','camera_type','sub_count','is_featured')
    list_display_links= ('camera_type','name','myphoto')
    search_fields=('name','crew','is_featured')
    list_filter=('is_featured','camera_type','crew','city')
    list_editable=('is_featured',)
admin.site.register(Youtuber,YtAdmin) 