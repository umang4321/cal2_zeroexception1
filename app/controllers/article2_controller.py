from app.controllers.controller import ControllerBase
from flask import render_template

class ArticleBController(ControllerBase):
    @staticmethod
    def get():
        return render_template('article2.html')

