# myapp/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    # Ovdje možete prilagoditi kako će izgledati 'User' model u adminu
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')

admin.site.unregister(User)  # Uklonite prethodnu registraciju
admin.site.register(User, CustomUserAdmin)  # Ponovno registrirajte s prilagodbama
