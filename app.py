import os
import sys

from flask import Flask, request, jsonify
from placeholder.generate_image import GenerateImage

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
  return jsonify({'error': 'Page not found'}), 404

# @app.errorhandler(500)
# def interval_server_err(error):
#   return jsonify({'error': 'Interval Server Error'}), 500

@app.route('/', methods=('get',))
def index():
  # default_width = 300
  # default_height = 200
  # default_text = f'{request.args.get("width") or default_width}x{request.args.get("height") or default_height}'

  generate_image = GenerateImage(
    width=request.args.get('width', type=int),
    height=request.args.get('height', type=int),
    bgcolor=request.args.get('bgcolor', type=str),
    text=request.args.get('text', type=str),
    textcolor=request.args.get('textcolor', type=str),
    textsize=request.args.get('textsize', type=int),
    textalign=request.args.get('textalign', type=str)
  )

  return generate_image.make_an_image()

if __name__ == '__main__':
  app.main()
