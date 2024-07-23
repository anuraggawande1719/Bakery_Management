# Bakery Management System

A web-based application for managing a bakery, built with Python and Django. This system allows you to manage products, customers, and orders efficiently.

## Features

- Add, view, update, and delete products
- Add, view, update, and delete customers
- Place, view, and manage orders
- Calculate total price for orders

## Prerequisites

- Python 3.x
- Django 3.x or higher

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/bakery_management.git
    cd bakery_management
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install django
    ```

4. **Apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser for the admin site:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Navigate to the application:**

    Open your web browser and go to `http://127.0.0.1:8000/` to view the application.

## Usage

### Admin Interface

1. Go to `http://127.0.0.1:8000/admin/`
2. Log in using the superuser credentials you created.
3. Manage products, customers, and orders through the Django admin interface.

### Application Interface

1. **Home Page:** `http://127.0.0.1:8000/`
   - Provides links to manage products, customers, and orders.

2. **Products:**
   - View all products: `http://127.0.0.1:8000/bakery/products/`
   - Add a new product: `http://127.0.0.1:8000/bakery/products/add/`

3. **Customers:**
   - View all customers: `http://127.0.0.1:8000/bakery/customers/`
   - Add a new customer: `http://127.0.0.1:8000/bakery/customers/add/`

4. **Orders:**
   - View all orders: `http://127.0.0.1:8000/bakery/orders/`
   - Place a new order: `http://127.0.0.1:8000/bakery/orders/add/`

## Project Structure


## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License 
