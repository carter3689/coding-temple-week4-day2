from app import app,db
from flask import render_template,flash,redirect,url_for

#flask_login imports
from flask_login import current_user,login_user,logout_user,login_required

#Model import
from app.models import User

#Import for postForm
from app.forms import PostForm,LoginForm,RegistrationForm

import os


@app.route('/')
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/products")
def products():
    products = [
        {
            "id":"1001",
            "title":"5 tweet credits",
            "price": "2.00",
            "desc":"More tweet credits for your expression"
        },
        {
            "id":"1002",
            "title":"10 tweet credits",
            "price": "5.00",
            "desc":"Even more tweet credits for your expression"
        },
        {
            "id":"1003",
            "title":"15 tweet credits",
            "price": "10.00",
            "desc":"More tweet credits for your expression"
        },
        {
            "id":"1004",
            "title":"20 tweet credits",
            "price": "20.00",
            "desc":"But wait...there's more tweet credits for you're expression"
        }
    ]
    return render_template('products.html',products = products)

@app.route('/post',methods=["GET","POST"])
def postForm():
    form = PostForm()

    if form.validate_on_submit():
        title = form.title.data
        tweet = form.post.data
        # post = Post(title = title, tweet = tweet) TODO Create Post Class
    return render_template("post.html",form = form)

# Register Route for Register Form
@app.route('/register', methods = ["GET","POST"])
def register():
    # Check to see if user is authenticated
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()

    # Validate form on submit
    if form.validate_on_submit():
        user = User(email = form.email.data,password_hash = form.password.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you have successfully registered.")
        return redirect(url_for('login'))

    return render_template("register.html", form=form)

# Login Route for Login Form

@app.route('/login',methods = ["GET","POST"])
def login():
    #Check the user authentication
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid email or password")
            return redirect(url_for('login'))
        login_user(user,remember=form.remember_me.data)
        flash("Login Requested for user {}, remember_me = {}".format(form.email.data, form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html',title="Sign In", form = form)

        