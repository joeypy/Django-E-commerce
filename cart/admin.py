from django.contrib import admin
from .models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "cart_id", "date_added")
    list_filter = ("cart_id",)
    list_display_links = ("cart_id",)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "cart", "quantity", "is_active")
    list_filter = ("product", "cart", "is_active")
    list_display_links = ("product",)
