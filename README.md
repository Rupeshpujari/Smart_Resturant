# 🍽️ Smart Restaurant Ordering System

A modern web-based restaurant ordering system built with Streamlit that allows customers to place orders for both dine-in and takeaway services.

## ✨ Features

- **Service Selection**: Choose between Takeaway or Dine-in options
- **Smart Table Management**: Automatic table assignment for dine-in customers (Tables 1-15)
- **Interactive Menu**: Browse through categorized menu with multiple levels of selection
- **Real-time Order Tracking**: Add items to cart and see live bill calculation
- **QR Code Generation**: Generate QR codes for bill payment and order tracking
- **Session Management**: Maintains order state throughout the session
## 📋 Menu Categories

- **Biryani & Rice Dishes** (Veg & Non-Veg)
- **Mandhi** (Arabic rice dishes)
- **Indian Breads** (Naan, Roti, Paratha)
- **Starters** (Veg & Non-Veg appetizers)
- **Curries** (Traditional Indian curries)
- **Chinese Dishes** (Indo-Chinese fusion)
- **Snacks/Shawarma & Sides**
- **Desserts & Beverages**
- **Water Bottles** (Hot/Cold options)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/smart-restaurant-app.git
   cd smart-restaurant-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run first.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501`

## 📁 Project Structure

```
Smart-Restaurant-app/
├─ app/                   # app source (me.py or streamlit files)
│  └─ me.py
├─ assets/                # screenshots, GIFs, logos
│  └─ screenshot.png
├─ tests/                 # unit tests
├─ docs/                  # optional docs or design notes
├─ .github/
│  ├─ workflows/ci.yml
│  └─ PULL_REQUEST_TEMPLATE.md
├─ requirements.txt
├─ dev-requirements.txt   # flake8, pytest etc.
├─ .gitignore
├─ README.md
├─ LICENSE
└─ CONTRIBUTING.md

