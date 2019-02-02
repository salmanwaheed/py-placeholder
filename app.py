#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://github.com/salmanwaheed/
# https://linkedin.com/in/salmanwaheedahmed/
# https://rubygems.org/profiles/salmanwaheed/

# view jekyll theme demo
# https://salmanwaheed.github.io/plan-b/

# Copyright (c) 2018 Salman Waheed

import os
import sys
import json

from flask import Flask,render_template, request
from placeholder.lib import drawAnImage

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return json.dumps({"Error": "Page not found"}), 404

@app.errorhandler(500)
def interval_server_err(error):
    return json.dumps({"Error": "Interval Server Error"}), 500

@app.route('/', methods=['GET'])
def index():
    width = request.args.get('width',default=300,type=int)
    height = request.args.get('height',default=200,type=int)
    bgcolor = request.args.get('bgcolor',default='darkgrey',type=str)
    text = request.args.get('text',default='300x200',type=str)
    textcolor = request.args.get('textcolor',default='black',type=str)
    textsize = request.args.get('textsize',default=20,type=int)
    textalign = request.args.get('textalign',default='center',type=str)

    draw = drawAnImage.drawAnImage(width=width,height=height,bgcolor=bgcolor,
                                text=text,textsize=textsize,textcolor=textcolor,
                                textalign=textalign)

    return draw.make_an_image()

if __name__ == "__main__":
    app.run()
