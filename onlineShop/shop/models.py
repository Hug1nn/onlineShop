from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True, default='category')
    description = models.TextField(blank=True)
    image = models.BinaryField(editable=True, blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse()


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete = 'cascade')
    name = models.CharField(max_length=250, db_index=True, default='product')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    