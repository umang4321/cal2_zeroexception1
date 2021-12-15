from app.controllers.controller import ControllerBase
from flask import render_template

class EvolutionController(ControllerBase):
    @staticmethod
    def get():
        return render_template('evolution.html')

