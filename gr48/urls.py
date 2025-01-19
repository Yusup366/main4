from django.contrib import admin
from django.urls import path
from django.conf import settings
from posts.views import main_view , posts_list_view, posts_detail_view, posts_create_view
from user.views import register_view , login_view , logout_view
from django.conf.urls.static import static




urlpatterns = (
    [
     path('admin/', admin.site.urls),
     path('',main_view, name='main_view'),
     path('posts/',posts_list_view),
     path('posts/<int:post_id>/',posts_detail_view),
     path('posts/create/',posts_create_view),
     path('register/',register_view),
     path('login/',login_view),
     path('logout/',logout_view),
    ]
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
