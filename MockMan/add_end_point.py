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

class RollbackException(Exception):
    pass

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
        print("Not able to write data to resources")
        raise RollbackException


def addMockJSONFiles():
    if not os.path.exists("mocks"):
        os.makedirs("mocks")
    mock_dir_path = "mocks/"+file_name_without_extention
    if not os.path.exists(mock_dir_path):
        os.makedirs(mock_dir_path)
    else:
        shutil.rmtree(mock_dir_path)
    try:
        json_file_path = mock_dir_path+"/"+mock_file_name
        http_methods = ["get", "post", "put", "delete", "patch"]
        for method in http_methods:            
            f = open(json_file_path+"_{}.json".format(method), "w+")
            f.write("{}")
            f.close()
    except Exception:
        print("Not able to write data to file mock json files")
        raise RollbackException

def addEndPointToApplicationFile():
    try: 
        f = open("app.py", "a")
        f.write(end_point_content.format(file_name_without_extention, file_name_without_extention, file_name_without_extention, end_point))
        f.close()
    except Exception:
        print("Not able to write data to file app.py", end_point_content.format(file_name_without_extention, end_point))
        raise RollbackException


def createBackup():
    cwd = os.getcwd()
    try:
        shutil.copytree("../../mock-man", "../mock-man-backup")
    except Exception as e:
        print(e)
        print("Backup already exists, enter yes if you want delete the backup and continue and  no if you want to exit and restore the backup first!")
        continue_delete = input()
        if "y" in continue_delete.lower():
            print("Removing Backup files...")
            removeBackup()
            createBackup()
        else:
            exit()


def removeBackup():
    shutil.rmtree("../mock-man-backup")


print("Enter Module Name: ")
file_name = input()
file_name_without_extention = file_name.replace(".py", "")
file_name = file_name_without_extention+".py"
mock_file_name = file_name_without_extention
print("Enter End point eg-/v3/user/info: ")
end_point = input()

# trigger point
createBackup()
try:
    addEndPoint()
    removeBackup()
except RollbackException:
    print("FAILED TO ADD END POINT", end_point)
    print("You can rollback by running rollback.py script")