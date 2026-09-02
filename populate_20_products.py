import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from store.models import Product

def populate():
    # Clear existing
    Product.objects.all().delete()
    
    products = [
        {"name": "Echo Dot (5th Gen) | Smart speaker with Alexa", "price": 49.99, "img": "https://m.media-amazon.com/images/I/71C3oJLtzIL._AC_UL320_.jpg"},
        {"name": "Fire TV Stick 4K Max streaming device", "price": 54.99, "img": "https://m.media-amazon.com/images/I/41zF1k2j-dL._AC_UL320_.jpg"},
        {"name": "Apple AirPods Pro (2nd Generation)", "price": 249.00, "img": "https://m.media-amazon.com/images/I/61SUj2aKoEL._AC_UL320_.jpg"},
        {"name": "Sony WH-1000XM5 Wireless Noise Canceling Headphones", "price": 398.00, "img": "https://m.media-amazon.com/images/I/51aXvjzcukL._AC_UL320_.jpg"},
        {"name": "Logitech MX Master 3S Wireless Performance Mouse", "price": 99.99, "img": "https://m.media-amazon.com/images/I/61ni3t1ryQL._AC_UL320_.jpg"},
        {"name": "Keychron K2 Wireless Mechanical Keyboard", "price": 79.99, "img": "https://m.media-amazon.com/images/I/61cGzQj+FHL._AC_UL320_.jpg"},
        {"name": "Samsung 49\" Odyssey G9 Gaming Monitor", "price": 1299.99, "img": "https://m.media-amazon.com/images/I/81r8JazRcoL._AC_UL320_.jpg"},
        {"name": "Apple MacBook Air Laptop: M1 Chip, 13” Retina Display", "price": 899.00, "img": "https://m.media-amazon.com/images/I/71jG+e7roXL._AC_UL320_.jpg"},
        {"name": "Nintendo Switch with Neon Blue and Neon Red Joy-Con", "price": 299.99, "img": "https://m.media-amazon.com/images/I/61-PblYntsL._AC_UL320_.jpg"},
        {"name": "PlayStation 5 Console", "price": 499.99, "img": "https://m.media-amazon.com/images/I/51051FiD9AQ._AC_UL320_.jpg"},
        {"name": "Xbox Series X Console", "price": 499.99, "img": "https://m.media-amazon.com/images/I/51ojzJk77qL._AC_UL320_.jpg"},
        {"name": "Meta Quest 2 — Advanced All-In-One Virtual Reality Headset", "price": 299.99, "img": "https://m.media-amazon.com/images/I/61tE7IcuLmL._AC_UL320_.jpg"},
        {"name": "GoPro HERO11 Black - Waterproof Action Camera", "price": 399.99, "img": "https://m.media-amazon.com/images/I/61k8-2J7IeL._AC_UL320_.jpg"},
        {"name": "Kindle Paperwhite (8 GB) – Now with a 6.8\" display", "price": 139.99, "img": "https://m.media-amazon.com/images/I/51QCbXzEQlL._AC_UL320_.jpg"},
        {"name": "Anker Portable Charger, 313 Power Bank", "price": 21.99, "img": "https://m.media-amazon.com/images/I/61b1bA-Oq5L._AC_UL320_.jpg"},
        {"name": "SanDisk 1TB Extreme Portable SSD", "price": 99.99, "img": "https://m.media-amazon.com/images/I/71UqHsh6o3L._AC_UL320_.jpg"},
        {"name": "Bose SoundLink Micro Bluetooth Speaker", "price": 99.00, "img": "https://m.media-amazon.com/images/I/71x52aO4Y9L._AC_UL320_.jpg"},
        {"name": "Fitbit Charge 5 Advanced Fitness & Health Tracker", "price": 149.95, "img": "https://m.media-amazon.com/images/I/61-9Gvw-0VL._AC_UL320_.jpg"},
        {"name": "Razer DeathAdder V2 Gaming Mouse", "price": 39.99, "img": "https://m.media-amazon.com/images/I/6182gC4L2GL._AC_UL320_.jpg"},
        {"name": "Corsair Vengeance LPX 16GB (2x8GB) DDR4 DRAM", "price": 54.99, "img": "https://m.media-amazon.com/images/I/51kHiPeTSmL._AC_UL320_.jpg"}
    ]

    import tempfile
    import urllib.request
    from django.core.files import File

    for p in products:
        prod = Product.objects.create(name=p["name"], price=p["price"], description="Amazing product!")
        try:
            result = urllib.request.urlretrieve(p["img"])
            prod.image.save(
                os.path.basename(p["img"].split("?")[0]),
                File(open(result[0], 'rb'))
            )
        except Exception as e:
            print(f"Failed to download image for {p['name']}: {e}")
            pass
        prod.save()
    
    print("Database populated with 20 products and images.")

if __name__ == '__main__':
    populate()
