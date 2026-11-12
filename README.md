# Django Todo List (CRUD)

A simple Todo List app built with Django and PostgreSQL. 

## Features
- Create, Read, Update, Delete todos
- Mark a todo complete/incomplete
- Django admin panel for managing todos

## Project structure
```
django_todo_list/
├── manage.py
├── requirements.txt
├── .env.example
├── todo_project/       # project settings & root urls
│   ├── settings.py
│   └── urls.py
└── todos/               # the app containing all CRUD logic
    ├── models.py         # Todo model
    ├── forms.py           # TodoForm (ModelForm)
    ├── views.py           # list/create/update/delete/toggle views
    ├── urls.py            # app-level routes
    ├── admin.py            # admin registration
    └── templates/todos/    # HTML templates
```

## Setup

1. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv venv
   linux: source venv/bin/activate   
   Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Create a Postgres database**
   ```sql
   CREATE DATABASE todo_db;
   ```

3. **Set your database credentials**
   Copy `.env.example` to `.env` and fill in your values,
   ( use a tool like `django-environ`/`python-dotenv` if you prefer):
   
   
4. **Run migrations** (creates the `todos_todo` table)
   ```bash
   python manage.py makemigrations
   python manage.py mairate
   ```

5. **(Optional) Create an admin user**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```
   Visit 
   `http://127.0.0.1:8000/` for the todo list, or
   `http://127.0.0.1:8000/admin/` for the admin panel if super is created.

## Author
**Joshua Oguejiofor**