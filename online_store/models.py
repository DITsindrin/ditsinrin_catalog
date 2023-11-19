from __future__ import annotations
from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class CategoryProduct(models.Model):
    title = models.CharField(max_length=250, verbose_name='название категории')
    description = models.TextField(verbose_name='описание категории')
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE,
                                        verbose_name='родительская категория')

    # created_at = models.DateTimeField(auto_now_add=True, **NULLABLE, verbose_name='дата создания')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    title = models.CharField(max_length=250, verbose_name='название продукта')
    description = models.TextField(verbose_name='описание продукта')
    image = models.ImageField(default='default.png', upload_to='product_img', **NULLABLE,
                              verbose_name='изображение товара')
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='категория продукта')
    price = models.IntegerField(verbose_name='цена продукта')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return f'{self.title} {self.category} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Contacts(models.Model):
    country = models.CharField(max_length=100, verbose_name='страна')
    inn = models.CharField(max_length=50, verbose_name='ИНН')
    address = models.CharField(max_length=250, verbose_name='адресс')
    support_email = models.EmailField(max_length=254, verbose_name='support email')

    def __str__(self):
        return f'{self.country} {self.inn} {self.address} {self.support_email}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
