from flask_restful import Resource
from utility.FileHandler import FileHandler
from flask import send_from_directory
import os


class Home(Resource):

    
    def get(self): 
        return send_from_directory('mocks', "HealthCheck_get.txt")
