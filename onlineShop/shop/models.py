from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    image = models.BinaryField(editable=True)

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
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    