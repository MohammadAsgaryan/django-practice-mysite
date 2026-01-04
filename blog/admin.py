from django.contrib import admin
from blog.models import post
# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'published_date', 'counted_views')
    list_filter = ('status', 'published_date')
    search_fields = ('title', 'content')
    ordering = ('-published_date',)
    
admin.site.register(post, PostAdmin)