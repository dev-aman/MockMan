from flask_restful import Resource
from flask import send_from_directory

class AASA(Resource):

    def get(self): 
        return send_from_directory('mocks', "HealthCheck_get.txt")
