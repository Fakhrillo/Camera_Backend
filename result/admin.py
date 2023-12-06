from django.contrib import admin
from .models import Tracked, ConfigParameter, StreamPhoto
# Register your models here.
from django.contrib.auth.models import Group
admin.site.unregister(Group)

admin.site.register(StreamPhoto)

admin.site.register(ConfigParameter)

class TrackedModel(admin.ModelAdmin):
    list_display = ('Cam_MxID', 'incoming', 'outgoing', 'present', 'created_at',)

admin.site.register(Tracked, TrackedModel)
