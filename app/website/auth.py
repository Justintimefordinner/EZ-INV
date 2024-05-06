from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        data = request.form
        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()
        
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password, try again.", category="error")
        else:
            flash("Username does not exist.", category="error")

    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(
        url_for("auth.login")
    )  # assuming 'login' is the function that handles the login view


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("confirm_password")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("An account with this email already exists!", category="error")
            print("emailExistsError")
        elif len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
            print("emailLengthError")
        elif len(username) < 2:
            flash("First name must be greater than 1 character.", category="error")
            print("usernameLengthError")
        elif password != password2:
            flash("Passwords don't match.", category="error")
            print("passwordMatchError")
        elif len(password) < 7:
            flash("Password must be at least 7 characters.", category="error")
            print("passwordLengthError")
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password, method="scrypt"))
            db.session.add(new_user)  # add new_user to the database session
            db.session.commit()  # commit the session to save the new user
            flash("Account created successfully!", category="success")
            login_user(new_user, remember=True)
            print("accountCreated")
            return redirect(url_for("views.home"))

    return render_template("sign_up.html", user=current_user)
