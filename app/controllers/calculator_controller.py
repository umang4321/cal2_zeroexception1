import pandas as pd
from app.controllers.controller import BaseController
from calc_mod.calculator import Calculator
from calc_mod.history.calculations import Calculations
from tests.readcsv import Read
from flask import render_template, request, flash, redirect, url_for

class CalcController(BaseController):
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            flash("Please enter a valid value")
        elif request.form['value2'] == '0' and request.form['operation'] == 'division':
            flash("Division by zero not possible!")
        else:
            flash('Successful Calculation')

            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']

            my_tuple = (value1, value2)

            getattr(Calculator, operation)(my_tuple)
            result = str(Calculations.get_last_calculation_actual_value())
            Calculations.create_dataframe_to_write(value1, value2, result, operation)
            df = Read.csvreader()

            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result, tables=[df.to_html(classes='data')], titles=df.columns.values, row_data=list(df.values.tolist()), zip=zip)
        return render_template('calculator1.html')
    @staticmethod
    def get():
        return render_template('calculator1.html')