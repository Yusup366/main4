from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from posts.views import main_view , posts_list_view, posts_detail_view



urlpatterns = (
    [
     path('admin/', admin.site.urls),
     path('',main_view),
     path('posts/',posts_list_view),
     path('posts/<int:post_id>/',posts_detail_view),
    ]
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
