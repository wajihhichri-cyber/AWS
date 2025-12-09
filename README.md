# CyberTek E-Commerce Application

A modern, professional Flask e-commerce application with user authentication, admin dashboard, and SQLite database.

## ✨ Features

- 🔐 **User Authentication**: Sign up, Sign in, Sign out with secure password hashing
- 👤 **User Profiles**: View account info, order history, and change password
- 🛒 **Shopping Cart**: Add products, update quantities, remove items
- 📦 **Order Management**: Place orders, view order history with details
- 👨‍💼 **Admin Dashboard**: Manage categories, view orders and users
- 🎨 **Modern UI**: Sleek design with animations and responsive layout
- 📱 **Fully Responsive**: Works on desktop, tablet, and mobile
- 💾 **SQLite Database**: Persistent storage for users, products, and orders

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip

### Installation

1. **Clone or navigate to the project**:
```bash
cd cybertek
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run the application**:
```bash
python app.py
```

4. **Open your browser**:
```
http://localhost:5000
```

## 📝 Default Credentials

The application automatically creates an admin account on first run:
- **Username**: `admin`
- **Password**: `admin123`

**⚠️ Important**: Change the admin password immediately in production!

## 📋 User Guide

### For Customers

1. **Sign Up**: Create a new account
   - Username, Email, Password
   - Confirm password must match

2. **Browse Products**: View all products on the home page

3. **Add to Cart**: Click "Add to Cart" on any product

4. **Checkout**: 
   - Review cart items
   - Update quantities or remove items
   - Proceed to checkout (requires login)
   - Complete order

5. **My Profile**:
   - View account information
   - View complete order history with details
   - Change password securely

6. **Sign Out**: Safely log out of your account

### For Admins

1. **Access Admin Dashboard**: Click "Admin" in navigation (only visible to admin users)

2. **Manage Categories**:
   - View all categories
   - Add new categories
   - Delete existing categories

3. **View Statistics**:
   - Total products count
   - Total categories count
   - Total orders count
   - Total users count

4. **Monitor Orders**:
   - View all orders
   - See order details and status
   - Track customer purchases

5. **Manage Users**:
   - View all registered users
   - See user registration date
   - View user order counts
   - Identify admin users

## 🗄️ Database Models

### User
- id, username (unique), email (unique), password (hashed)
- is_admin, created_at
- Relationship: orders

### Category
- id, name (unique)
- Relationship: products

### Product
- id, name, price, description, image, specs, stock, category_id, created_at
- Relationship: order_items

### Order
- id, user_id, total, status, created_at
- Relationship: items (OrderItem), user

### OrderItem
- id, order_id, product_id, quantity, price
- Relationship: order, product

## 🎯 Key Routes

### Authentication
- `GET/POST /signup` - User registration
- `GET/POST /login` - User login
- `GET /logout` - User logout

### Shopping
- `GET /` - Home page with products
- `GET /product/<id>` - Product details
- `POST /add-to-cart/<id>` - Add to cart (AJAX)
- `GET /cart` - View shopping cart
- `POST /update-cart/<id>` - Update cart item quantity
- `GET /remove-from-cart/<id>` - Remove from cart
- `GET/POST /checkout` - Checkout page
- `POST /process-order` - Process order and save to database

### User Profile
- `GET /profile` - User profile with orders
- `POST /change-password` - Change password

### Admin
- `GET /admin/dashboard` - Admin dashboard
- `POST /admin/add-category` - Add category
- `POST /admin/delete-category/<id>` - Delete category

### Error Handling
- `GET /404` - Page not found
- `GET /500` - Server error

## 📱 Responsive Design

The application is fully responsive and works on:
- ✅ Desktop (1200px+)
- ✅ Tablet (768px - 1199px)
- ✅ Mobile (< 768px)

## 🎨 Design Features

- **Color Scheme**: Dark theme with cyan and purple accents
- **Animations**: Smooth transitions and fade-in effects
- **Icons**: Font Awesome 6.4.0 for all icons
- **Typography**: Inter font family with multiple weights
- **Responsive Grid**: Auto-adjusting layouts

## 🔒 Security Features

- ✅ Password hashing with Werkzeug
- ✅ Session-based authentication
- ✅ Login required for checkout
- ✅ Admin role protection
- ✅ CSRF protection ready (Flask-Login)
- ✅ Input validation on all forms

## 📊 Project Structure

```
cybertek/
├── app.py                          # Main application with all routes
├── requirements.txt                # Python dependencies
├── cybertek.db                     # SQLite database (created on first run)
├── static/
│   ├── style.css                  # All styling with auth/profile/admin styles
│   └── script.js                  # Frontend functionality
└── templates/
    ├── base.html                  # Base template with navbar
    ├── home.html                  # Home page
    ├── product_detail.html        # Product details
    ├── cart.html                  # Shopping cart
    ├── checkout.html              # Checkout page
    ├── order_success.html         # Order confirmation
    ├── signup.html                # Sign up page
    ├── login.html                 # Login page
    ├── profile.html               # User profile with orders
    ├── admin_dashboard.html       # Admin dashboard
    ├── 404.html                   # 404 error page
    └── 500.html                   # 500 error page
```

## 🚀 Production Deployment

Before deploying to production:

1. **Change Secret Key**: Update `app.secret_key` in `app.py`
2. **Disable Debug Mode**: Set `debug=False` (already done)
3. **Use Environment Variables**: Store configuration in environment
4. **Database**: Consider using PostgreSQL instead of SQLite
5. **HTTPS**: Enable SSL/TLS certificate
6. **Session Management**: Use server-side session storage
7. **Admin Password**: Change default admin password immediately

## 📝 Example AWS Deployment

```bash
# Install EB CLI
pip install awsebcli --upgrade --user

# Initialize EB application
eb init -p python-3.11 cybertek

# Create environment
eb create cybertek-env

# Deploy
eb deploy
```

## 🛠️ Technologies Used

- **Backend**: Flask 3.0.0
- **Database**: SQLAlchemy ORM with SQLite
- **Authentication**: Flask-Login with Werkzeug
- **Frontend**: HTML5, CSS3, JavaScript
- **Icons**: Font Awesome 6.4.0
- **Deployment Ready**: AWS compatible

## 📄 License

This project is open source and available under the MIT License.

## 📞 Support

For issues or questions, please check the code comments in `app.py` for detailed implementation notes.
├── app.py              # Main Flask application
├── templates/          # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── product_detail.html
│   ├── cart.html
│   ├── checkout.html
│   └── order_success.html
├── static/            # CSS and JS files
│   ├── style.css
│   └── script.js
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Development

- The application uses Flask sessions for cart management
- Product data is currently stored in-memory (ready for database integration)
- Images are loaded from Unsplash CDN (ready for S3 migration)

## Next Steps for Production

1. Set up AWS account and configure credentials
2. Create S3 bucket for product images
3. Set up RDS/DynamoDB for product data
4. Configure AWS Secrets Manager
5. Deploy to Elastic Beanstalk
6. Set up CloudFront distribution
7. Configure custom domain and SSL

Enjoy building with CyberTek! 🚀
