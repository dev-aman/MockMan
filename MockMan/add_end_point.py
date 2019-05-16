file_content = """\
from flask_restful import Resource
from utility.FileHandler import FileHandler

class {}(Resource):
    def {}(self):
        return FileHandler.getJSONFrom("{}")
"""

end_point_content = """
from resources.{} import {}
api.add_resource({}, '{}')
"""

def addEndPoint():
    addResourceFile()
    addEndPointToApplicationFile()

def addResourceFile():
    try:
        f = open("resources/{}".format(file_name), "w+")
        f.write(file_content.format(file_name_without_extention, http_method, mock_file_name))
        f.close()
    except Exception:
        print("Not able to write data to file ", "resources/{}".format(file_name), file_content.format(file_name_without_extention, http_method, mock_file_name))


def addEndPointToApplicationFile():
    try: 
        f = open("app.py", "a")
        f.write(end_point_content.format(file_name_without_extention, file_name_without_extention, file_name_without_extention, end_point))
        f.close()
    except Exception:
        print("Not able to write data to file app.py", end_point_content.format(file_name_without_extention, end_point))


print("Enter Resource File Name: ")
file_name = input()
file_name_without_extention = file_name.replace(".py", "")
print("Enter Mock file name: ")
mock_file_name = input()
print("Enter End point eg-/v3/user/info: ")
end_point = input()
print("Enter HTTP Method eg:- get, post, put etc: ")
http_method = input()
http_method = http_method.lower()

# trigger point
addEndPoint()