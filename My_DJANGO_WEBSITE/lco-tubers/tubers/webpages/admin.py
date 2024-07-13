from django.contrib import admin
from .models import Slider,Group
from django.utils.html import format_html

# Register your models here.
class GroupAdmin(admin.ModelAdmin):
# editing the properties looks using the format_html
    def myphoto(self,object):
        return format_html('<img src="{}" width="40">'.format(object.photo.url))
    list_display=( 'id','myphoto','first_name','role')
    list_display_links= ('first_name', 'id')
    search_fields=('first_name','role')
    list_filter=('first_name','role')

    
admin.site.register(Slider)
admin.site.register(Group,GroupAdmin)