# E-Commerce Store (Amazon Clone)

A fully functional, responsive e-commerce web application built with Django and styled beautifully using Bootstrap. 

This project simulates a modern e-commerce storefront (inspired by Amazon), complete with a dynamic product gallery, user authentication, and a working shopping cart system.

## 🚀 Features

- **Product Gallery**: Browse a grid of authentic tech products (Laptops, Cameras, Smartwatches, etc.) featuring accurate high-quality images.
- **Dynamic Hero Banner**: An auto-sliding, fading carousel advertising current sales (e.g., "Great Indian Festival Sale").
- **Shopping Cart**: Add items, adjust quantities, and remove items with seamless asynchronous JavaScript calls (no page reloads needed!).
- **User Authentication**: Secure login and registration functionality. Only logged-in users can add items to their cart.
- **Checkout Simulation**: A shipping form to process mock orders.
- **Vercel Ready**: Pre-configured with `vercel.json` and `requirements.txt` for immediate deployment to Vercel Serverless Functions.

## 🛠️ Tech Stack

- **Backend**: Python, Django (3.2)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite (Configured to run on Vercel's ephemeral `/tmp` storage)

## 💻 Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Utkantha/codealpha_ecommerce.git
   cd codealpha_ecommerce
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Populate the database with dummy products:**
   ```bash
   python populate.py
   ```

4. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   *Open `http://127.0.0.1:8000/` in your browser.*

## 🌐 Vercel Deployment

This project is configured out-of-the-box to deploy on Vercel. Because Vercel serverless functions use a read-only filesystem, the `settings.py` file contains a custom script that automatically copies the local `db.sqlite3` database to Vercel's writable `/tmp` directory when the server spins up. This allows the initial product gallery to be served flawlessly!
