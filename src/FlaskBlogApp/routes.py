from flask import render_template, redirect, url_for, request, flash

from FlaskBlogApp.forms import SignupForm, LoginForm, NewArticleForm

from FlaskBlogApp import app

# import json
            # from python shell 
            # import secrets
            # secrets.token_hex(16)  e.g  
            # and voila a "SECRET_KEY"  of 16 length


@app.route("/index/")
@app.route("/")
def root():
    return render_template("index.html")


@app.route("/signup/", methods=["POST", "GET"])
def signup():
    # form = SignupForm(meta={'csrf':False})   if we want to disable secret key in THAT form
    # or  WTF_CSRF_ENABLED = False  for globally

    form = SignupForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        password2 = form.password2.data

        print(username, email, password,password2)

    return render_template("signup.html", form=form)


@app.route("/login/", methods=["POST", "GET"])
def login():
    form = LoginForm()
    # msg=""
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        print(email, password)

        flash(f"Η είσοδος του χρήστη με email: {email} στη σελίδα μας έγινε με επιτυχία","success")
        # msg = "Η είσοδος του χρήστη στη σελίδα μας έγινε με επιτυχία"
    return render_template("login.html", form=form)   # msg=msg


@app.route("/logout/")
def logout():
    return redirect(url_for("root"))


@app.route("/new_article/", methods=["POST", "GET"])
def new_article():

    form = NewArticleForm()
    if request.method == 'POST' and form.validate_on_submit():
        article_title = form.article_title.data
        article_body = form.article_body.data

        print(article_title, article_body)

    return render_template("new_article.html", form=form)
