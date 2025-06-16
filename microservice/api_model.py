from flask import Flask, request
from flask_restful import Api
from flask_restful import Resource, reqparse
import joblib
import pandas as pd
import numpy as nm


app = Flask(__name__)
api = Api(app)

class ML_model(Resource):
    def post(self):
        full_json_data = request.get_json()

        data = pd.DataFrame.from_dict(full_json_data)
        print(data.head())

        model = joblib.load('model_cbr.pkl')
        predict_price = model.predict(data)
        print(predict_price)

        return nm.array_str(predict_price)

api.add_resource(ML_model, "/predict")
