from app.controllers.controller import BaseController
from flask import render_template

class IndexController(BaseController):
    @staticmethod
    def get():
        return render_template('index.html')
