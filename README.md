# 🎓 Django Course API

A simple Django REST Framework-based Course Enrollment API with token-based authentication.

---

## 🚀 Features

- 🧑‍🏫 Manage Courses and Enrollments using ViewSets and Routers
- 🔐 Token-based Authentication using DRF's built-in `obtain_auth_token`
- 📝 User Registration Endpoint

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

---

## 📂 API Endpoints

| Method | Endpoint        | Description                     |
|--------|------------------|---------------------------------|
| GET    | `/course/`       | List all courses                |
| POST   | `/course/`       | Create a new course             |
| GET    | `/enroll/`       | List all enrollments            |
| POST   | `/enroll/`       | Enroll a student in a course    |
| POST   | `/register/`     | Register a new user             |
| POST   | `/token/`        | Obtain auth token (login)       |

---

## 🧑‍💻 Installation

```bash
git clone https://github.com/YourUsername/course-api.git
cd course-api
python -m venv venv
source venv/bin/activate  # Use `venv\Scripts\activate` on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
