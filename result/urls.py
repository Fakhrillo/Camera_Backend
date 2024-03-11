from .views.result import *
from .views.config import *
from django.urls import path
from .views.photostream import *

urlpatterns = [
    path('result/', TrackedCreateAPIView.as_view()),
    path('images/', get_image_urls, name='get_image_urls'),
    path('tracked/<str:Cam_MxID>', GetTrackedAPIView.as_view()),
    path('last_data/', GetLastTrackedAPIView.as_view()),
    path('config/post/', ConfigurationPostAPIView.as_view()),
    path('photo/<str:Cam_MxID>', StreamPhotoUpdateView.as_view()),
    path('conf/<str:Cam_MxID>/', GetConfigurationsAPIView.as_view()),
]
