#!/usr/bin/python
import os
import sys
sys.path.insert(0, os.path.expanduser('~/public_html/imgx/env/lib/python2.7/site-packages/'))

from flask import Flask, render_template, request
from imgx.lib import DrawAnImage

app = Flask(__name__)

@app.errorhandler(500)
def not_found(error):
    return '500', 500

@app.errorhandler(404)
def not_found(error):
    return '404', 404

@app.route('/docs', methods=['GET'])
def docs():
    return "Hello World"

# def http_error_handler(error):
#     return 'he', error.code

# for error in (401, 404, 500): # or with other http code you consider as error
#     app.error_handler_spec[None][error] = http_error_handler

@app.route('/', methods=['GET'])
def index():
    width         = request.args.get('width', default = None, type = int)
    height        = request.args.get('height', default = None, type = int)
    bgcolor       = request.args.get('bgcolor', default = None, type = str)
    txt           = request.args.get('txt', default = None, type = str)
    txtcolor      = request.args.get('txtcolor', default = None, type = str)
    txtsize       = request.args.get('txtsize', default = 18, type = int)
    txtalign      = request.args.get('txtalign', default = None, type = str)

    # instance of class/object
    draw = DrawAnImage.DrawAnImage(width = width, height = height, bgcolor = bgcolor,
                                txt = txt, txtsize = txtsize, txtcolor = txtcolor,
                                txtalign = txtalign
                             )

    return draw.make_an_image()

if __name__ == "__main__":
    app.run()
