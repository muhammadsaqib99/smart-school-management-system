# 🎓 Smart School Management System

A modern and user-friendly School Management System built with Django and Tailwind CSS. This project is designed to efficiently manage students, teachers, classes, and user roles with a clean and responsive admin dashboard.

---

## 🚀 Features

- 🔐 User Authentication (Login / Logout)
- 👥 Role-Based Access Control (Admin, Teacher, Student)
- 🎓 Student Management (Add, Edit, Delete, List)
- 👨‍🏫 Teacher Management System
- 🏫 Class & Section Management
- 📂 Bulk Student Upload via CSV
- 📊 Dashboard with Analytics (Chart.js)
- 👤 Profile Page (Role-based information)
- 🎨 Modern UI using Tailwind CSS
- 📱 Fully Responsive Design
- 📌 Sidebar Admin Panel Layout

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Tailwind CSS
- **Database:** SQLite
- **Charts:** Chart.js

---

## ⚙️ Installation Guide

```bash
git clone https://github.com/muhammadsaqib99/smart-school-management-system.git
cd smart_school

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
