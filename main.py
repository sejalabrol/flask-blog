from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("my_email")
password = os.getenv("password")

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


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        send_mail(data["name"], data["email"], data["phone"], data["message"])
        return render_template(
            "contact.html", heading="Your message was sent successfully"
        )
    elif request.method == "GET":
        return render_template("contact.html", heading="Contact Me")


def send_mail(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)  # or (my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}",
        )


if __name__ == "__main__":
    app.run(debug=True)
