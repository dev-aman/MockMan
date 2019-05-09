from flask_restful import Resource
import sqlite3

class HealthCheck(Resource):
    def get(self):
        return { 'success': True, 'status': "Mocking service is live!" }
