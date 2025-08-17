import csv
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from shop.models import Category, Product

class Command(BaseCommand):
    help = "Import products from CSV (category,name,price,quantity,stock)"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Path to CSV file")

    def handle(self, *args, **kwargs):
        csv_file = kwargs["csv_file"]

        with open(csv_file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                category_name = row["category"].strip()
                name = row["name"].strip()
                price = float(row["price"])
                quantity = int(row["quantity"])
                stock = int(row["stock"])

                # Get or create category
                category, _ = Category.objects.get_or_create(
                    name=category_name,
                    defaults={"slug": slugify(category_name)},
                )

                # Generate unique slug
                base_slug = slugify(name)
                slug = base_slug
                counter = 1
                while Product.objects.filter(slug=slug).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1

                # Create product
                Product.objects.create(
                    category=category,
                    name=name,
                    slug=slug,
                    price=price,
                    quantity=quantity,
                    stock=stock,
                )

                self.stdout.write(self.style.SUCCESS(f"Added product: {name}"))
