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

import routes