from django.contrib import admin
from django.urls import path
from main.views import homepage_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name='homepage'),  # Homepage view
]