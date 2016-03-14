from flask import Flask, url_for, render_template, request, redirect
from FakeMenuItems import *

app = Flask(__name__)


@app.route('/')
@app.route('/restaurants')
def show_restaurants():
    return render_template('restaurants.html', restaurants=restaurants)
    #return render_template('restaurants.html', restaurants=[])


@app.route('/<int:rid>/menu')
def show_menu(rid):
    return render_template('menu.html', restaurant=restaurant, items=items)


@app.route('/<int:rid>/rename', methods=['GET', 'POST'])
def rename_restaurant(rid):
    if request.method == 'GET':
        return render_template('rename_restaurant.html', restaurant=restaurant)
    elif request.method == 'POST':
        return redirect(url_for('show_restaurants'))


@app.route('/<int:rid>/<int:miid>/rename', methods=['GET', 'POST'])
def rename_menu_item(rid, miid):
    if request.method == 'GET':
        return render_template('rename_menu_item.html', restaurant=restaurant,
                item=item)
    elif request.method == 'POST':
        return redirect(url_for('show_menu', rid=rid))


@app.route('/<int:rid>/create_menu_item')
def create_menu_item(rid):
    return "here we create a new menu item for rid %i" % (rid)


@app.route('/create_restaurant', methods=['GET', 'POST'])
def create_restaurant():
    if request.method == 'GET':
        return render_template('create_restaurant.html')
    elif request.method == 'POST':
        return redirect(url_for('show_restaurants'))


@app.route('/<int:rid>/delete_restaurant', methods=['POST'])
def delete_restaurant(rid):
    return redirect(url_for('show_restaurants'))

@app.route('/<int:rid>/<int:miid>/delete_menu_item', methods=['POST'])
def delete_menu_item(rid, miid):
    return redirect(url_for('show_menu', rid=rid))

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0', port=8080)
