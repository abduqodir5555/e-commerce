from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import User, VerificationOtp, UserAddress

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', )

@admin.register(VerificationOtp)
class VeirificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'code', 'expires_in')

@admin.register(UserAddress)
class UserAdresAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'street')

# class UserAdmin(UserAdmin):
#     list_display = ('email', 'first_name', 'last_name', 'is_staff')
#     ordering = ('email', )

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
