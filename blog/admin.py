from django.contrib import admin
from .models import Blog, Category 
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=['title','Category','author','status','is_featured']
    search_fields=('id','title','category__category_name','status')
    list_editable=('is_featured',)
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
# Register your models here.
