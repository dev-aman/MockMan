from flask_restful import Resource
from utility.FileHandler import FileHandler

class HealthCheck(Resource):

    
    def get(self):
        return FileHandler.getJSONFrom("HealthCheck/HealthCheck_get.json")