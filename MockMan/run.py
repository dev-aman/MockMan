# This is run.py
from flask import Flask
# from flask_ngrok import run_with_ngrok

def create_app(config_filename):
    app = Flask(__name__, static_folder='mocks')
    # run_with_ngrok(app)
    app.config.from_object(config_filename)
    
    from app import api_bp
    app.register_blueprint(api_bp)
    return app

if __name__ == "__main__":
    app = create_app("config")
    app.run(host='0.0.0.0',debug=True, port=80)