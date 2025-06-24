# Telegram Bot Backend with Django, Celery & Redis

This project sets up a **Django-based backend** designed to manage **Telegram bots**, while handling background and asynchronous tasks like sending emails using **Celery** and **Redis**.

---

## 🚀 Project Features

- ✅ Django backend setup for bot automation
- ✅ JWT-based user authentication
- ✅ Background task execution using Celery
- ✅ Redis as the message broker
- ✅ Email service integration for notifications
- ✅ MySQL as the production database

---

## 📦 Tech Stack

- **Python 3**
- **Django**
- **Celery**
- **Redis**
- **MySQL**
- **JWT (via SimpleJWT)**
- **SMTP Email Integration**

---

## 🛠️ Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/sai-satish/telegram-bot-with-django
cd telegram-bot-with-django
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv telegram-bot-with-django
source telegram-bot-with-django/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a .env file in the project root with the following variables:

- SECRET_KEY=your-django-secret-key
- DB_NAME=your-database-name
- DB_USER=your-database-username
- DB_PASSWORD=your-database-password
- DB_HOST=localhost
- DB_PORT=3306
- BOT_TOKEN=your-telegram-bot-token
- EMAIL_HOST_USER=youremail@example.com
- EMAIL_HOST_PASSWORD=your-app-password

### 5. Getting Redis Server setup
```bash
sudo apt update
sudo apt install redis-server
sudo service redis-server start
```

### 6. Start Celery Worker
In the project root directory (where manage.py is present):
``` bash
celery -A telegram_bot worker --loglevel=info
```

### 7. 🌐 Run Django Server
```bash
cd telegram_bot
python manage.py runserver
```

Your application will be available at http://127.0.0.1:8000/
