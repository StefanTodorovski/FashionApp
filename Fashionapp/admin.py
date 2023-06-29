from django.contrib import admin

from .models import UserProfile, Category, Product


class UserProfileAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return True


admin.site.register(UserProfile, UserProfileAdmin)


class CategoryAdmin(admin.ModelAdmin):
    exclude = ("created_by",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def has_view_permission(self, request, obj=None):
        return True


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    exclude = ("created_by",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def has_view_permission(self, request, obj=None):
        return True


admin.site.register(Product, ProductAdmin)
