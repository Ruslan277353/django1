from django.contrib import admin


from django.contrib import admin
from .models import NewsModel, NewsCategory, MyUserModel

@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    search_fields = ['category_name', 'id', 'date_added']
    list_filter = ['date_added']
    list_display = ['id', 'category_name', 'date_added']
    ordering = ['-id']
@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'id', 'date_added']
    list_filter = ['date_added']
    list_display = ['id', 'title', 'date_added']
    ordering = ['-id']
@admin.register(MyUserModel)
class MyUserModelAdmin(admin.ModelAdmin):
    search_fields = ['username', 'id']
    list_display = ['username', 'id', 'phone_number', 'email']
    ordering = ['-id']
