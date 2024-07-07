from django.contrib import admin
from catalog.models import Product, Category, Blog, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'count_of_views', 'slug', 'is_published')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_number', 'version_name', 'is_active')


admin.site.site_header = "E-Market 2.0"
admin.site.site_title = "E-Market 2.0 Admin Panel"
admin.site.index_title = "Управление сайтом"
