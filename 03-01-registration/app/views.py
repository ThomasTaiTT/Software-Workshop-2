from flask import render_template, redirect, url_for, flash
from app import app

from app.forms import LoginForm, RegistrationForm
from datetime import datetime

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Registration for {form.username.data} received')
        return redirect(url_for('index'))
    return render_template('registration.html', title='Register', form=form)