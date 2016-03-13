from flask import Flask, request
from database_setup import Restaurant, MenuItem, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Boiler-plate stuff
engine=create_engine('sqlite:///restaurantmenu.db')
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
    restaurants = session.query(Restaurant).all()
    def get_template(restaurant):
        return """
                <p>
                %s<br>
                <a href="">Edit</a><br>
                <form action="delete_restaurant" method="post">
                  <button type="submit" name="rid" value="%d">Delete</button>
                </form>
                ---
                </p>
                """ % (restaurant.name, restaurant.id)
    adder = """
    <p>
    <a href="add_restaurant">Add restaurant</a>
    </p>
    """
    return ''.join([get_template(x) for x in restaurants]) + adder

@app.route('/delete_restaurant', methods=['POST'])
def delete_restaurant():
    rid = request.form['rid']
    object = session.query(Restaurant).filter_by(id=rid).first()
    if not object:
        return "<h1>Cannot find restaurant with id %s</h1>" % rid
    name = object.name
    session.delete(object)
    session.commit()
    return 'Successfully deleted restaurant %s with id <br><h1>%s</hl>' % (name, str(rid))

@app.route('/add_restaurant', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        form = """
        Restaurant name to be added
        <form action="%s" method="POST">
        <input type="text" name="text">
        <input type="submit" name="my_form" value="Submit">
        </form>
        """ % request.url_rule.rule
        return form
    elif request.method == 'POST':
        restaurant_name = request.form['text']
        session.add(Restaurant(name=restaurant_name))
        session.commit()
        html = """
        Successfully posted new restaurant
        <hl>%s</hl>
        <p><a href="restaurants">Return to restaurant list</a></p>
        """ % restaurant_name
        return html

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
    #pass
