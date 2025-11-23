from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = 'cybertek-secret-key-change-in-production'

# Demo Products Database
PRODUCTS = [
    {
        'id': 1,
        'name': 'CyberBook Pro X1',
        'category': 'Laptops',
        'price': 1299.99,
        'image': 'https://cybertek-products-images-2025.s3.us-east-1.amazonaws.com/products/1.jpeg',
        'description': 'Ultra-thin laptop with 16GB RAM, 512GB SSD, and stunning 4K display',
        'specs': ['Intel i7 Processor', '16GB RAM', '512GB SSD', '14-inch 4K Display'],
        'stock': 15
    },
    {
        'id': 2,
        'name': 'Quantum Wireless Headphones',
        'category': 'Audio',
        'price': 249.99,
        'image': 'https://cybertek-products-images-2025.s3.us-east-1.amazonaws.com/products/2.jpeg',
        'description': 'Premium noise-cancelling headphones with 40-hour battery life',
        'specs': ['Active Noise Cancellation', '40-Hour Battery', 'Bluetooth 5.3', 'Premium Sound'],
        'stock': 28
    },
    {
        'id': 3,
        'name': 'NeoWatch Ultra',
        'category': 'Wearables',
        'price': 399.99,
        'image': 'https://cybertek-products-images-2025.s3.us-east-1.amazonaws.com/products/3.jpeg',
        'description': 'Advanced smartwatch with health tracking and AMOLED display',
        'specs': ['AMOLED Display', 'Heart Rate Monitor', 'GPS Tracking', 'Water Resistant'],
        'stock': 22
    },
    {
        'id': 4,
        'name': 'TechPad Mini',
        'category': 'Tablets',
        'price': 599.99,
        'image': 'https://cybertek-products-images-2025.s3.us-east-1.amazonaws.com/products/4.jpeg',
        'description': 'Compact tablet perfect for work and entertainment on the go',
        'specs': ['10.5-inch Display', '128GB Storage', '12MP Camera', 'All-Day Battery'],
        'stock': 18
    },
    {
        'id': 5,
        'name': 'ProGaming Mouse RGB',
        'category': 'Gaming',
        'price': 79.99,
        'image': 'https://cybertek-products-images-2025.s3.us-east-1.amazonaws.com/products/5.jpeg',
        'description': 'High-precision gaming mouse with customizable RGB lighting',
        'specs': ['16000 DPI', 'RGB Lighting', 'Programmable Buttons', 'Ergonomic Design'],
        'stock': 45
    },
    {
        'id': 6,
        'name': 'UltraView 4K Monitor',
        'category': 'Displays',
        'price': 449.99,
        'image': 'https://cybertek-products-images-2025.s3.us-east-1.amazonaws.com/products/6.jpeg',
        'description': '27-inch 4K HDR monitor with stunning color accuracy',
        'specs': ['27-inch 4K', 'HDR Support', '144Hz Refresh', 'USB-C Connectivity'],
        'stock': 12
    },
    {
        'id': 7,
        'name': 'PowerBank Infinite',
        'category': 'Accessories',
        'price': 89.99,
        'image': 'https://cybertek-products-images-2025.s3.us-east-1.amazonaws.com/products/7.jpeg',
        'description': '30000mAh portable charger with fast charging technology',
        'specs': ['30000mAh Capacity', 'Fast Charging', 'Multiple Ports', 'LED Display'],
        'stock': 35
    },
    {
        'id': 8,
        'name': 'CyberCam 4K Pro',
        'category': 'Cameras',
        'price': 899.99,
        'image': 'https://cybertek-products-images-2025.s3.us-east-1.amazonaws.com/products/8.jpeg',
        'description': 'Professional 4K webcam for streaming and video calls',
        'specs': ['4K Resolution', 'Auto-Focus', 'Low-Light Performance', 'Wide Angle Lens'],
        'stock': 20
    }
]

@app.route('/')
def home():
    return render_template('home.html', products=PRODUCTS)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product:
        return redirect(url_for('home'))
    return render_template('product_detail.html', product=product)

@app.route('/add-to-cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if product:
        cart = session['cart']
        existing_item = next((item for item in cart if item['id'] == product_id), None)
        
        if existing_item:
            existing_item['quantity'] += 1
        else:
            cart.append({
                'id': product['id'],
                'name': product['name'],
                'price': product['price'],
                'image': product['image'],
                'quantity': 1
            })
        
        session['cart'] = cart
        session.modified = True
    
    return jsonify({'success': True, 'cart_count': len(session.get('cart', []))})

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/update-cart/<int:product_id>', methods=['POST'])
def update_cart(product_id):
    quantity = int(request.form.get('quantity', 1))
    cart = session.get('cart', [])
    
    for item in cart:
        if item['id'] == product_id:
            if quantity <= 0:
                cart.remove(item)
            else:
                item['quantity'] = quantity
            break
    
    session['cart'] = cart
    session.modified = True
    return redirect(url_for('cart'))

@app.route('/remove-from-cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    cart = [item for item in cart if item['id'] != product_id]
    session['cart'] = cart
    session.modified = True
    return redirect(url_for('cart'))

@app.route('/checkout')
def checkout():
    cart_items = session.get('cart', [])
    if not cart_items:
        return redirect(url_for('cart'))
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('checkout.html', cart_items=cart_items, total=total)

@app.route('/process-order', methods=['POST'])
def process_order():
    # Here you would integrate payment processing
    # For demo, we'll just clear the cart
    session['cart'] = []
    session.modified = True
    return render_template('order_success.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
