from flask import Blueprint
from flask_restful import Api
from resources.HealthCheck import HealthCheck
from resources.Home import Home
from resources.AASA import AASA

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(HealthCheck, '/')

# Route
api.add_resource(Home, '/apple-app-site-association')

api.add_resource(AASA, '/.well-known/apple-app-site-association')

from resources.UpdateMockData import UpdateMockData
api.add_resource(UpdateMockData, '/updateMockData')
