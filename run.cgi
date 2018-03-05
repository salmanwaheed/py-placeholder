#!/usr/bin/python
from wsgiref.handlers import CGIHandler
from imgx.app import app

CGIHandler().run(app)
