import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from store.models import Product

def populate():
    Product.objects.all().delete()
    products = [
        {"name": "Sony Wireless Noise Canceling Headphones", "price": 348.00, "link": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=300&q=80"},
        {"name": "Apple MacBook Air 13-inch Laptop", "price": 999.00, "link": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=300&q=80"},
        {"name": "Apple iPhone 15 Pro Max", "price": 1199.00, "link": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=300&q=80"},
        {"name": "Samsung 27-inch Curved Monitor", "price": 189.99, "link": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=300&q=80"},
        {"name": "Logitech MX Master 3S Wireless Mouse", "price": 99.99, "link": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?auto=format&fit=crop&w=300&q=80"},
        {"name": "Mechanical Gaming Keyboard RGB", "price": 49.99, "link": "https://images.unsplash.com/photo-1595225476474-87563907a212?auto=format&fit=crop&w=300&q=80"},
        {"name": "Apple Watch Series 9 Smartwatch", "price": 399.00, "link": "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?auto=format&fit=crop&w=300&q=80"},
        {"name": "Canon EOS Rebel T7 DSLR Camera", "price": 479.00, "link": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?auto=format&fit=crop&w=300&q=80"},
        {"name": "Apple iPad Pro 12.9-inch", "price": 1099.00, "link": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?auto=format&fit=crop&w=300&q=80"},
        {"name": "DJI Mini 3 Pro Drone", "price": 759.00, "link": "https://images.unsplash.com/photo-1507582020474-9a35b7d455d9?auto=format&fit=crop&w=300&q=80"},
        {"name": "TP-Link AX1800 WiFi 6 Router", "price": 74.99, "link": "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&w=300&q=80"},
        {"name": "Echo Dot (5th Gen) Smart Speaker", "price": 49.99, "link": "https://images.unsplash.com/photo-1543512214-318c7553f230?auto=format&fit=crop&w=300&q=80"},
        {"name": "LG 65-Inch Class OLED Smart TV", "price": 1496.99, "link": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?auto=format&fit=crop&w=300&q=80"},
        {"name": "Meta Quest 2 Advanced VR Headset", "price": 299.99, "link": "https://images.unsplash.com/photo-1622979135225-d2ba269cf1ac?auto=format&fit=crop&w=300&q=80"},
        {"name": "PlayStation 5 Console", "price": 499.00, "link": "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?auto=format&fit=crop&w=300&q=80"},
        {"name": "SanDisk 1TB Extreme Portable SSD", "price": 119.99, "link": "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?auto=format&fit=crop&w=300&q=80"},
        {"name": "Blue Yeti USB Microphone", "price": 129.99, "link": "https://images.unsplash.com/photo-1590602847861-f357a9332bbc?auto=format&fit=crop&w=300&q=80"},
        {"name": "GIGABYTE GeForce RTX 4070 GPU", "price": 599.99, "link": "https://images.unsplash.com/photo-1591488320449-011701bb6704?auto=format&fit=crop&w=300&q=80"},
        {"name": "Apple AirPods Pro (2nd Gen)", "price": 249.00, "link": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?auto=format&fit=crop&w=300&q=80"},
        {"name": "CyberPowerPC Gamer Xtreme VR Gaming PC", "price": 999.99, "link": "https://images.unsplash.com/photo-1587831990711-23ca6441447b?auto=format&fit=crop&w=300&q=80"},
        {"name": "Bose QuietComfort 45 Headphones", "price": 329.00, "link": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?auto=format&fit=crop&w=300&q=80"},
        {"name": "Nintendo Switch OLED Model", "price": 349.99, "link": "https://images.unsplash.com/photo-1617096200347-cb04ae810b1d?auto=format&fit=crop&w=300&q=80"},
        {"name": "GoPro HERO11 Black Action Camera", "price": 399.99, "link": "https://images.unsplash.com/photo-1565329921943-7e537b7a2ea9?auto=format&fit=crop&w=300&q=80"},
        {"name": "Amazon Kindle Paperwhite (8GB)", "price": 139.99, "link": "https://images.unsplash.com/photo-1544816155-12df9643f363?auto=format&fit=crop&w=300&q=80"}
    ]
    for p in products:
        Product.objects.create(name=p["name"], price=p["price"], description="Amazing product!", image_link=p["link"])
    print("Database populated with 20 products with reliable Unsplash images.")

if __name__ == '__main__':
    populate()
