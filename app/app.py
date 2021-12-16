
"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.evolution_controller import EvolutionController
from app.controllers.inventors_controller import InventorsController
from app.controllers.article1_controller import ArticleController
from app.controllers.article2_controller import ArticleBController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/basicform", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/basicform", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/evolution", methods=['GET'])
def evolution_get():
    return EvolutionController.get()

@app.route("/inventors", methods=['GET'])
def inventors_get():
    return InventorsController.get()

@app.route("/article1", methods=['GET'])
def article1_get():
    return ArticleController.get()

@app.route("/article2", methods=['GET'])
def article2_get():
    return ArticleBController.get()