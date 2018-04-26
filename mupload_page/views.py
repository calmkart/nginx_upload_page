#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-12 12:35:51
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=9527, debug=app.debug)
