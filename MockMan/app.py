from flask import Blueprint
from flask_restful import Api
from resources.HealthCheck import HealthCheck
from resources.HomeCards import HomeCards

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(HealthCheck, '/healthCheck')
api.add_resource(HomeCards, '/homeCards')