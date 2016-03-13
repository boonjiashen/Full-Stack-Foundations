from flask import Flask, request, redirect
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

def get_front_page():
    restaurants = session.query(Restaurant).all()
    def get_template(restaurant):
        return  \
                """
                <p>
                %s<br>
                <a href="/%d/edit">Edit</a><br>
                """ % (restaurant.name, restaurant.id) +  \
                """
                <form id="%d" action="/%d/delete" method="post">
                    <a href="javascript:;" onclick="document.getElementById('%d').submit();">Delete</a>
                </form>
                ---
                </p>
                """ % (restaurant.id, restaurant.id, restaurant.id)
                #<a href="/%d/delete">Delete</a><br>
    adder = """
    <p>
    <a href="add_restaurant">Add restaurant</a>
    </p>
    """
    return ''.join([get_template(x) for x in restaurants]) + adder

@app.route('/restaurants')
def restaurants():
    return get_front_page()

@app.route('/<int:rid>/edit', methods=['GET', 'POST'])
def edit_restaurant(rid):
    object = session.query(Restaurant).filter_by(id=rid).first()
    if not object:
        return "<h1>Cannot find restaurant with id %s</h1>" % rid
    curr_name = object.name
    if request.method == 'GET':
        html = """
        <p>
        New name for %s
        <form action="%s" method="POST">
        <input type="text" name="new_name">
        <input type="submit" value="Submit">
        </form>
        """ % (curr_name, request.path)  # redirect back to same path but with POST
        return html
    elif request.method == 'POST':
        new_name = request.form['new_name']
        object.name = new_name
        session.commit()
        return "Successfully renamed %s as %s" % (curr_name, new_name)

@app.route('/test')
def test():
    return """
            <form id="form1" action="showMessage.jsp" method="post">
                <a href="javascript:;" onclick="document.getElementById('form1').submit();">hi</a>
            </form>
            """
                #<input type="hidden" name="mess" value=<%=n%>/>


@app.route('/<int:rid>/delete', methods=['GET', 'POST'])
def delete_restaurant(rid):
    object = session.query(Restaurant).filter_by(id=rid).first()
    if not object:
        return "<h1>Cannot find restaurant with id %s</h1>" % rid
    name = object.name

    if request.method == 'GET':
        html = """
        Are you sure you want to delete %s?
        <form action="%s" method="POST">
        <input type="submit" value="Yes">
        </form>
        """ % (object.name, request.path)
        return html
    elif request.method == 'POST':
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
