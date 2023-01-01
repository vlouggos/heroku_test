from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
DATABASE_URL = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)



class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)




@app.route("/")
def home():
   # new_book = Book(title="TITLE", author="AUTHOR", rating=10)
   # db.session.add(new_book)
    return DATABASE_URL



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
