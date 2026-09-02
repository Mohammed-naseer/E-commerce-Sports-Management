<div align="center">

<img src="sports/static/css/img/barlogo.png" alt="dSports Logo" width="100" />

# 🏆 dSports — E-Commerce Sports Management

**A premium full-stack sports e-commerce web application built with Django**

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.1-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://mysql.com)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br/>

> *Your premier destination for official football club jerseys, high-performance running shoes, and elite athletic training wear.*

[🚀 Live Demo](#-getting-started) · [📸 Screenshots](#-screenshots) · [✨ Features](#-features) · [🛠️ Installation](#-installation)

</div>

---

## 📸 Screenshots

<div align="center">

| Homepage | Product Catalog | Shopping Cart |
|----------|----------------|---------------|
| Hero video + featured products | Dynamic grid with Add to Cart | AJAX-powered cart with live totals |

| Checkout | Order Receipt | Admin Dashboard |
|----------|--------------|-----------------|
| Full delivery form + order summary | Itemized invoice + shipping details | Manage all orders & products |

</div>

---

## ✨ Features

### 🛍️ Shopping Experience
- **Dynamic Product Catalog** — 60+ real products across 8 categories with beautiful card grid
- **Size & Quantity Selector** — Choose your perfect fit before adding to cart
- **AJAX Shopping Cart** — Instant add/remove/update without page reloads
- **Live Cart Badge** — Real-time cart count updates in the navbar
- **Image Zoom Modal** — Click any product image for an enlarged high-res view
- **Search & Sort** — Find products by keyword; sort by price or name

### 📦 Order Management
- **Full Checkout Flow** — Delivery form with address + payment method selection
- **Auto Order Numbers** — Every order gets a unique ID (e.g. `DSP-4A3F9B12`)
- **Order Confirmation Receipt** — Itemized invoice with shipping address
- **Database Persistence** — All orders & items saved to MySQL

### 🎨 Premium UI/UX Design
- **Glassmorphism Sticky Navbar** with mega dropdown navigation
- **Animated Toast Notifications** — Success/error messages auto-dismiss in 4s
- **Dark Sports Theme** — Deep navy + vibrant orange palette
- **Hover Micro-animations** — Cards lift, images zoom, badges pulse
- **Fully Responsive** — Works beautifully on desktop, tablet and mobile

### 🔧 Admin & Backend
- **Django Admin Dashboard** — Full CRUD for all 6 models
- **Contact Form** — Customer messages stored and reviewable in admin
- **Management Command** — `python manage.py seed_data` populates the entire catalog
- **Context Processor** — Cart count available globally on every page

---

## 🏷️ Product Categories

| Department | Categories | Products |
|------------|-----------|---------|
| ⚽ **Football** | Jerseys, Boots, Accessories | 30 products |
| 🏃 **Running Shoes** | Men's, Women's | 12 products |
| 💪 **Training** | Men's, Women's, Kids | 18 products |

### 🎽 Featured Club Jerseys
`Real Madrid` · `Manchester United` · `Liverpool` · `Arsenal` · `PSG` · `Juventus` · `Manchester City` · `Chelsea` · `Tottenham` · `Celtic` · `Atletico Madrid` · `FC Barcelona`

---

## 🛠️ Installation

### Prerequisites
- Python 3.10+
- MySQL 8.0+
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/Mohammed-naseer/E-commerce-Sports-Management.git
cd E-commerce-Sports-Management
```

### 2. Create & Activate Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django mysqlclient
```

### 4. Configure the Database

Create a MySQL database named `Hackaton`:

```sql
CREATE DATABASE Hackaton CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Update `sports/sports/settings.py` with your MySQL credentials if different:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Hackaton',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### 5. Run Migrations

```bash
cd sports
python manage.py migrate
```

### 6. Seed the Product Catalog

```bash
python manage.py seed_data
```

> This automatically creates **8 categories** and **60 products** with all images, prices and descriptions.

### 7. Create Admin Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Start the Development Server

```bash
python manage.py runserver
```

Open your browser and visit **http://127.0.0.1:8000** 🎉

---

## 🗂️ Project Structure

```
E-commerce-Sports-Management/
│
├── sports/                         # Django project root
│   ├── details/                    # Main application
│   │   ├── migrations/             # Database migrations
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── seed_data.py    # Catalog seeding command
│   │   ├── models.py               # Category, Product, Order, OrderItem, etc.
│   │   ├── views.py                # All views (catalog, cart, checkout, contact)
│   │   ├── cart.py                 # Session-based cart engine
│   │   ├── context_processors.py   # Global cart & categories context
│   │   ├── forms.py                # DeliveryForm, ContactForm
│   │   ├── admin.py                # Customized admin dashboard
│   │   └── urls.py                 # (via sports/urls.py)
│   │
│   ├── sports/                     # Django settings
│   │   ├── settings.py
│   │   └── urls.py                 # Main URL configuration
│   │
│   ├── templates/
│   │   └── base/
│   │       ├── base.html           # Master template (navbar + footer)
│   │       ├── index.html          # Homepage
│   │       ├── product_list.html   # Dynamic catalog template
│   │       ├── cart.html           # Shopping cart
│   │       ├── deliveryForm.html   # Checkout
│   │       ├── order_success.html  # Order receipt
│   │       └── contact.html        # Contact us
│   │
│   └── static/
│       ├── css/
│       │   ├── style.css           # Full design system
│       │   ├── dropdown.css        # Mega navigation dropdown
│       │   ├── modal.css           # Image zoom modal
│       │   └── img/                # 100+ product & background images
│       └── script.js               # AJAX cart, toast, modal handlers
│
├── .gitignore
└── README.md
```

---

## 🔗 URL Reference

| Route | View | Description |
|-------|------|-------------|
| `/` | `index` | Homepage with hero video & featured products |
| `/shop/` | `product_list` | Full catalog with search & sort |
| `/jersey/` | `jersey` | Football club jerseys |
| `/shoes/` | `shoes` | Football boots & studs |
| `/accessories/` | `accessories` | Balls, gloves, bags & gear |
| `/maleRunningShoes/` | `maleRunningShoes` | Men's running footwear |
| `/femaleRunningShoes/` | `femaleRunningShoes` | Women's running footwear |
| `/trainingmen/` | `trainingmen` | Men's gym & activewear |
| `/trainingwomen/` | `trainingwomen` | Women's activewear |
| `/trainingKids/` | `trainingKids` | Kids' athletic wear |
| `/cart/` | `cart_view` | Shopping cart |
| `/cart/add/<id>/` | `cart_add` | Add item to cart |
| `/cart/remove/<id>/` | `cart_remove` | Remove item from cart |
| `/cart/update/` | `cart_update` | AJAX quantity update |
| `/delivery/` | `deliveryForm` | Checkout & shipping form |
| `/order-success/<no>/` | `order_success` | Order receipt page |
| `/contact/` | `contact` | Contact us form |
| `/admin/` | Django Admin | Admin dashboard |

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.12, Django 5.1 |
| **Database** | MySQL 8.0 |
| **Frontend** | HTML5, Vanilla CSS3, JavaScript (ES6+) |
| **AJAX** | jQuery 3.6 + Fetch API |
| **Icons** | Font Awesome 6.4 |
| **Fonts** | Google Fonts — Outfit & Plus Jakarta Sans |
| **Version Control** | Git & GitHub |

---

## 👨‍💻 Author

<div align="center">

**Mohammed Naseer**  
*B.Tech Computer Science | Malla Reddy University, Hyderabad*

[![GitHub](https://img.shields.io/badge/GitHub-Mohammed--naseer-181717?style=for-the-badge&logo=github)](https://github.com/Mohammed-naseer)

📧 2411CS010387@mallareddyuniversity.ac.in  
📞 +91 7013722022

</div>

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it for educational purposes.

---

<div align="center">

**⭐ If you found this helpful, please star the repository!**

Made with ❤️ for the Malla Reddy University project submission

</div>
