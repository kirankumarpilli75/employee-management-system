# Employee Management System (Django)

A full-stack Employee Management System built with Django, SQLite, and Bootstrap 5.
Includes authentication, a dashboard, and complete CRUD + search for employee records.

## Features

- **Authentication:** Login / Logout, protected dashboard and employee pages (`@login_required`)
- **Employee CRUD:** Add, list, view, update, delete employees
- **Search:** Search employees by name or department
- **Dashboard:** Total employees, department breakdown, recently added employees (Bootstrap cards)
- **Profile Photos:** Optional image upload per employee
- **Django Admin:** Customized list display, filters, search, fieldsets
- **Responsive UI:** Bootstrap 5, mobile-friendly navbar and tables
- **Messages Framework:** Success/error/info alerts on every action
- **Form Validation:** Server-side validation on all employee fields

## Tech Stack

| Layer      | Technology          |
|------------|----------------------|
| Backend    | Python 3, Django 4.2 |
| Database   | SQLite               |
| Frontend   | HTML5, CSS3, Bootstrap 5 |
| Images     | Pillow               |

## Project Structure

```
employee_management/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── db.sqlite3                  (created after migrate)
├── employee_management/        # Project config
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── accounts/                   # Authentication app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
├── employees/                  # Employee CRUD app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│       └── 0001_initial.py
├── templates/
│   ├── base.html
│   ├── includes/
│   │   ├── navbar.html
│   │   └── footer.html
│   ├── accounts/
│   │   └── login.html
│   ├── dashboard/
│   │   └── dashboard.html
│   └── employees/
│       ├── employee_list.html
│       ├── employee_form.html
│       ├── employee_detail.html
│       └── employee_confirm_delete.html
├── static/
│   ├── css/style.css
│   ├── js/script.js
│   └── img/
└── media/
    └── profile_photos/
```

## Setup Instructions

1. **Clone / extract the project**, then move into the folder:
   ```bash
   cd employee_management
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for Django admin and to log in to the app):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. Visit:
   - App: http://127.0.0.1:8000/accounts/login/
   - Admin: http://127.0.0.1:8000/admin/

## Notes

- Only logged-in users can access the dashboard and employee pages; anonymous users are
  redirected to the login page.
- Employee ID shown in the UI (e.g. `EMP-0001`) is derived from the database primary key.
- Profile photos are stored under `media/profile_photos/` and served via Django in
  development (`DEBUG=True`). Use a proper file/object storage service in production.
- Before deploying: set `DEBUG = False`, set a real `SECRET_KEY` via an environment
  variable, and configure `ALLOWED_HOSTS`.
