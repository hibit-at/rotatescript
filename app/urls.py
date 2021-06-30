from django.urls import path

from . import views

app_name = 'testapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('sample/',views.sample, name='sample'),
    path('download/',views.download, name='download'),
    path('angle/',views.angle,name='angle'),
]
