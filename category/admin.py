from django.contrib import admin
from django.utils.html import format_html

from import_export.admin import ImportExportActionModelAdmin

from .models import Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(ImportExportActionModelAdmin):
    list_display = ["category_name", "slug", "image_tag"]
    # prepopulated_fields = {'slug': ('category_name',)}

    def image_tag(self, obj):
        if obj.category_img:
            return format_html(
                f'<img src="{obj.category_img.url}" style="width: 50px; height:50px;" />'
            )
        else:
            return "No hay Imagen"

    image_tag.allow_tags = True
    image_tag.short_description = "Category Img"
