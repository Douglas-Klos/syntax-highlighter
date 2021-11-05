import sys
from flask import Flask, render_template, request, redirect, url_for, session

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from werkzeug.utils import HTMLBuilder

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template("syntax_highlighting.jinja2")

    if request.method == 'POST':

        return render_template(
                    'syntax_highlighting.jinja2',
                    user_input=highlight(
                        request.form["user_input"],
                        PythonLexer(),
                        HtmlFormatter(linenos='table'),
                    )
                )