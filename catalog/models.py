from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название категории"
    )
    description = models.TextField(
        verbose_name="Описание категории",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название продукта"
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        blank=True,
        null=True
    )
    photo = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Фото продукта"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        related_name="products",
        blank=True,
        null=True
    )
    price = models.IntegerField(
        verbose_name="Цена продукта"
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения",
        auto_now_add=True,
        editable=False
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "created_at", "updated_at", "price"]

    def __str__(self):
        return f"{self.name}, {self.category}, {self.price}"


class Blog(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок"
    )
    slug = models.SlugField(
        max_length=150,
        verbose_name="slug",
        unique=True,
        blank=True,
        null=True
    )
    content = models.TextField(
        verbose_name="Содержание"
    )
    preview = models.ImageField(
        upload_to="blog/preview",
        blank=True,
        null=True,
        verbose_name="Превью"
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
        auto_now_add=True,
        editable=False
    )
    is_published = models.BooleanField(
        verbose_name="Опубликовано",
        default=False
    )
    count_of_views = models.PositiveIntegerField(
        verbose_name="колличество просмотров",
        default=0
    )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["created_at", "count_of_views"]

    def __str__(self):
        return f"{self.title}, {self.slug}, {self.created_at}, {self.count_of_views}, {self.is_published}"


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт"
    )
    version_number = models.PositiveIntegerField(
        verbose_name="Номер версии"
    )
    version_name = models.CharField(
        max_length=100,
        verbose_name="Название версии"
    )
    is_active = models.BooleanField(
        verbose_name="Активная версия",
        default=False
    )

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продукта"
        ordering = ["product", "version_number"]

    def __str__(self):
        return f"{self.product}, {self.version_number}, {self.version_name}, {self.is_active}"
