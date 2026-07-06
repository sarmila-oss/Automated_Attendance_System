# 🎓 Student Attendance Management System

A modern web-based **Student Attendance Management System** developed using **Python Flask** and **MySQL**. This application helps educational institutions manage students, faculty, and attendance records efficiently through a simple and user-friendly interface.

---

## 📌 Features

- 🔐 Secure Admin Login
- 👨‍🎓 Student Management (Add, Edit, Delete, View)
- 👨‍🏫 Faculty Management (Add, Edit, Delete, View)
- 📝 Attendance Management
- 📊 Attendance Report
- 📅 Date-wise Attendance Filter
- 🔍 Student Search
- 📥 Export Attendance Report to Excel
- 📄 Export Attendance Report to PDF
- 📈 Dashboard Statistics
  - Total Students
  - Today's Present Count
  - Today's Absent Count

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Backend
- Python
- Flask

### Database
- MySQL

---

## 📁 Project Structure

```
Automated_Attendance_System/
│
├── app.py
├── config.py
├── requirements.txt
├── attendance_system.sql
├── README.md
├── .gitignore
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── students.html
│   ├── add_student.html
│   ├── edit_student.html
│   ├── attendance.html
│   ├── attendance_report.html
│   ├── faculty.html
│   ├── add_faculty.html
│   └── edit_faculty.html
│
└── static/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Automated_Attendance_System.git
```

### 2. Open the project folder

```bash
cd Automated_Attendance_System
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Create a MySQL database named:

```
attendance_system
```

Import:

```
attendance_system.sql
```

Update your MySQL credentials inside:

```
config.py
```

Example:

```python
host="localhost"
user="root"
password="YOUR_PASSWORD"
database="attendance_system"
```

### 5. Run the application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 👤 Default Admin Login

| Username | Password |
|----------|----------|
| admin | 1234 |

---

## 📷 Screenshots

### Login Page

(Add Screenshot Here)

### Dashboard

(Add Screenshot Here)

### Student Management

(Add Screenshot Here)

### Attendance

(Add Screenshot Here)

### Attendance Report

(Add Screenshot Here)

### Faculty Management

(Add Screenshot Here)

---

## 🚀 Future Enhancements

- Face Recognition Attendance
- QR Code Attendance
- Email Notifications
- Student Login
- Faculty Login
- Mobile Responsive Design
- Cloud Database Integration

---

## 👩‍💻 Developed By

**Sarmila V**

Final Year Student

Department of Information Technology

---

## 📄 License

This project is developed for educational purposes.
