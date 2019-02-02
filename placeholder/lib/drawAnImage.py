#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://github.com/salmanwaheed/
# https://linkedin.com/in/salmanwaheedahmed/
# https://rubygems.org/profiles/salmanwaheed/

# view jekyll theme demo
# https://salmanwaheed.github.io/plan-b/

# Copyright (c) 2018 Salman Waheed

import os
from placeholder.lib import colorMap
from io import BytesIO

try:
    from PIL import Image,ImageDraw,ImageFont
    from flask import send_file
except ImportError:
    pass

class drawAnImage(object):

    _mode                  = 'RGBA'
    _abs_path              = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    _font_path             = 'fonts'
    _font_name             = 'arial.ttf'

    def __init__(self,width=300,height=200,bgcolor='darkgray',
                    text='300x200',textsize=20,textcolor='black',textalign='center'):

        self._width,self._height = (width,height)
        self._bgcolor = bgcolor
        self._text = text
        self._textcolor = textcolor
        self._textsize = textsize
        self._textalign = textalign

    def make_an_image(self):
        blank_image = Image.new(mode=self._mode,size=(self._width,self._height),color=self._bgcolor)
        draw = ImageDraw.Draw(blank_image)
        textsize = draw.textsize(self._text)
        if self._text or self._text != None:
            draw.text(self.text_align(textsize=textsize),self._text,font=self.font_type,fill=self._textcolor)

        byte_io = BytesIO()
        blank_image.save(byte_io,'png')
        byte_io.seek(0)

        return send_file(byte_io,mimetype='image/png')

    def text_align(self,textsize=None):
        textX,textY = textsize
        rightX = (self._width - textX) - 50
        bottomY = (self._height - textY) - 20

        if self._textalign == 'top,left':
            x,y = (10,10)
        elif self._textalign == 'top,right':
            x,y = (rightX,10)
        elif self._textalign == 'bottom,left':
            x,y = (10,bottomY)
        elif self._textalign == 'bottom,right':
            x,y = (rightX,bottomY)
        else:
            centerX = (self._width - textX) / 2 - textX / 2
            centerY = (self._height - textY - 15) / 2
            x,y = (centerX,centerY)

        return (x,y)

    @property
    def font_type(self):
        font_full_path = os.path.join(self._abs_path,self._font_path,self._font_name)
        return ImageFont.truetype(font_full_path,self._textsize)
