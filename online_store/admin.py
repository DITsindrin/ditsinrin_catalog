from django.contrib import admin

from online_store.models import CategoryProduct, Product, Contacts


# Register your models here.
@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'parent_category',)
    search_fields = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'price', 'date_creation', 'last_modified_date',)
    list_filter = ('category',)
    search_fields = ('title',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'inn', 'address', 'support_email',)
