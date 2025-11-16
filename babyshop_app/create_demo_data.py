import os
import django
import random
from django.utils.text import slugify


# Ensure being in project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)


# Telling Django where settings.py is
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "babyshop.settings")


# Initializing Django
django.setup()


# Importing the models
from products.models import Category, Product


def run():
    categories = {
        "Strollers": [
            ("Luxury Stroller X1", "High-quality stroller with excellent suspension."),
            ("City Mini Stroller", "Lightweight and perfect for urban environments."),
            ("Comfort Stroller Pro", "Extra storage and full reclining comfort.")
        ],
        "Baby Toys": [
            ("Wooden Rattle", "Eco-friendly wooden rattle for infants."),
            ("Cuddly Bear", "Soft plush bear for newborns.")
        ],
        "Clothing": [
            ("Baby Body Blue", "Soft cotton baby body in blue."),
            ("Baby Hat", "Cute organic cotton baby hat."),
            ("Warm Onesie", "Perfect for colder days.")
        ],
        "Care Products": [
            ("Natural Baby Oil", "Pure and gentle baby oil."),
            ("Mild Wash Lotion", "Gentle cleansing for sensitive baby skin."),
        ],
        "Safety Products": [
            ("Door Safety Gate", "Prevents access to unsafe areas."),
            ("Drawer Locks", "Essential child safety for drawers and cupboards."),
        ]
    }

    for cat_name, products in categories.items():
        slug = slugify(cat_name)
        category, created = Category.objects.get_or_create(
            name=cat_name, slug=slug
        )
        print(f"Category: {cat_name} ({'created' if created else 'exists'})")

        for product_name, description in products:
            price = round(random.uniform(9.00, 199.00), 2)

            product, created = Product.objects.get_or_create(
                name=product_name,
                defaults={
                    "description": description,
                    "price": price,
                    "category": category,
                }
            )
            print(f"  Product: {product_name} ({'created' if created else 'exists'})")

    print("\nDemo data successfully created!")


if __name__ == "__main__":
    run()
