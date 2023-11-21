from django.contrib import admin
from .models import Tracked, ConfigParameter, StreamPhoto
# Register your models here.

admin.site.register(StreamPhoto)



admin.site.register(ConfigParameter)

class TrackedModel(admin.ModelAdmin):
    list_display = ('mxid', 'incoming', 'outgoing', 'created_at',)

admin.site.register(Tracked, TrackedModel)