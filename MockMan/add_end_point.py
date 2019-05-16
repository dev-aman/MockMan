import os
import shutil

file_content = """\
from flask_restful import Resource
from utility.FileHandler import FileHandler

class {}(Resource):
    def get(self):
        return FileHandler.getJSONFrom("{}")


    def post(self):
        return FileHandler.getJSONFrom("{}")


    def put(self):
        return FileHandler.getJSONFrom("{}")


    def delete(self):
        return FileHandler.getJSONFrom("{}")
    

    def patch(self):
        return FileHandler.getJSONFrom("{}")
"""

end_point_content = """
from resources.{} import {}
api.add_resource({}, '{}')
"""

def addEndPoint():
    addResourceFile()
    addEndPointToApplicationFile()
    addMockJSONFiles()


def addResourceFile():
    try:
        f = open("resources/{}".format(file_name), "w+")
        json_file_path = file_name_without_extention+"/"+mock_file_name
        f.write(file_content.format(file_name_without_extention, json_file_path+"_get.json", json_file_path+"_post.json", json_file_path+"_put.json", json_file_path+"_delete.json", json_file_path+"_patch.json"))
        f.close()
    except Exception:
        print("Not able to write data to file ", "resources/{}".format(file_content.format(file_name_without_extention, json_file_path+"_get.json", json_file_path+"_post.json", json_file_path+"_put.json", json_file_path+"_delete.json", json_file_path+"_patch.json")))


def addMockJSONFiles():
    if not os.path.exists("mocks"):
        os.makedirs("mocks")
    mockDirPath = "mocks/"+file_name_without_extention
    if not os.path.exists(mockDirPath):
        os.makedirs(mockDirPath)
    else:
        shutil.rmtree(mockDirPath)
    try:
        json_file_path = mockDirPath+"/"+mock_file_name
        httpMethods = ["get", "post", "put", "delete", "patch"]
        for method in httpMethods:            
            f = open(json_file_path+"_{}.json".format(method), "w+")
            f.write("{}")
            f.close()
    except Exception:
        print("Not able to write data to file mock json files")

def addEndPointToApplicationFile():
    try: 
        f = open("app.py", "a")
        f.write(end_point_content.format(file_name_without_extention, file_name_without_extention, file_name_without_extention, end_point))
        f.close()
    except Exception:
        print("Not able to write data to file app.py", end_point_content.format(file_name_without_extention, end_point))


print("Enter Module Name: ")
file_name = input()
file_name_without_extention = file_name.replace(".py", "")
file_name = file_name_without_extention+".py"
mock_file_name = file_name_without_extention
print("Enter End point eg-/v3/user/info: ")
end_point = input()

# trigger point
addEndPoint()