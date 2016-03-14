from flask import Flask, url_for, render_template, request, redirect
from database_setup import Restaurant, MenuItem, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Boiler-plate stuff
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

restaurants = []

@app.route('/')
@app.route('/restaurants')
def show_restaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)


@app.route('/<int:rid>/menu')
def show_menu(rid):
    restaurant = session.query(Restaurant).filter_by(id=rid).one()
    items = session.query(MenuItem).filter_by(restaurant_id=rid).all()
    return render_template('menu.html', restaurant=restaurant, items=items)


@app.route('/<int:rid>/rename', methods=['GET', 'POST'])
def rename_restaurant(rid):
    restaurant = session.query(Restaurant).filter_by(id=rid).one()
    if request.method == 'GET':
        return render_template('rename_restaurant.html', restaurant=restaurant)
    elif request.method == 'POST':
        new_name = request.form['new_restaurant_name']
        restaurant.name = new_name
        session.commit()
        return redirect(url_for('show_restaurants'))


@app.route('/<int:rid>/<int:miid>/rename', methods=['GET', 'POST'])
def rename_menu_item(rid, miid):
    item = session.query(MenuItem).filter_by(id=miid).one()
    assert(item.restaurant_id == rid)
    if request.method == 'GET':
        return render_template('rename_menu_item.html', restaurant=item.restaurant,
                item=item)
    elif request.method == 'POST':
        assert(len(request.form.items())==1)
        new_name = request.form.values()[0]
        item.name = new_name
        session.commit()
        return redirect(url_for('show_menu', rid=rid))


@app.route('/<int:rid>/create_menu_item', methods=['GET', 'POST'])
def create_menu_item(rid):
    restaurant = session.query(Restaurant).filter_by(id=rid).one()
    if request.method == 'GET':
        return render_template('create_menu_item.html', restaurant=restaurant)
    elif request.method == 'POST':
        assert(len(request.form.items())==1)
        name = request.form.values()[0]
        session.add(MenuItem(name=name, restaurant_id=rid))
        session.commit()
        return redirect(url_for('show_menu', rid=rid))


@app.route('/create_restaurant', methods=['GET', 'POST'])
def create_restaurant():
    if request.method == 'GET':
        return render_template('create_restaurant.html')
    elif request.method == 'POST':
        assert(len(request.form.items())==1)
        name = request.form.values()[0]
        session.add(Restaurant(name=name))
        session.commit()
        return redirect(url_for('show_restaurants'))


@app.route('/<int:rid>/delete_restaurant', methods=['POST'])
def delete_restaurant(rid):
    restaurant = session.query(Restaurant).filter_by(id=rid).one()
    items = session.query(MenuItem).filter_by(restaurant_id=rid).delete()
    session.delete(restaurant)
    session.commit()
    return redirect(url_for('show_restaurants'))

@app.route('/<int:rid>/<int:miid>/delete_menu_item', methods=['POST'])
def delete_menu_item(rid, miid):
    item = session.query(MenuItem).filter_by(id=miid).one()
    assert(item.restaurant_id == rid)
    session.delete(item)
    return redirect(url_for('show_menu', rid=rid))

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0', port=8080)
