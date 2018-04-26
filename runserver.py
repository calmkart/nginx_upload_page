#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-12 12:34:32
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from __future__ import absolute_import
from mupload_page.views import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9527, debug=app.debug)
