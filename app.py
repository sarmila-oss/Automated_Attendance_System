from flask import Flask, render_template, request, redirect, url_for
from config import db
from datetime import date
from openpyxl import Workbook
from flask import send_file
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")
@app.route('/dashboard')
def dashboard():
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]
    today = date.today()
    cursor.execute("""
        SELECT COUNT(*)
        FROM attendance
        WHERE attendance_date=%s
        AND status='Present'
    """,(today,))
    present = cursor.fetchone()[0]
    cursor.execute("""
        SELECT COUNT(*)
        FROM attendance
        WHERE attendance_date=%s
        AND status='Absent'
    """,(today,))
    absent = cursor.fetchone()[0]
    plt.figure(figsize=(4,4))
    plt.pie(
        [present, absent],
        labels=["Present","Absent"],
        autopct="%1.1f%%",
        startangle=90
    )
    os.makedirs("static", exist_ok=True)
    plt.savefig("static/chart.png")
    plt.close()
    return render_template(
        "dashboard.html",
        total_students=total_students,
        present=present,
        absent=absent
    )

@app.route('/check_login', methods=['POST'])
def check_login():
    username = request.form['username']
    password = request.form['password']
    if username == "admin" and password == "1234":
        return redirect(url_for('dashboard'))
    return "Invalid Username or Password"
