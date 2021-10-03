from django.db.models import Model, CharField, TextField, ImageField
from autoslug import AutoSlugField
from django.urls import reverse


# Create your models here.
class Category(Model):
    category_name = CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from="category_name")
    description = TextField(max_length=255, blank=True)
    category_img = ImageField(upload_to="photo/categories", blank=True)

    def get_url(self):
        return reverse("products_by_category", args=[self.slug])

    def __str__(self) -> str:
        return self.category_name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
