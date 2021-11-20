"""
Author: Douglas Klos
Date: 18th November 2021
github: https://github.com/Douglas-Klos/syntax-highlighter

This is a work in progress

https://syntax-highlighter.herokuapp.com/

import sys
print('', file=sys.stderr)
"""

from flask import Flask
from os import urandom

app = Flask(__name__)
app.config['SECRET_KEY'] = urandom(128)

from flask import render_template, request, redirect, url_for, session
from passlib.hash import pbkdf2_sha256
from peewee import Model
from pygments import highlight
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.formatters import HtmlFormatter

from app.model import User, Post


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("main.jinja2")


@app.route("/syntax", methods=["GET", "POST"])
def syntax():

    lexers = sorted([x[0] for x in [x[1] for x in get_all_lexers()] if len(x) > 1])
    lexers.insert(0, lexers.pop(lexers.index("javascript")))
    lexers.insert(0, lexers.pop(lexers.index("cython")))
    lexers.insert(0, lexers.pop(lexers.index("python")))

    if request.method == "GET":
        return render_template(
            "syntax_highlighting.jinja2",
            all_lexers=lexers,
        )

    if request.method == "POST":
        return render_template(
            "syntax_highlighting.jinja2",
            all_lexers=lexers,
            user_input=highlight(
                request.form["user_input"],
                get_lexer_by_name(request.form["colour"]),
                HtmlFormatter(linenos="table"),
            ),
        )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            user = User.select().where(User.name == request.form["name"]).get()

            if user and pbkdf2_sha256.verify(request.form["password"], user.password):
                session["username"] = request.form["name"]
                return redirect(url_for("syntax"))

        except User.DoesNotExist:
            pass

        return render_template(
            "login.jinja2",
            error="Incorrect username or password.",
        )

    else:
        return render_template("login.jinja2")


@app.route("/writings", methods=["GET"])
def writings():
    return render_template("writings.jinja2")


@app.route("/helpers", methods=["GET"])
def helpers():
    return render_template("helpers.jinja2")


@app.route("/learning_paths", methods=["GET"])
def learning_paths():
    return render_template("learning_paths.jinja2")


@app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.jinja2")
