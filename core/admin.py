from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.auth.admin import  UserAdmin as BaseUserAdmin
from store.admin import ProductAdmin, ProductImageInline
from store.models import Product
from tags.models import TaggedItem
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ('first_name', 'last_name',"username", "email", "password1", "password2"),
            },
        ),
    )


class TagInline(GenericTabularInline):
    model = TaggedItem
    autocomplete_fields = ['tag']
    extra: 0
    
class CustomeProductAdmin(ProductAdmin):
    inlines = [TagInline, ProductImageInline]
  

admin.site.unregister(Product)
admin.site.register(Product, CustomeProductAdmin)