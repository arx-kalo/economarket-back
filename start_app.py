from flask import Flask
from flask_cors import CORS

def star_app():
    
    app = Flask(__name__)
    CORS(app,  resources={r"/*": {"origins": "*"}})
    
    return app
    