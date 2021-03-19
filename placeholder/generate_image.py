import os
from io import BytesIO

try:
  from PIL import Image, ImageDraw, ImageFont, ImageShow
  from flask import send_file
except ImportError:
  pass

class GenerateImage:
  def __init__(
    self,
    width=None,
    height=None,
    bgcolor=None,
    text=None,
    textsize=None,
    textcolor=None,
    textalign=None
  ):
    self._width = width or 300
    self._height = height or 200
    self._bgcolor = bgcolor or 'darkgray'
    self._text = text or '300x200'
    self._textcolor = textcolor or 'black'
    self._textsize = textsize or 20
    self._textalign = textalign or 'center'

  def make_an_image(self):
    blank_image = Image.new(mode='RGBA', size=(self._width, self._height), color=self._bgcolor)
    draw = ImageDraw.Draw(blank_image)
    textsize = draw.textsize(self._text)
    if self._text or self._text is not None:
      draw.text(self.text_align(textsize=textsize), str(self._text), font=self.font_type, fill=self._textcolor)

    byte_io = BytesIO()
    blank_image.save(byte_io, 'png')
    byte_io.seek(0)

    return send_file(byte_io,  mimetype='image/png')

  def text_align(self, textsize=None):
    textX, textY = textsize
    rightX = ((self._width - textX) / 2) + 70
    bottomY = ((self._height - textY) / 1.1) - 10

    if self._textalign == 'top,left':
      x, y = (10, 0)
    elif self._textalign == 'top,right':
      x, y = (rightX, 0)
    elif self._textalign == 'bottom,left':
      x, y = (10, bottomY)
    elif self._textalign == 'bottom,right':
      x, y = (rightX, bottomY)
    else:
      centerX = (self._width / 2) - (self._textsize * 2.3)
      centerY = (self._height - self._textsize) / 2
      x, y = (centerX, centerY)

    return (x, y)

  @property
  def font_type(self):
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    font_full_path = os.path.join(path, 'fonts/arial.ttf')
    return ImageFont.truetype(font_full_path, self._textsize)
