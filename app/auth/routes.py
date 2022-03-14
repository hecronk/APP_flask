from flask import render_template, flash, redirect
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html', title='Sign In', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('auth/register.html', title='Sign Up', form=form)
