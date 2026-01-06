from django.contrib import admin
from blog.models import Post
# Register your models here.



class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'status', 'created_date', 'counted_views')
    list_filter = ('status', 'created_date')
    search_fields = ('title', 'content')
    ordering = ('-created_date',)
    
    
admin.site.register(Post, PostAdmin)