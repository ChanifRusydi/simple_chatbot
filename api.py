from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import keras
import numpy as np
import json

app=Flask(__name__)
api=Api(app)

parser =reqparse.RequestParser()
parser.add_argument('data')

class Chatbot(Resource):
    def post(self):
        args=parser.parse_args()
        X=np.array(json.loads(args['data']))
        prediction=model.predict(X)
        return jsonify(prediction.tolist())


api.add_resource(Chatbot, '/chatbot')
if __name__ == '__main__':
    model=keras.models.load_model('chatbot_model.h5')
    app.run(debug=True)