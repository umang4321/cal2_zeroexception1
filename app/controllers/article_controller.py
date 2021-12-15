from app.controllers.controller import BaseController
from flask import render_template

class articleController(BaseController):
    @staticmethod
    def get():
        return render_template('opps.html')
