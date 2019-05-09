from flask_restful import Resource
from utility.FileHandler import FileHandler

class HomeCards(Resource):
    def get(self):
        return FileHandler.getJSONFrom("homeCards.json")






