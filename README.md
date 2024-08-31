# FameLink

FameLink is a Django-based web application that connects users with popular people around the world. The platform provides various features, including user authentication, article management, and dynamic contact and about us pages.

## Features

- **User Authentication**: Login, Logout, Registration, Password Reset
- **Article Management**: Add, Edit, Delete, View articles
- **Dynamic Pages**: About Us, Contact Us
- **Dockerized Setup**: Easy deployment using Docker

## Project Structure

```bash
├── DjangoAdvanced_Project/
│   ├── DjangoAdvanced_Project/    # Main project directory
│   │   ├── __init__.py            # Project initialization
│   │   ├── asgi.py                # ASGI configuration
│   │   ├── settings.py            # Project settings
│   │   ├── urls.py                # URL configuration
│   │   ├── wsgi.py                # WSGI configuration
│   ├── popularpeople/             # Main application directory
│   │   ├── migrations/            # Database migrations
│   │   ├── static/                # Static files (CSS, JS, Images)
│   │   │   ├── css/               # Stylesheets
│   │   │   └── images/            # Image files
│   │   ├── templates/             # HTML templates
│   │   │   ├── base.html          # Base template
│   │   │   ├── about.html         # About Us page template
│   │   │   ├── contact.html       # Contact Us page template
│   │   │   ├── index.html         # Homepage template
│   │   │   └── post.html          # Article template
│   │   ├── admin.py               # Admin configuration
│   │   ├── apps.py                # Application configuration
│   │   ├── forms.py               # Forms for handling user input
│   │   ├── models.py              # Database models
│   │   ├── urls.py                # URL routing
│   │   ├── views.py               # Application views (logic)
│   │   ├── tests.py               # Unit tests
│   │   ├── templatetags/          # Custom template tags
│   ├── users/                     # User management application
│   │   ├── templates/             # User-related templates
│   │   │   ├── login.html         # Login page template
│   │   │   ├── register.html      # Registration page template
│   │   │   ├── profile.html       # User profile page template
│   │   │   ├── password_reset.html # Password reset page template
│   │   ├── forms.py               # User forms
│   │   ├── views.py               # User views
│   │   ├── urls.py                # User URL configuration
│   ├── manage.py                  # Django management script
│   ├── Dockerfile                 # Docker configuration
│   ├── requirements.txt           # Python dependencies
│   ├── README.md                  # Project documentation
```

## Installation

### Prerequisites

- Python 3.12+
- Docker (if deploying with Docker)

### Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/famelink.git
    cd famelink
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Access the application:**
    - Open your web browser and go to `http://localhost:8000`.

### Docker Setup

1. **Build the Docker image:**
    ```bash
    docker build -t famelink-app .
    ```

2. **Run the Docker container:**
    ```bash
    docker run -d -p 8000:8000 famelink-app
    ```

3. **Access the application:**
    - Open your web browser and go to `http://localhost:8000`.

## Usage

- **Admin Panel:** Accessible at [http://localhost:8000/admin](http://localhost:8000/admin).
- **User Features:** Register, login, and manage your profile.

## Contributing

Feel free to fork the project, create a branch, and submit a pull request with any improvements or fixes. Contributions are welcome!

## Contact

For any inquiries or questions, feel free to contact us at [nazaruk7649@ukr.net](mailto:nazaruk7649@ukr.net).

---

Thank you for using FameLink! We hope you find it useful and enjoyable.
