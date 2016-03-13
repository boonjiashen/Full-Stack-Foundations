from flask import Flask, request
from database_setup import Restaurant, MenuItem, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Boiler-plate stuff
engine=create_engine('sqlite:///Lesson_1/restaurantmenu.db')
Base.metadata.bind=engine
DBSession=sessionmaker(bind=engine)
session=DBSession()


@app.route('/hello')
def hello_world():
    return 'hi mortal'

@app.route('/hola')
def hola():
    return 'hola!'

@app.route('/restaurants')
def restaurants():
    names = [x.name for x in session.query(Restaurant).all()]
    template = """
    <p>
    %s<br>
    <a href="">Edit</a><br>
    <a href="">Delete</a>
    </p>
    """
    return ''.join([template % name for name in names])

@app.route('/')
def form():
    return """
    <form action="display" method="POST">
    <input type="text" name="text">
    <input type="submit" name="my_form" value="Submit">
    </form>
    """

@app.route('/display', methods=['POST'])
def form_post():
    received = request.form['text']
    return 'you posted: ' + received


if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0', port=8080)
