from django.contrib import admin
from django.urls import path
from posts.views import main_view, html_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',main_view),
    path('html/',html_view),
]
