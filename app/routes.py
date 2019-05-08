from app import app
from flask import render_template

#Import for postForm
from app.forms import PostForm

@app.route('/')
def helloworld():
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
