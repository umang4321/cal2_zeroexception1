from app.controllers.controller import BaseController
from tests.readcsv import Read
from flask import render_template

class ResultController(BaseController):
    @staticmethod
    def get():
        df = Read.csvreader()
        return render_template('Results Table.html', titles=df.columns.values, row_data=list(df.values.tolist()), zip=zip)
