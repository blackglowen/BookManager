# Book Manager

Book Manager is a book catalog or if you want a simple library management system based on Django Python web application framework.

![Book Manager Admin Site](https://raw.githubusercontent.com/blackglowen/BookManager/main/screenshots/bookm-admin.png)

![Book Manager Admin Site](https://raw.githubusercontent.com/blackglowen/BookManager/main/screenshots/bookm01.png)

## Running database migrations

    python manage.py migrate
    
## Seeding the database with dummy data

    python manage.py seed -u 10 --genres --authors

## Creating an admin user

    python manage.py createsuperuser
    

## Running the application

    python manage.py runserver
