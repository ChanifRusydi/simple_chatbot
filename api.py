from copyreg import pickle
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
import keras
import numpy as np
import json

app=Flask(__name__)
api=Api(app)
@app.route('/linearregression',methods=['POST'])


def linearregression():
    try:
        with open('my_model.pkl' , 'rb') as f:
            linear_regression_model=pickle.load(f)
        data.request.get_json()['data']
        data=np.array(data).np.reshape(1,-1)
        prediction = linear_regression_model.predict(data)
        return jsonify(prediction[0],status=200)
    except Exception as e:
        return jsonify(str(e),status=400)
class Chatbot(Resource):
    def post(self):
        args=parser.parse_args()
        X=np.array(json.loads(args['data']))
        prediction=model.predict(X)
        return jsonify(prediction.tolist())


api.add_resource(Chatbot, '/chatbot')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)