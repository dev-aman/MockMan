from flask import Blueprint
from flask_restful import Api
from resources.HealthCheck import HealthCheck

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

## Route
# HealthCheck
api.add_resource(HealthCheck, '/healthCheck')

#UpdateMockData
from resources.UpdateMockData import UpdateMockData
api.add_resource(UpdateMockData, '/updateMockData')
