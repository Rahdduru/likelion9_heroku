from django.contrib import admin
from django.urls import path, include
import herokuApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', herokuApp.views.home, name='home'),
    path('post/', herokuApp.views.post, name ='post'),
    path('create/', herokuApp.views.create, name='create'),
    path('edit/<str:id>/', herokuApp.views.edit, name='edit'),
]