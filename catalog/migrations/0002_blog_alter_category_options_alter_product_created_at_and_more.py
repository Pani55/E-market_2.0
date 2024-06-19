# Generated by Django 5.0.6 on 2024-06-19 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Заголовок")),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        max_length=150,
                        null=True,
                        unique=True,
                        verbose_name="slug",
                    ),
                ),
                ("content", models.TextField(verbose_name="Содержание")),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="blog/preview",
                        verbose_name="Превью",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(auto_now_add=True, verbose_name="Дата создания"),
                ),
                (
                    "count_of_views",
                    models.IntegerField(verbose_name="колличество просмотров"),
                ),
            ],
        ),
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["name"],
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateField(auto_now_add=True, verbose_name="Дата создания"),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateField(
                auto_now_add=True, verbose_name="Дата последнего изменения"
            ),
        ),
    ]
