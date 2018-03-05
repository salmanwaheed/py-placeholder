# myname/logo placeholder
# make different shapes

import os
from imgx.lib import colormap
from io import BytesIO

try:
    from PIL import Image, ImageDraw, ImageFont
    from flask import send_file
except ImportError:
    pass

class DrawAnImage(object):

    # imutable default values
    __mode                  = 'RGBA'
    __abs_path              = os.path.abspath( os.path.dirname( os.path.dirname( __file__ ) ) )
    __font_path             = 'fonts'
    __font_name             = 'arial.ttf'

    def __init__(self,
                    width    = None, height   = None,
                    bgcolor  = None, txt      = None,
                    txtsize  = None, txtcolor = None,
                    txtalign = None
                ):

        #mutable values
        self.width, self.height    = (width, height)
        self.bgcolor               = bgcolor
        self.txt                   = txt
        self.txtcolor              = txtcolor
        self.txtsize               = txtsize
        self.txtalign              = txtalign

    def make_an_image(self):
        # make a blank image for text
        blank_image = Image.new(
                    mode  = self.__mode,
                    size  = ( self.__width__(), self.__height__() ),
                    color = self.__bgcolor__()
                )

        # get a drawing context
        draw = ImageDraw.Draw( blank_image )

        # get text size
        txtsize = draw.textsize( self.__txt__() )

        # add text inside the image
        if self.__txt__():
            draw.text(
                    self.__txtalign__(txtsize = txtsize),
                    self.__txt__(),
                    font = self.__font_type__,
                    fill = self.__txtcolor__()
                )

        byte_io = BytesIO()
        blank_image.save(byte_io, 'png')
        byte_io.seek(0)

        # make dummy image in memory, no save
        return send_file(byte_io, mimetype='image/png')

    def __width__(self, default = 300):
        return self.width if self.width else default

    def __height__(self, default = 200):
        return self.height if self.height else default

    def __bgcolor__(self, default = 'dimgrey'):
        return self.bgcolor if self.bgcolor else default

    def __txt__(self, default = '300x200'):
        return self.txt if self.txt != None else '{}x{}'.format(self.width, self.height)

    def __txtcolor__(self, default = 'black'):
        return self.txtcolor if self.txtcolor else default

    def __txtsize__(self, default = 40):
        return self.txtsize if self.txtsize else default

    def __txtalign__(self, txtsize = None):
        txtX, txtY = txtsize
        rightX = ( self.__width__() - txtX ) - 50
        bottomY = ( self.__height__() - txtY ) - 20

        # default value
        if self.txtalign == 'top,left':
            x, y = (10, 10)
        elif self.txtalign == 'top,right':
            x, y = (rightX, 10)
        elif self.txtalign == 'bottom,left':
            x, y = (10, bottomY)
        elif self.txtalign == 'bottom,right':
            x, y = (rightX, bottomY)
        else:
            # centerX = (self.__width__() - txtX - 40) / 2
            centerX = ( self.__width__() - txtX ) / 2 - txtX / 2
            centerY = (self.__height__() - txtY - 15) / 2
            x, y = (centerX, centerY)

        return ( x, y )

    # get a font
    @property
    def __font_type__(self):
        font_full_path = os.path.join(self.__abs_path, self.__font_path, self.__font_name)
        return ImageFont.truetype(font_full_path, self.__txtsize__())
