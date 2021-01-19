from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = [
        'company_name',
        'first_name',
        'last_name',
        'username',
        'phone',
        'address',
    ]
    list_display = ['company_name', 'username', 'phone']
