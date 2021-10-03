from django.contrib import admin
from django.utils.html import format_html
from import_export.admin import ImportExportActionModelAdmin

from store.models import Product, Variation


@admin.register(Product)
class ProductAdmin(ImportExportActionModelAdmin):
    list_display = (
        "id",
        "product_name",
        "price",
        "stock",
        "category",
        "modified_at",
        "is_available",
        "image_tag",
    )
    list_display_links = (
        "id",
        "product_name",
    )
    ordering = ("id",)
    readonly_fields = ("slug",)

    def image_tag(self, obj):
        if obj.images:
            return format_html(
                f'<img src="{obj.images.url}" style="width: 50px; height:50px;" />'
            )
        else:
            return "No Image"

    image_tag.allow_tags = True
    image_tag.short_description = "Product Img"


@admin.register(Variation)
class VariationAdmin(ImportExportActionModelAdmin):
    list_display = (
        "id",
        "product",
        "variation_category",
        "variation_value",
        "is_active",
        "created_at",
    )
    list_editable = ("is_active",)
    list_filter = ("product", "variation_category", "variation_value",)

