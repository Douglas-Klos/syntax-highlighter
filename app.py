import sys
from flask import Flask, render_template, request, redirect, url_for, session

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from werkzeug.utils import HTMLBuilder

app = Flask(__name__)
app.secret_key = b'#6\xbe\xdf\xaf\xbf\xf6\xef\xa1X\xfe\xda#\xc1\x97\x1d\xb4\xad\xf2\x15\x9e\x80\xe1'

user_input = ""

""" Two Pages """
# @app.route('/', methods=['GET', 'POST'])
# def index():

#     if request.method == 'GET':
#         return render_template("user_input.html")

#     if request.method == 'POST':
#         session['user_input'] = request.form["user_input"]
#         return redirect(url_for('format_input'))


# @app.route('/syntax', methods=['GET', 'POST'])
# def format_input():

#     if request.method == 'GET':
#         return render_template(
#             'highlighted.html',
#             user_input=highlight(
#                 session['user_input'],
#                 PythonLexer(),
#                 HtmlFormatter(),
#             )
#         )
    
@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template("user_input.html")

    if request.method == 'POST':
        session['user_input'] = request.form["user_input"]

        return render_template(
                    'user_input.html',
                    user_input=highlight(
                        session['user_input'],
                        PythonLexer(),
                        HtmlFormatter(),
                    )
                )