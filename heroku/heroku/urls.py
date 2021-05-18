from django.contrib import admin
from django.urls import path
import herokuApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', herokuApp.views.main, name='main'),
    path('new/create', herokuApp.views.create, name='create')
]