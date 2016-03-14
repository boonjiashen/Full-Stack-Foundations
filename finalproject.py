from flask import Flask, url_for, render_template
from FakeMenuItems import *

app = Flask(__name__)


@app.route('/')
@app.route('/restaurants')
def show_restaurants():
    return render_template('restaurants.html', restaurants=restaurants)
    #return render_template('restaurants.html', restaurants=[])


@app.route('/<int:rid>/menu')
def show_menu(rid):
    return "here's our menu for rid %i" % rid


@app.route('/<int:rid>/rename')
def rename_restaurant(rid):
    return "here we rename rid %i" % rid


@app.route('/<int:rid>/<int:miid>/rename')
def rename_menu_item(rid, miid):
    return "here we rename miid %i of rid %i" % (miid, rid)


@app.route('/<int:rid>/create_menu_item')
def create_menu_item(rid):
    return "here we create a new menu item for rid %i" % (rid)


@app.route('/create_restaurant')
def create_restaurant():
    return "here we create a new restaurant"


@app.route('/<int:rid>/delete_restaurant', methods=['POST'])
def delete_restaurant(rid):
    return "here we delete restaurant %d" % (rid)


if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0', port=8080)
