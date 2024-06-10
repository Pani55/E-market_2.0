import json

from django.core.management import BaseCommand

from catalog.models import Product, Category

file_path = 'catalog.json'


class Command(BaseCommand):

    @staticmethod
    def json_read(path_to_file):
        with open(path_to_file, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read(file_path):
            if category['model'] == 'catalog.category':
                category_for_create.append(
                    Category(pk=category['pk'],
                             name=category['fields']['name'],
                             description=category['fields']['description'])
                )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read(file_path):
            if product['model'] == 'catalog.product':
                product_for_create.append(
                    Product(pk=product['pk'],
                            name=product['fields']['name'],
                            description=product['fields']['description'],
                            photo=product['fields']['photo'],
                            category=Category.objects.get(
                                pk=product['fields']['category']),
                            price=product['fields']['price'])
                )

        Product.objects.bulk_create(product_for_create)