```

## 🔧 Technologies Used

- **Frontend**: Streamlit
- **Backend**: Python
- **QR Code Generation**: qrcode library
- **Image Processing**: Pillow (PIL)
- **Data Storage**: JSON

## 📱 How to Use

1. **Select Service Type**: Choose between "Takeaway" or "Dine-in"
2. **Table Assignment**: For dine-in, you'll automatically get a table number
3. **Browse Menu**: Navigate through categories and select items
4. **Add to Cart**: Specify quantity and add items to your order
5. **Checkout**: Review your order and generate QR code for payment

## 🎯 Key Features Explained

### Table Management
- Tracks allocated tables (1-15) across sessions
- Prevents double-booking of tables
- Displays table number throughout the ordering process

### Menu Navigation
- 4-level hierarchical menu structure
- Dynamic dropdown population based on selections
- Real-time price calculation

### Order Management
- Session-based cart management
- Live total calculation
- Order history display

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🍴 Future Enhancements

### 💳 Payment & Billing
- [ ] **Payment Gateway Integration**: Integrate with Razorpay, Stripe, or PayPal for secure online payments
- [ ] **Multiple Payment Methods**: Support UPI, credit/debit cards, digital wallets, and cash on delivery
- [ ] **Split Bill Feature**: Allow customers to split bills among multiple people
- [ ] **Discount & Coupon System**: Apply promotional codes and loyalty discounts
- [ ] **Tax Calculation**: Automatic GST/tax calculation based on location
- [ ] **Digital Receipt**: Email/SMS receipt with detailed breakdown

### 📊 Order Management & Tracking
- [ ] **Real-time Order Status**: Live tracking from order confirmation to delivery/ready
- [ ] **Kitchen Display System**: Digital screen for kitchen staff to manage orders
- [ ] **Estimated Wait Time**: Dynamic calculation based on kitchen load and order complexity
- [ ] **Order History**: Customer profile with past orders and favorites
- [ ] **Reorder Feature**: Quick reorder from previous orders with one click
- [ ] **Order Modifications**: Allow changes to orders within a specific time window

### 👨‍💼 Admin Dashboard & Management
- [ ] **Restaurant Admin Panel**: Complete dashboard for restaurant owners/managers
- [ ] **Menu Management**: Add/edit/remove items, update prices, and manage availability
- [ ] **Inventory Management**: Track ingredient stock and auto-disable unavailable items
- [ ] **Sales Analytics**: Daily, weekly, monthly reports with charts and insights
- [ ] **Table Management**: Real-time table status, reservations, and capacity planning
- [ ] **Staff Management**: User roles, permissions, and activity tracking
- [ ] **Revenue Reports**: Detailed financial reports and profit analysis

### 👥 Customer Experience
- [ ] **Customer Registration**: User accounts with profiles and preferences
- [ ] **Loyalty Program**: Points system, rewards, and membership tiers
- [ ] **Favorites List**: Save frequently ordered items for quick access
- [ ] **Dietary Preferences**: Filter menu by vegan, vegetarian, gluten-free, etc.
- [ ] **Allergy Alerts**: Warning system for common allergens
- [ ] **Rating & Review System**: Customer feedback on dishes and overall experience
- [ ] **Social Sharing**: Share favorite dishes on social media platforms

### 📱 Mobile & Accessibility
- [ ] **Mobile App**: Native iOS and Android applications
- [ ] **Progressive Web App (PWA)**: Offline capability and app-like experience
- [ ] **Voice Ordering**: Integration with voice assistants for hands-free ordering
- [ ] **Accessibility Features**: Screen reader support, high contrast mode, and keyboard navigation
- [ ] **Multi-language Support**: Support for regional languages and internationalization
- [ ] **Dark Mode**: Toggle between light and dark themes

### 🔔 Communication & Notifications
- [ ] **SMS Notifications**: Order confirmation, status updates, and promotional messages
- [ ] **Email Integration**: Digital receipts, marketing campaigns, and newsletters
- [ ] **Push Notifications**: Real-time updates through web/mobile app notifications
- [ ] **WhatsApp Integration**: Order updates and customer support through WhatsApp
- [ ] **Call Integration**: Click-to-call feature for customer support

### 🗄️ Data & Analytics
- [ ] **Database Migration**: Move from JSON to PostgreSQL/MySQL for better performance
- [ ] **Data Analytics**: Customer behavior analysis and business intelligence
- [ ] **A/B Testing**: Test different UI/UX elements to optimize conversion
- [ ] **Performance Monitoring**: Real-time app performance and error tracking
- [ ] **Backup & Recovery**: Automated data backup and disaster recovery systems
- [ ] **GDPR Compliance**: Data privacy and user consent management

### 🔗 Third-party Integrations
- [ ] **Delivery Platforms**: Integration with Swiggy, Zomato, Uber Eats APIs
- [ ] **POS Systems**: Connect with existing point-of-sale hardware
- [ ] **Accounting Software**: Integration with QuickBooks, Tally for financial management
- [ ] **Social Media**: Facebook, Instagram integration for marketing and reviews
- [ ] **Google Services**: Maps integration, Google Reviews, and Google My Business
- [ ] **Printer Integration**: Direct printing to kitchen and billing printers

### 🏪 Multi-location & Franchise
- [ ] **Multi-restaurant Support**: Manage multiple restaurant locations from single dashboard
- [ ] **Franchise Management**: White-label solution for restaurant chains
- [ ] **Location-based Menus**: Different menus and pricing for different locations
- [ ] **Centralized Reporting**: Consolidated reports across all locations
- [ ] **Brand Customization**: Custom themes, logos, and branding for each location

### 🔒 Security & Compliance
- [ ] **User Authentication**: Secure login with OTP, social login, and 2FA
- [ ] **Data Encryption**: End-to-end encryption for sensitive customer data
- [ ] **PCI DSS Compliance**: Secure payment processing standards
- [ ] **Role-based Access Control**: Different permission levels for staff and admins
- [ ] **Audit Logs**: Track all system changes and user activities
- [ ] **Security Scanning**: Regular vulnerability assessments and penetration testing

### 📈 Advanced Features
- [ ] **AI Recommendations**: Machine learning-based food recommendations
- [ ] **Predictive Analytics**: Forecast demand and optimize inventory
- [ ] **Chatbot Support**: AI-powered customer service and order assistance
- [ ] **Table Reservation System**: Online booking with calendar integration
- [ ] **Event Management**: Special event bookings and catering orders
- [ ] **Subscription Model**: Monthly meal plans and recurring orders

## 📞 Contact

👨‍💻 **Developer:** Rupesh Pujari
📧 **Email:** rupeshpujari5542@gmail.com  
🔗 **GitHub:** (https://github.com/Rupeshpujari)  
---

⭐ Don't forget to star this repository if you found it helpful!



