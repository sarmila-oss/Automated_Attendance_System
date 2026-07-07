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

<img width="900" height="541" alt="Screenshot 2026-07-06 162348" src="https://github.com/user-attachments/assets/fb0e82b2-ee88-4d7a-8df7-6b381b2ed770" />



### Dashboard

 <img width="1876" height="882" alt="Screenshot 2026-07-06 164054" src="https://github.com/user-attachments/assets/800c98d8-9467-4c8f-8290-bcd49d05494f" />

### Student Management

<img width="1901" height="911" alt="Screenshot 2026-07-06 164112" src="https://github.com/user-attachments/assets/659c355e-0c18-4425-b721-45fca81ac9ee" />


### Attendance


<img width="1450" height="641" alt="Screenshot 2026-07-06 164212" src="https://github.com/user-attachments/assets/455e677e-2071-45c0-8c57-f24e16269b2b" />

### Attendance Report

<img width="1466" height="685" alt="Screenshot 2026-07-06 164337" src="https://github.com/user-attachments/assets/d6814289-3258-4bdd-877f-bbd58a148cc6" />


### Faculty Management

<img width="1462" height="652" alt="Screenshot 2026-07-06 164352" src="https://github.com/user-attachments/assets/1102517c-7e59-4fa1-8cc3-8b2cdcd9f6b8" />


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

3rd Year 

Department of Information Technology

---

## 📄 License

This project is developed for educational purposes.
