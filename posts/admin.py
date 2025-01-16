from django.contrib import admin
from posts.models import Post , Categoty,Tag


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'rate', 'created_at')
    list_filter = ('category', 'tags')
    search_fields = ('title','description','tage__name')

admin.site.register(Categoty)
admin.site.register(Tag)

