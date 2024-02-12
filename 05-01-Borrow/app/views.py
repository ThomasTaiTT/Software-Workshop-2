from flask import render_template, redirect, url_for, flash
from app import app
from datetime import datetime
from app.forms import AddStudentFrom
from app.models import Student
from app import db
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/datetime')
def date_time():
    now = datetime.now()
    return render_template('datetime.html', now=now)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = AddStudentFrom()
    if form.validate_on_submit():
        new_student = Student(username=form.username.data, firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data)
        db.session.add(new_student)
        try:
            db.session.commit()
            flash(f'New studnet added: {form.username.data} received', 'success')
            return redirect(url_for('index'))
        except:
            db.session.rollback()
            if Student.query.filter_by(username=form.username.data).first():
                form.username.errors.append('Username already taken. Please choose another')
            if Student.query.filter_by(email=form.email.data).first():
                form.email.errors.append('Email already taken. Please choose another')
    return render_template('add_student.html', title='Add Student', form=form)