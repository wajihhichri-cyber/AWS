# CyberTek E-Commerce Application

A modern, professional Flask e-commerce application with sleek animations and responsive design.

## Features

- 🎨 Modern UI with smooth animations
- 🛒 Shopping cart functionality
- 📱 Fully responsive design
- 🎯 Product catalog with filtering
- 💳 Checkout process
- 🔐 Session-based cart management

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

## AWS Deployment Notes

This application is prepared for AWS deployment with:
- Environment variable support for configuration
- Placeholder for AWS Secrets Manager integration
- Ready for S3 integration for product images
- Scalable session management

### AWS Integration (To be implemented):

1. **S3 for Images**: Replace static image URLs with S3 bucket URLs
2. **Secrets Manager**: Store sensitive configuration in AWS Secrets Manager
3. **RDS/DynamoDB**: Replace in-memory product data with database
4. **Elastic Beanstalk**: Deploy application to Elastic Beanstalk
5. **CloudFront**: Add CDN for static assets

## Project Structure

```
cybertek/
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