@app.route('/save_student', methods=['POST'])
def save_student():
    name = request.form['name']
    roll_no = request.form['roll_no']
    department = request.form['department']
    year = request.form['year']
    email = request.form['email']
    phone = request.form['phone']
    cursor = db.cursor()
    sql = """
    INSERT INTO students(name, roll_no, department, year, email, phone)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (name, roll_no, department, year, email, phone)
    cursor.execute(sql, values)
    print("Rows inserted:", cursor.rowcount)
    db.commit()
    print("Commit Done")
    cursor.execute("SELECT * FROM students")
    print(cursor.fetchall())
    return redirect(url_for('dashboard'))

@app.route('/add_student')
def add_student_page():
    return render_template("add_student.html")

@app.route('/students')
def students():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    student_data = cursor.fetchall()
    return render_template("students.html", students=student_data)

@app.route('/edit_student/<int:id>')
def edit_student(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cursor.fetchone()
    return render_template("edit_student.html", student=student)

@app.route('/update_student', methods=['POST'])
def update_student():
    id = request.form['id']
    name = request.form['name']
    roll_no = request.form['roll_no']
    department = request.form['department']
    year = request.form['year']
    email = request.form['email']
    phone = request.form['phone']
    cursor = db.cursor()
    sql = """
    UPDATE students
    SET name=%s,
        roll_no=%s,
        department=%s,
        year=%s,
        email=%s,
        phone=%s
    WHERE id=%s
    """
    values = (name, roll_no, department, year, email, phone, id)
    cursor.execute(sql, values)
    db.commit()
    return redirect('/students')

@app.route('/delete_student/<int:id>')
def delete_student(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    db.commit()
    return redirect('/students')

@app.route('/attendance')
def attendance():
    cursor = db.cursor()
    cursor.execute("SELECT id, name, roll_no FROM students")
    students = cursor.fetchall()
    return render_template("attendance.html", students=students)

@app.route('/save_attendance', methods=['POST'])
def save_attendance():
    cursor = db.cursor()
    cursor.execute("SELECT id FROM students")
    students = cursor.fetchall()
    today = date.today()
    for student in students:
        student_id = student[0]
        status = request.form.get(f"status{student_id}")
        cursor.execute(
            "SELECT id FROM attendance WHERE student_id=%s AND attendance_date=%s",
            (student_id, today)
        )
        existing = cursor.fetchone()
        if existing:
            cursor.execute(
                """
                UPDATE attendance
                SET status=%s
                WHERE student_id=%s AND attendance_date=%s
                """,
                (status, student_id, today)
            )
        else:
            cursor.execute(
                """
                INSERT INTO attendance(student_id, attendance_date, status)
                VALUES(%s,%s,%s)
                """,
                (student_id, today, status)
            )
    db.commit()
    return redirect('/attendance_report')

@app.route('/attendance_report')
def attendance_report():
    cursor = db.cursor()
    selected_date = request.args.get('date')
    search = request.args.get('search')
    if search:
        sql = """
        SELECT attendance.id,
            students.name,
            students.roll_no,
            attendance.attendance_date,
            attendance.status
        FROM attendance
        INNER JOIN students
        ON attendance.student_id = students.id
        WHERE students.name LIKE %s
        OR students.roll_no LIKE %s
        ORDER BY attendance.attendance_date DESC
        """
        value = ("%" + search + "%", "%" + search + "%")
        cursor.execute(sql, value)
    elif selected_date:
        sql = """
        SELECT attendance.id,
               students.name,
               students.roll_no,
               attendance.attendance_date,
               attendance.status
        FROM attendance
        INNER JOIN students
        ON attendance.student_id = students.id
        WHERE attendance.attendance_date=%s
        ORDER BY attendance.attendance_date DESC
        """
        cursor.execute(sql, (selected_date,))
    else:
        sql = """
        SELECT attendance.id,
               students.name,
               students.roll_no,
               attendance.attendance_date,
               attendance.status
        FROM attendance
        INNER JOIN students
        ON attendance.student_id = students.id
        ORDER BY attendance.attendance_date DESC
        """
        cursor.execute(sql)
    report = cursor.fetchall()
    return render_template(
        "attendance_report.html",
        report=report
    )
    return render_template("attendance_report.html", report=report)

@app.route('/faculty')
def faculty():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM faculty")
    faculty = cursor.fetchall()
    return render_template("faculty.html", faculty=faculty)

@app.route('/add_faculty')
def add_faculty():
    return render_template("add_faculty.html")

@app.route('/save_faculty', methods=['POST'])
def save_faculty():
    name = request.form['name']
    department = request.form['department']
    email = request.form['email']
    phone = request.form['phone']
    cursor = db.cursor()
    sql = """
    INSERT INTO faculty(name, department, email, phone)
    VALUES(%s, %s, %s, %s)
    """
    values = (name, department, email, phone)
    cursor.execute(sql, values)
    db.commit()
    return redirect('/faculty')

@app.route('/edit_faculty/<int:id>')
def edit_faculty(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM faculty WHERE id=%s", (id,))
    faculty = cursor.fetchone()
    return render_template("edit_faculty.html", faculty=faculty)

@app.route('/update_faculty', methods=['POST'])
def update_faculty():
    id = request.form['id']
    name = request.form['name']
    department = request.form['department']
    email = request.form['email']
    phone = request.form['phone']
    cursor = db.cursor()
    sql = """
    UPDATE faculty
    SET name=%s,
        department=%s,
        email=%s,
        phone=%s
    WHERE id=%s
    """
    values = (name, department, email, phone, id)
    cursor.execute(sql, values)
    db.commit()
    return redirect('/faculty')

@app.route('/delete_faculty/<int:id>')
def delete_faculty(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM faculty WHERE id=%s", (id,))
    db.commit()
    return redirect('/faculty')

@app.route('/export_excel')
def export_excel():
    cursor = db.cursor()
    cursor.execute("""
    SELECT students.name,
           students.roll_no,
           attendance.attendance_date,
           attendance.status
    FROM attendance
    INNER JOIN students
    ON attendance.student_id = students.id
    """)
    data = cursor.fetchall()
    wb = Workbook()
    ws = wb.active
    ws.title = "Attendance Report"
    ws.append(["Student Name", "Roll No", "Date", "Status"])
    for row in data:
        ws.append(row)
    file_name = "Attendance_Report.xlsx"
    wb.save(file_name)
    return send_file(file_name, as_attachment=True)

@app.route('/export_pdf')
def export_pdf():
    cursor = db.cursor()
    cursor.execute("""
        SELECT students.name,
               students.roll_no,
               attendance.attendance_date,
               attendance.status
        FROM attendance
        INNER JOIN students
        ON attendance.student_id = students.id
    """)
    data = cursor.fetchall()
    pdf_file = "Attendance_Report.pdf"
    doc = SimpleDocTemplate(pdf_file)
    table_data = [["Student Name", "Roll No", "Date", "Status"]]
    for row in data:
        table_data.append(list(row))
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
    ]))
    doc.build([table])
    return send_file(pdf_file, as_attachment=True)
if __name__ == '__main__':
    app.run(debug=True)