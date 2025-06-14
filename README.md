# 🩺 Django Multiuser Dashboard (Doctor & Patient)

A Django web application with custom signup/login functionality for two user types — **Doctors** and **Patients**. Upon login, users are redirected to their respective styled dashboards. Features include a two-column signup form, profile picture upload, and authentication-based routing.

---

## 🚀 Features

- 👤 Custom signup with:
  - First Name, Last Name
  - Profile Picture upload
  - Username, Email, Password, Address
  - Two-column responsive form
- 🔐 Login system with redirection:
  - Doctors → Doctor Dashboard
  - Patients → Patient Dashboard
- 🎨 Bootstrap-based styling
- 🔄 Logout functionality
- 🧾 Success messages on signup and logout

---

## 🛠️ Tech Stack

- Python 3.12+
- Django 5.2
- SQLite (default)
- HTML + Bootstrap 5 (for styling)

---

## 🏁 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Sumathisree-A/Multiuser_Dashboard/
cd Multiuser_Dashboard
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv # Windows
venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash 
pip install -r requirements.txt
```
### 4️⃣ Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the development server
```bash
python manage.py runserver
```
