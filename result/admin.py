from django.contrib import admin
from .models import Tracked, ConfigParameter, StreamPhoto
# Register your models here.
from django.contrib.auth.models import Group
admin.site.unregister(Group)

@admin.register(StreamPhoto)
class StreamPhoto(admin.ModelAdmin):
    list_display = ('id', 'Cam_MxID', 'image')
    list_display_links = ['id', 'Cam_MxID']
    search_fields = ('id', 'Cam_MxID')
    list_filter = ['Cam_MxID']


@admin.register(ConfigParameter)
class ConfigParameter(admin.ModelAdmin):
    list_display = ('id', 'Cam_MxID')
    list_display_links = ['id', 'Cam_MxID']
    list_filter = ['Cam_MxID' ]
    search_fields = ('id', 'Cam_MxID')
    

@admin.register(Tracked)
class TrackedModel(admin.ModelAdmin):
    list_display = ('Cam_MxID', 'incoming', 'outgoing', 'present', 'created_at',)

    search_fields = ('id', 'Cam_MxID')

    list_filter = ['Cam_MxID']