from app.controllers.controller import ControllerBase
from flask import render_template

class InventorsController(ControllerBase):
    @staticmethod
    def get():
        return render_template('inventors.html')

