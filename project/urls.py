
from django.contrib import admin
from django.urls import path, include
from main.views import HomeView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('home', HomeView.as_view(), name='home')
]