from flask_restful import Resource
from utility.FileHandler import FileHandler

class HealthCheck(Resource):
    def get(self):
        return FileHandler.getJSONFrom("health_check.json")