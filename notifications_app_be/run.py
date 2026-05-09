from flask import Flask 
from config import Config
app=Flask(__name__)
app.config.from_object(Config)
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logging_middleware.logging_config import setup_logging
setup_logging(app)

@app.route('/')
def home():
    return {"message":"Backend Running"}

if __name__=="__main__":
    app.run(debug=True)