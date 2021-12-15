"""A simple flask web app"""
from flask import Flask, request
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalcController
from app.controllers.result_controller import ResultController
from app.controllers.article_controller import articleController
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    """index routing to controller"""
    return IndexController.get()

@app.route("/Results Table", methods=['GET'])
def result_get():
    """result page routing to controller"""
    return ResultController.get()

@app.route("/opps", methods=['GET'])
def ooppage_get():
    """OOP page routing to controller"""
    return articleController.get()

@app.route("/calculator1", methods=['GET'])
def calculator_get():
    return CalcController.get()

@app.route("/calculator1", methods=['POST'])
def calculator_post():
    return CalcController.post()
