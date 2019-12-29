from flask import Flask, abort, request, jsonify
from flask_restful import Resource, Api

import math  
import json
app = Flask(__name__)
api = Api(app)
from ..controller.primeChecker import PrimeChecker

class IsPrime(Resource):
    def get(self):
        return 'true'

    def post(self):
        data=request.json
        number=data['number']
        return PrimeChecker().isTwoSidedPrime(number)

api.add_resource(IsPrime, '/isTwoSidedPrime')


@app.errorhandler(404)
def not_found(e):
    return '', 404

