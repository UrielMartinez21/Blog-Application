from django.contrib import admin
from blog.models import Post

# This is a way to register the Post model with the admin site
# admin.site.register(Post)

# This is another way to register the Post model with the admin site
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status') # This is the list of fields to display in the admin list view
    list_filter = ('status', 'publish')                             # This is the list of fields to filter the results by
    search_fields = ('title', 'author')                             # This is the list of fields to search the results by
    prepopulated_fields = {'slug': ('title',)}                      # This is the field to populate automatically with the value of other fields
    raw_id_fields = ('author',)                                     # This is the field to display as a lookup widget
    date_hierarchy = 'publish'                                      # This is the field to display as a date hierarchy
    ordering = ('status', 'publish')                                # This is the list of fields to order the results by