from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название категории товаров')

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name


class Merchandise(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Название категории товаров")
    name = models.CharField(max_length=128, verbose_name="Наименование товара")
    manufacturer = models.CharField(max_length=128, verbose_name="Фирма производитель")
    price = models.PositiveBigIntegerField(verbose_name="Цена")

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class MerchandiseImg(models.Model):
    image = models.ImageField(upload_to="static/img", verbose_name="Изображение товара")
    product = models.ForeignKey(Merchandise, on_delete=models.CASCADE, verbose_name="Товар")

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'

    def __str__(self):
        return f'Картинка товара - {self.product}'
