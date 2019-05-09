import json
import os

class FileHandler:
    def getJSONFrom(fileName: str):
        cur_path = os.getcwd()
        new_path = "/mocks/" + fileName
        print(cur_path+new_path)
        f = open(cur_path+new_path, "r")
        response = f.read()
        parsed = json.loads(response)
        return parsed