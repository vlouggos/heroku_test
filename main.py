from flask import Flask
import os

app = Flask(__name__)
DATABASE_URL = os.environ.get("DATABASE_URL")



@app.route("/")
def home():
    return DATABASE_URL



if __name__ == "__main__":
    app.run()
