from django.contrib import admin
from django.urls import path
from posts.views import main_view , posts_list_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main_view),
    path('posts/',posts_list_view),
]
