from flask import Flask
from flask import jsonify
import pandas as pd
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/Prediction')
def GetPrediction():
    return jsonify(
        Prediction()
    )

@app.route('/Predictions', methods = ['GET'])
def GetPredictions():
    return Predictions()

@app.route('/User', methods = ['GET'])
def GetUser():
    return User()

@app.route('/register', methods = ['Post'])
def PostUser():
    return CreateUser()

@app.route('/Login', methods = ['Post'])
def Login():
    return LoginUser()

def User():
    return 1

def CreateUser():
    return 2

def LoginUser():
    return 3

def Predictions():
    list = [1,2,3]
    return list

def Prediction():
    folder = pd.read_csv('Predictie.csv')
    folder.drop(folder.columns.difference(['timestamp','close']), 1, inplace=True)
    folder.columns=["timestamp","close"]
    folder.set_index('timestamp',inplace=True)
    result= folder.to_json(orient="table")
    parsed = json.loads(result)
    return parsed
