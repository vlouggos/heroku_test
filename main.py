from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
DATABASE_URL = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL


@app.route("/")
def home():
    return DATABASE_URL



if __name__ == "__main__":
    app.run()
