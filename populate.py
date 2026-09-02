import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from store.models import Product

def populate():
    products = [
        {"name": "Laptop", "price": 999.99, "description": "High performance laptop for work and gaming."},
        {"name": "Smartphone", "price": 499.99, "description": "Latest model smartphone with a great camera."},
        {"name": "Headphones", "price": 149.99, "description": "Noise-cancelling over-ear headphones."},
        {"name": "Keyboard", "price": 49.99, "description": "Mechanical keyboard with RGB lighting."},
        {"name": "Mouse", "price": 29.99, "description": "Wireless ergonomic mouse."},
        {"name": "Monitor", "price": 199.99, "description": "27-inch 4K monitor."},
    ]

    for p in products:
        Product.objects.get_or_create(name=p["name"], price=p["price"], description=p["description"])
    
    print("Database populated with sample products.")

if __name__ == '__main__':
    populate()
