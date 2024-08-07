# Generated by Django 5.0.6 on 2024-07-07 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_blog_is_published"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
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
                (
                    "version_number",
                    models.PositiveIntegerField(verbose_name="Номер версии"),
                ),
                (
                    "version_name",
                    models.CharField(max_length=100, verbose_name="Название версии"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="Активная версия"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Версия продукта",
                "verbose_name_plural": "Версии продукта",
                "ordering": ["product", "version_number"],
            },
        ),
    ]
