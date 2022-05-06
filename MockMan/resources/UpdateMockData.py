from flask_restful import Resource
from flask import request
import json

class UpdateMockData(Resource):

    def get(self):
        return self.writeJsonMock("get")


    def post(self):
        return self.writeJsonMock("post")        


    def put(self):
        return self.writeJsonMock("put")        


    def delete(self):
        return self.writeJsonMock("delete")        


    def patch(self):
        return self.writeJsonMock("patch")        


    def writeJsonMock(self, method_type):
        module_name = request.args.get('module')
        json_data = request.get_json(force=True)
        try: 
            file_name = "mocks/{}/{}_{}.json".format(module_name, module_name, method_type)
            f = open(file_name, "w")
            f.write(json.dumps(json_data))
            f.close()
            return { "status": True }
        except Exception as exception:
            print(exception)
            return { "status": False }
