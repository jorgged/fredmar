from django.contrib import admin
from .models import Category, Product, Product_card, Tag, Contacto, carousel, logo

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','brand','model','year','price','stock','is_active',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name','brand', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
admin.site.register(Category, CategoryAdmin)

class Product_card_Admin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name', 'description',]
    list_per_page = 20
admin.site.register(Product_card, Product_card_Admin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name', 'description',]
    list_per_page = 20
admin.site.register(Tag, TagAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('created_at','name','subject','email','message',)
    search_fields = ['name', 'subject','email','message',]
    list_per_page = 20
admin.site.register(Contacto, ContactAdmin)

class carouselAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name',]
    list_per_page = 20
admin.site.register(carousel, carouselAdmin)

class logoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name',]
    list_per_page = 20
admin.site.register(logo, logoAdmin)