from flask import Flask, render_template
import requests

app = Flask(__name__)


endpoint = "https://api.npoint.io/c790b4d5cab58020d391"

blog_data = requests.get(endpoint).json()


@app.route("/")
def home():
    return render_template("index.html", data=blog_data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<id>")
def post(id):
    return render_template("post.html", blog=blog_data[int(id) - 1])


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
