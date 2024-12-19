# myapp/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Product, Category, Order, OrderItem, Review, Message

class CustomUserAdmin(UserAdmin):
    # Ovdje možete prilagoditi kako će izgledati 'User' model u adminu
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')

admin.site.unregister(User)  # Uklonite prethodnu registraciju
admin.site.register(User, CustomUserAdmin)  # Ponovno registrirajte s prilagodbama

#modeli____________________________________________________________________________________________________________
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone_number', 'is_seller')  # Polja koja želiš vidjeti u admin panelu
    list_filter = ('is_seller',)  # Opcionalno, filtriranje po statusu prodavača
    search_fields = ('user__username', 'address', 'phone_number', 'bio')  # Opcionalno, omogućuje pretraživanje

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'is_available')  # Polja koja želiš vidjeti u admin panelu
    list_filter = ('is_available',)  # Opcionalno, filtriranje po dostupnosti
    search_fields = ('name', 'description')  # Opcionalno, omogućuje pretraživanje
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'created_at', 'is_completed', 'total_price')
    list_filter = ('is_completed',)
    search_fields = ('buyer__user__username',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    search_fields = ('order__id', 'product__name')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('product__name', 'user__user__username')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'is_read', 'created_at')
    list_filter = ('is_read',)
    search_fields = ('sender__user__username', 'receiver__user__username')
