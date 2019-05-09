# MockMan

MockMan is a Python(Flask) project, used to create a mock local server which front end developers can use at the time when the backend is being parallelly developed or delayed.

## Pre Requisites
- Python 3.7 or higher installed.
- pip 10.0.1 or higher.

## Installation

Clone the repository, open terminal and navigate to the root directory(where the `run.py` is)

```bash
python3 -m venv env
```

```bash
source env/bin/activate
```

```bash
pip3 install -r requirements.txt
```

## Usage

To add new APIs Mock follow the following steps:

- Open Project in any text editor which you are comfortable with(VS-Code, Sublime, PyCharm, etc.)
- Add your response Mock JSON file to mocks. `<MOCK_JSON_FILE_NAME.json>`
[Add screenshot]
- Go to the `resources` directory and create a new file with an appropriate name `<File_Name>`(Can be anything except the files already present in `resources`).
[Add screenshot]
- Copy the following code to the newly created file and replace the `<CLASS_NAME>` with your class name and `<MOCK_JSON_FILE_NAME.json>` with your file name.
  ```python
  from flask_restful import Resource
  from utility.FileHandler import FileHandler

  class CLASS_NAME(Resource):
      def get(self):
          return FileHandler.getJSONFrom("MOCK_JSON_FILE_NAME.json")
  ```
- Go to `app.py` first import the newly added api class using the following syntax.
   ```pyhton
   from resources.<File_Name> import <Class_Name>
   ```
  add a new route by adding the endPoint.
  ```python
  api.add_resource(HomeCards, '/v1/yourEndPoint')
  ```
[add screenshot]

 - Run the application by running the following command.
   ```bash
   python3 run.py
   ```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
